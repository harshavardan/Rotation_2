import moose
import pylab
import rdesigneur as rd
rdes = rd.rdesigneur(
    chanProto = [
        #['make_Na()','Na'],
        #['make_K_DR()','K_DR'],
        #['./chans/kdr.xml'],
        ['./chans/na3Modified.xml'],
        #['./chans/na3Mod.xml'],
        #['./otherModels/CA1PyramidalCell/neuroConstruct/generatedNeuroML/na3.xml'],
        #['make_HH_Na()', 'HH_Na'], 
        #['make_HH_K()', 'HH_K']
        ],
    chanDistrib = [
        ['na3Modified', 'soma', 'Gbar', '30' ],
        #['kdr', 'soma', 'Gbar', '2000' ]
        ],
    stimList = [['soma', '1', '.', 'inject', '(t>0.1 && t<0.2) * 1e-8' ]],
    plotList = [['soma', '1', '.', 'Vm', 'Membrane potential']]
)

rdes.buildModel()
moose.reinit()
moose.start( 0.3 )
rdes.display()
#plt.savefig( '%s.png' % __file__ )
