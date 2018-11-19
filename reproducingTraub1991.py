#import moose
#import pylab
#import rdesigneur as rd
#moose.reinit()
#rdes = rd.rdesigneur(
    ## cellProto syntax: ['ballAndStick', 'name', somaDia, somaLength, dendDia, dendLength, numDendSegments ]
    ## The numerical arguments are all optional
    #cellProto = [['ballAndStick', 'soma', 8.46e-6, 125e-6, 2.89e-6, 120e-6, 8]],
    #chanProto = [
        #['make_Na()', 'Na'],
        #['make_K_DR()', 'K_DR']
        #],
    #chanDistrib = [
        #['Na', 'soma', 'Gbar', '1200' ],
        #['K_DR', 'soma', 'Gbar', '360' ],
        #['Na', 'dend#', 'Gbar', '400' ],
        #['K_DR', 'dend#', 'Gbar', '120' ]
        #],
    #stimList = [['soma', '1', '.', 'inject', '(t>0.01 && t<0.06) * 1e-9' ]],
    #plotList = [['soma', '1', '.', 'Vm', 'Membrane potential']],
    ##moogList = [['#', '1', '.', 'Vm', 'Vm (mV)']]
#)
#rdes.buildModel()
#soma = moose.element( '/model/elec/soma' )
#moose.start(0.07)
#rdes.display()
##rdes.displayMoogli( 0.0005, 0.06, 0.0 )

import moose
import pylab
import rdesigneur as rd
rdes = rd.rdesigneur(
    chanProto = [
        ['make_Na()','Na'],
        ['make_K_DR()','K_DR'],
        #['./chans/kdr.xml'],
        #['make_HH_Na()', 'HH_Na'], 
        #['make_HH_K()', 'HH_K']
        ],
    chanDistrib = [
        ['Na', 'soma', 'Gbar', '30' ],
        ['K_DR', 'soma', 'Gbar', '25' ]
        ],
    stimList = [['soma', '1', '.', 'inject', '(t>0.1 && t<0.2) * 1e-8' ]],
    plotList = [['soma', '1', '.', 'Vm', 'Membrane potential']]
)

rdes.buildModel()
moose.reinit()
moose.start( 0.3 )
rdes.display()
#plt.savefig( '%s.png' % __file__ )