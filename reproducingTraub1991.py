#I wrote an swc file with an apical dendrite and a basal dendrite
#with dimensions from the paper. The area of the cyclidrical soma
#from the paper was used to find the radius of a sphere with the 
#same area. This radius was used in the swc file.

import moose
import math
import matplotlib.pyplot as plt
import rdesigneur as rd

##Dilawar's code

#def print_model( ):
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
        #print( "Gbar=%g S, %g S/m^2| %s" % (e.Gbar, e.Gbar/vol, '/'.join(x[-2:])))

    #for c in moose.wildcardFind( '/model/##[TYPE=ZombieCaConc]' ):
        #e = moose.element(c)
        #x = c.path.split( '/')
        #print( "Tau=%g | %s" % (e.tau, '/'.join(x[-2:])))

#My code

x=1#2.42e-6/4.44

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
        ['Ca_conc', 'soma', 'tau', '0.01333', 'B', '17.402e12'],
        ['Ca_conc', 'apical_f_1_0', 'tau', '0.01333', 'B', '26.404e12' ],
        ['Ca_conc', 'apical_f_2_0', 'tau', '0.01333', 'B', '5.941e12' ],
        ['Ca_conc', 'apical_f_3_0', 'tau', '0.01333', 'B', '5.941e12' ],
        ['Ca_conc', 'apical_f_4_0', 'tau', '0.01333', 'B', '5.941e12' ],
        ['Ca_conc', 'apical_f_5_0', 'tau', '0.01333', 'B', '5.941e12' ],
        ['Ca_conc', 'apical_f_6_0', 'tau', '0.01333', 'B', '5.941e12' ],
        ['Ca_conc', 'apical_f_7_0', 'tau', '0.01333', 'B', '5.941e12' ],
        ['Ca_conc', 'apical_8_0', 'tau', '0.01333', 'B', '5.941e12' ],
        ['Ca_conc', 'apical_8_1', 'tau', '0.01333', 'B', '5.941e12' ],
        ['Ca_conc', 'apical_e_8_2', 'tau', '0.01333', 'B', '5.941e12' ],
        ['Ca_conc', 'dend_e_9_0', 'tau', '0.01333', 'B', '34.530e12'],
        ['Ca_conc', 'dend_e_10_0', 'tau', '0.01333', 'B', '7.769e12'],
        ['Ca_conc', 'dend_e_11_0', 'tau', '0.01333', 'B', '7.769e12'],
        ['Ca_conc', 'dend_e_12_0', 'tau', '0.01333', 'B', '7.769e12'],
        ['Ca_conc', 'dend_e_13_0', 'tau', '0.01333', 'B', '7.769e12'],
        ['Ca_conc', 'dend_e_14_0', 'tau', '0.01333', 'B', '7.769e12'],
        ['Ca_conc', 'dend_e_15_0', 'tau', '0.01333', 'B', '7.769e12'],
        ['Ca_conc', 'dend_e_16_0', 'tau', '0.01333', 'B', '7.769e12'],
        ['Ca', 'soma', 'Gbar', '40'],
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
        ['Na', 'dend#', 'Gbar', '(p<=13.75e-6) ? 150 : ((p>13.75e-6 && p<=27.5e-6) ? 0 : ((p>27.5e-6 && p<=41.25e-6) ? 200 : 0))'],
        ['K_DR', 'dend#', 'Gbar', '(p<=13.75e-6) ? 50 : ((p>13.75e-6 && p<=27.5e-6) ? 0 : ((p>27.5e-6 && p<=41.25e-6) ? 200 : 0))'],
        ['Ca', 'dend#', 'Gbar', '(p<=13.75e-6) ? 80 : ((p>13.75e-6 && p<=27.5e-6) ? 50 : ((p>27.5e-6 && p<=68.75e-6) ? 120 : ((p>68.75e-6 && p<=86.25e-6) ? 50 : 0)))'],
        ['K_AHP', 'dend#', 'Gbar', '(p<=96.25e-6) ? 8 : 0'],
        ['K_C', 'dend#','Gbar','(p<=13.75e-6) ? 200 : ((p>13.75e-6 && p<=27.5e-6) ? 50 : ((p>27.5e-6 && p<=68.75e-6) ? 100 : ((p>68.75e-6 && p<=96.25e-6) ? 50 : 0)))']
        ],
        
    stimList = [['soma', '1', '.', 'inject', '(t>10 && t<=25) ? 0.1e-9 : 0' ]],
    plotList = [
        ['soma', '1', '.', 'Vm', 'Membrane potential'],
        ['soma', '1','Ca_conc','Ca', 'Calcium concentration (soma)']        
        ],
    #moogList = [['#', '1', '.', 'Vm', 'Soma potential']]
)

rdes.buildModel()
#  print_model()
moose.reinit()
moose.start( 30 )
#rdes.displayMoogli( 0.001, 0.7, rotation = 0.02 )
rdes.display()
#tables = moose.wildcardFind( '/##[TYPE=Table]' )
#for i, t in enumerate(tables):
    #plt.subplot( 4, 1, i+1)
    #plt.plot( t.vector, '.' )

#plt.show()

#INFO:matplotlib.backends._backend_tk:Could not load matplotlib icon: can't use "pyimage10" as iconphoto: not a photo image