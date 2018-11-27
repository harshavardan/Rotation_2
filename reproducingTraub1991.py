#I wrote an swc file with an apical dendrite and a basal dendrite
#with dimensions from the paper. The area of the cyclidrical soma
#from the paper was used to find the radius of a sphere with the 
#same area. This radius was used in the swc file.

import moose
import math
import matplotlib.pyplot as plt
import rdesigneur as rd
import networkx as nx

#Dilawar's code

def print_model( ):
    print( ' STIMULUS' )
    res = {}
    for s in moose.wildcardFind( '/model/stims/##' ):
        if isinstance(s, moose.Function):
            print( "%s | %s" % (s.path, s.expr) )

    for c in moose.wildcardFind( '/model/elec/##[TYPE=ZombieHHChannel]' ):
        e = moose.element(c)
        x = c.path.split( '/')
        compt = moose.element(e.parent)
        vol = math.pi * compt.diameter * compt.length 
        print( "Gbar=%g S, %g S/m^2| %s" % (e.Gbar, e.Gbar/vol, '/'.join(x[-2:])))

    for c in moose.wildcardFind( '/model/##[TYPE=ZombieCaConc]' ):
        e = moose.element(c)
        x = c.path.split( '/')
        print( "Tau=%g | %s" % (e.tau, '/'.join(x[-2:])))

    # print compartments.
    g = nx.DiGraph()
    for c in moose.wildcardFind( '/model/##[TYPE=ZombieCompartment]'):
        g.add_node( c.name )
        for x in c.neighbors['axial']:
            print( "%s -> %s" % (c.name, x.name ))
            g.add_edge( c.name, x.name )

    nx.draw_spring( g, with_labels = True )
    plt.show()
    quit()

#My code

rdes = rd.rdesigneur(
    cellProto = [
        ['./cells/traubCompartments.swc','elec'],
        #['ballAndStick','soma', 8.46e-6, 125e-6, 5.78e-6, 120e-6, 10]#[ballAndStick,name, somaDia=10e-6, somaLen=10e-6, dendDia=4e-6, dendLen=200e-6, numDendSeg=1] 
        ],
    chanProto = [
        ['make_Na()', 'Na'],
        ['make_K_DR()', 'K_DR'],
        ['make_Ca()', 'Ca'],
        ['make_Ca_conc()', 'Ca_conc' ],
        ['make_K_AHP()', 'K_AHP'],
        ['make_K_C()', 'K_C'],
        ['make_K_A()', 'K_A'],
        ['./chans/LeakConductance.xml']
        ],
    passiveDistrib = [
        ['#', 'CM', '0.030', 'RM', '1.0', 'RA', '1.0' ] # look into this
        ],
    chanDistrib = [
        ['Na', 'soma', 'Gbar', '300' ], # conductance units are S/m^2
        ['K_DR', 'soma', 'Gbar', '150' ],
        ['Ca', 'soma', 'Gbar', '40'],
        ['Ca_conc', '#', 'tau', '0.01333'],
        ['K_AHP', 'soma', 'Gbar', '8'],
        ['K_C', 'soma', 'Gbar', '100'],
        ['K_A', 'soma', 'Gbar', '50'],
        ['LeakConductance', '#', 'Gbar', "1.0" ],
        
        #apical dendrites
        ['Na', 'apical#', 'Gbar', '(p<=12e-6) ? 150 : ((p>12e-6 && p<=24e-6) ? 0 : ((p>24e-6 && p<=36e-6) ? 200 : 0))'],
        ['K_DR', 'apical#', 'Gbar', '(p<=12e-6) ? 50 : ((p>12e-6 && p<=24e-6) ? 0 : ((p>24e-6 && p<=36e-6) ? 200 : 0))'],
        ['Ca', 'apical#', 'Gbar', '(p<=12e-6) ? 80 : ((p>12e-6 && p<=24e-6) ? 50 : ((p>24e-6 && p<=60e-6) ? 170 : ((p>60e-6 && p<=84e-6) ? 100 : ((p>84e-6 && p<=108e-6) ? 50 : 0))))'],
        ['K_AHP', 'apical#', 'Gbar', '(p<=108e-6) ? 8 : 0'],
        ['K_C', 'apical#', 'Gbar', '(p<=12e-6) ? 200 : ((p>12e-6 && p<=24e-6) ? 50 : ((p>24e-6 && p<=84e-6) ? 150 : ((p>84e-6 && p<=108e-6) ? 50 : 0)))'],
        
        #basal dendrites
        ['Na', 'dend#', 'Gbar', '(p<=12e-6) ? 150 : ((p>12e-6 && p<=24e-6) ? 0 : ((p>24e-6 && p<=36e-6) ? 200 : 0))'],
        ['K_DR', 'dend#', 'Gbar', '(p<=12e-6) ? 50 : ((p>12e-6 && p<=24e-6) ? 0 : ((p>24e-6 && p<=36e-6) ? 200 : 0))'],
        ['Ca', 'dend#', 'Gbar', '(p<=12e-6) ? 80 : ((p>12e-6 && p<=24e-6) ? 50 : ((p>24e-6 && p<=60e-6) ? 120 : ((p>60e-6 && p<=84e-6) ? 50 : 0)))'],
        ['K_AHP', 'dend#', 'Gbar', '(p<=84e-6) ? 8 : 0'],
        ['K_C', 'dend#','Gbar','(p<=12e-6) ? 200 : ((p>12e-6 && p<=24e-6) ? 50 : ((p>24e-6 && p<=60e-6) ? 100 : ((p>60e-6 && p<=84e-6) ? 50 : 0)))']
        ],
        
    stimList = [['soma', '1', '.', 'inject', '(t>0.2 && t<0.8) ? 0 :0' ]],
    plotList = [
        ['soma', '1', '.', 'Vm', 'Membrane potential'],
        ['#', '1','Ca_conc','Ca', 'Calcium concentration (soma)']        
        ],
    #moogList = [['#', '1', '.', 'Vm', 'Soma potential']]
)

rdes.buildModel()
moose.reinit()
print_model()
moose.start( 10 )
#rdes.displayMoogli( 0.001, 0.7, rotation = 0.02 )
rdes.display()
#tables = moose.wildcardFind( '/##[TYPE=Table]' )
#for i, t in enumerate(tables):
    #plt.subplot( 4, 1, i+1)
    #plt.plot( t.vector, '.' )

#plt.show()


#INFO:matplotlib.backends._backend_tk:Could not load matplotlib icon: can't use "pyimage10" as iconphoto: not a photo image


