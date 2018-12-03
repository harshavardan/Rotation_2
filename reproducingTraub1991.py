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
    
    #print( ' STIMULUS' )
    #res = {}
    #for s in moose.wildcardFind( '/model/stims/##' ):
        #if isinstance(s, moose.Function):
            #print( "%s | %s" % (s.path, s.expr) )

    #for c in moose.wildcardFind( '/model/elec/##[TYPE=ZombieHHChannel]' ):
        #e = moose.element(c)
        #x = c.path.split( '/')
        #compt = moose.element(e.parent)
        #vol = math.pi * compt.diameter * compt.length 
        #print( "%g S/m^2| %s" % (e.Gbar/vol, '/'.join(x[-2:])))

    #for c in moose.wildcardFind( '/model/##[TYPE=ZombieCaConc]' ):
        #e = moose.element(c)
        #x = c.path.split( '/')
        #print( "Tau=%g | %s" % (e.tau, '/'.join(x[-2:])))

    ## print compartments.
    #g = nx.DiGraph()
    #for c in moose.wildcardFind( '/model/##[TYPE=ZombieCompartment]'):
        #g.add_node( c.name )
        #for x in c.neighbors['axial']:
            #print( "%s -> %s" % (c.name, x.name ))
            #g.add_edge( c.name, x.name )

    #nx.draw_spring( g, with_labels = True )
    #plt.show()
    
    #My code
    
    #print B values
    #for c in moose.wildcardFind( '/model/elec/##[TYPE=ZombieCaConc]' ):
        #e=moose.element(c)
        #x=c.path.split('/')
        #print('B=%g %s' % (e.B, '/'.join(x[-2:])))
    
    #print passive properties
    for c in moose.wildcardFind( '/model/elec/##[TYPE=ZombieCompartment]' ):
        e=moose.element(c)
        x=c.path.split('/')
        area=math.pi*e.diameter*e.length
        
        CM=e.Cm/area
        print('CM=%g F/m^2 %s' % (CM, '/'.join(x[-2:])))
        
        RM=e.Rm*area
        print('RM=%g Ohm.m^2 %s' % (RM, '/'.join(x[-2:])))
        
        RA=e.Ra*area/e.length #Not being set correctly.
        print('RA=%g Ohm.m %s' % (RA, '/'.join(x[-2:])))
    
    ##quit()

def findRadius(R,v,l):
    if R<math.sqrt(v/(math.pi*l)):
        print("Invalid values passed!")
        return
    else:
        rad=(2*R-math.sqrt(4*R**2-4*v/(math.pi*l)))/2
        return(str(rad))

def findV(B):
    return(1.0/(B*96485.3415))

#vol=1e-16
tau='0.01333'

rdes = rd.rdesigneur(
    cellProto = [
        ['./cells/traubCompartments.swc','elec'],
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
        ['Ca_conc', 'soma', 'tau', tau, 'thick', findRadius(16.25e-6,findV(34.804e12),16.25e-6)], #Compartment number 9
        ['Ca', 'soma', 'Gbar', '40'],
        ['K_AHP', 'soma', 'Gbar', '8'],
        ['K_C', 'soma', 'Gbar', '100'],
        ['K_A', 'soma', 'Gbar', '50'],
        ['LeakConductance', '#', 'Gbar', "1.0" ],
        
        #apical dendrites
        ['Na', 'apical#', 'Gbar', '(p<=12e-6) ? 150 : ((p>12e-6 && p<=24e-6) ? 0 : ((p>24e-6 && p<=36e-6) ? 200 : 0))'],
        ['K_DR', 'apical#', 'Gbar', '(p<=12e-6) ? 50 : ((p>12e-6 && p<=24e-6) ? 0 : ((p>24e-6 && p<=36e-6) ? 200 : 0))'],
        ['Ca_conc', 'apical_1_0', 'tau', tau, 'thick', findRadius(2.89e-6, findV(26.404e12), 12e-6)],#10
        ['Ca_conc', 'apical_1_1', 'tau', tau, 'thick', findRadius(2.89e-6, findV(5.941e12), 12e-6)],#11
        ['Ca_conc', 'apical_1_2', 'tau', tau, 'thick', findRadius(2.89e-6, findV(5.941e12), 12e-6)],#12
        ['Ca_conc', 'apical_1_3', 'tau', tau, 'thick', findRadius(2.89e-6, findV(5.941e12), 12e-6)],#13
        ['Ca_conc', 'apical_1_4', 'tau', tau, 'thick', findRadius(2.89e-6, findV(5.941e12), 12e-6)],#14
        ['Ca_conc', 'apical_1_5', 'tau', tau, 'thick', findRadius(2.89e-6, findV(5.941e12), 12e-6)],#15
        ['Ca_conc', 'apical_1_6', 'tau', tau, 'thick', findRadius(2.89e-6, findV(5.941e12), 12e-6)],#16
        ['Ca_conc', 'apical_1_7', 'tau', tau, 'thick', findRadius(2.89e-6, findV(5.941e12), 12e-6)],#17
        ['Ca_conc', 'apical_1_8', 'tau', tau, 'thick', findRadius(2.89e-6, findV(5.941e12), 12e-6)],#18
        ['Ca_conc', 'apical_e_1_9', 'tau', tau, 'thick', findRadius(2.89e-6, findV(5.941e12), 12e-6)],#19
        ['Ca', 'apical#', 'Gbar', '(p<=12e-6) ? 80 : ((p>12e-6 && p<=24e-6) ? 50 : ((p>24e-6 && p<=60e-6) ? 170 : ((p>60e-6 && p<=84e-6) ? 100 : ((p>84e-6 && p<=108e-6) ? 50 : 0))))'],
        ['K_AHP', 'apical#', 'Gbar', '(p<=108e-6) ? 8 : 0'],
        ['K_C', 'apical#', 'Gbar', '(p<=12e-6) ? 200 : ((p>12e-6 && p<=24e-6) ? 50 : ((p>24e-6 && p<=84e-6) ? 150 : ((p>84e-6 && p<=108e-6) ? 50 : 0)))'],
        
        #basal dendrites
        ['Na', 'dend#', 'Gbar', '(p<=13.75e-6) ? 150 : ((p>13.75e-6 && p<=27.5e-6) ? 0 : ((p>27.5e-6 && p<=41.25e-6) ? 200 : 0))'],
        ['K_DR', 'dend#', 'Gbar', '(p<=13.75e-6) ? 50 : ((p>13.75e-6 && p<=27.5e-6) ? 0 : ((p>27.5e-6 && p<=41.25e-6) ? 200 : 0))'],
        ['Ca_conc', 'dend_2_0', 'tau', tau, 'thick', findRadius(2.42e-6, findV(34.530e12), 13.75e-6)],#8
        ['Ca_conc', 'dend_2_1', 'tau', tau, 'thick', findRadius(2.42e-6, findV(7.769e12), 13.75e-6)],#7
        ['Ca_conc', 'dend_2_2', 'tau', tau, 'thick', findRadius(2.42e-6, findV(7.769e12), 13.75e-6)],#6
        ['Ca_conc', 'dend_2_3', 'tau', tau, 'thick', findRadius(2.42e-6, findV(7.769e12), 13.75e-6)],#5
        ['Ca_conc', 'dend_2_4', 'tau', tau, 'thick', findRadius(2.42e-6, findV(7.769e12), 13.75e-6)],#4
        ['Ca_conc', 'dend_2_5', 'tau', tau, 'thick', findRadius(2.42e-6, findV(7.769e12), 13.75e-6)],#3
        ['Ca_conc', 'dend_2_6', 'tau', tau, 'thick', findRadius(2.42e-6, findV(7.769e12), 13.75e-6)],#2
        ['Ca_conc', 'dend_e_2_7', 'tau', tau, 'thick', findRadius(2.42e-6, findV(7.769e12), 13.75e-6)],#1
        ['Ca', 'dend#', 'Gbar', '(p<=13.75e-6) ? 80 : ((p>13.75e-6 && p<=27.5e-6) ? 50 : ((p>27.5e-6 && p<=68.75e-6) ? 120 : ((p>68.75e-6 && p<=96.25e-6) ? 50 : 0)))'],
        ['K_AHP', 'dend#', 'Gbar', '(p<=96.25e-6) ? 8 : 0'],
        ['K_C', 'dend#','Gbar','(p<=13.75e-6) ? 200 : ((p>13.75e-6 && p<=27.5e-6) ? 50 : ((p>27.5e-6 && p<=68.75e-6) ? 100 : ((p>68.75e-6 && p<=96.25e-6) ? 50 : 0)))']
        ],
        
    #stimList = [['soma', '1', '.', 'inject', '(t>4 && t<9) ? 0.01e-9 :0' ]],
    plotList = [
        ['#', '1', '.', 'Vm', 'Membrane potential'],
        ['#', '1','Ca_conc','Ca', 'Calcium concentration']        
        ],
    #moogList = [['#', '1', '.', 'Vm', 'Soma potential']]
)

rdes.buildModel()
moose.reinit()
print_model()
moose.start( 10 )
#rdes.displayMoogli( 0.001, 1, rotation = 0.02 )
#rdes.display()
#findRadius(1,1,1)
#tables = moose.wildcardFind( '/##[TYPE=Table]' )
#for i, t in enumerate(tables):
    #plt.subplot( 4, 1, i+1)
    #plt.plot( t.vector, '.' )

#plt.show()

#INFO:matplotlib.backends._backend_tk:Could not load matplotlib icon: can't use "pyimage10" as iconphoto: not a photo image