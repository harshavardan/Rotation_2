import moose
import pylab
import rdesigneur as rd
rdes = rd.rdesigneur(
    chanProto = [
        ['make_Na()','Na3'],
        #['make_K_DR()','K_DR'],
        ['./chans/kdr.xml'],
        ['make_HH_Na()', 'Na'], 
        ['make_HH_K()', 'K']
        ],
    chanDistrib = [
        ['Na3', 'soma', 'Gbar', '800' ],
        ['kdr', 'soma', 'Gbar', '1000' ]],
    stimList = [['soma', '1', '.', 'inject', '(t>0.1 && t<0.2) * 1e-7' ]],
    plotList = [['soma', '1', '.', 'Vm', 'Membrane potential']]
)

rdes.buildModel()
moose.reinit()
moose.start( 0.3 )
rdes.display()