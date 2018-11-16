import moose
print( "[INFO ] Using moose from %s" % moose.__file__ )
print( "[INFO ] Version %s" % moose.__version__ )

import pylab
import rdesigneur as rd
rdes = rd.rdesigneur(
    chanProto = [
        #['make_Na()','Na3'],
        #['make_K_DR()','K_DR'],
        ['./chans/kdr.xml'],
        ['./chans/na3.xml'],
        ['make_HH_Na()', 'Na'], 
        ['make_HH_K()', 'K']
        ],
    chanDistrib = [
        ['na3', 'soma', 'Gbar', '1200' ],
        #['kdr', 'soma', 'Gbar', '1000' ]
        ],
    stimList = [['soma', '1', '.', 'inject', '(t>0.1 && t<0.2) * 1e-7' ]],
    plotList = [['soma', '1', '.', 'Vm', 'Membrane potential']]
)

rdes.buildModel()
moose.reinit()
moose.start( 0.3 )
rdes.display()
