#I wrote an swc file with an apical dendrite and a basal dendrite
#with dimensions from the paper. The area of the cyclidrical soma
#from the paper was used to find the radius of a sphere with the 
#same area. This radius was used in the swc file.

import moose
import pylab
import rdesigneur as rd

rdes = rd.rdesigneur(
    cellProto = [
        ['./cells/traub1991.swc','elec'],
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
        ['Ca_conc', '#', 'tau', '0.020'],
        ['K_AHP', 'soma', 'Gbar', '8'],
        ['K_C', 'soma', 'Gbar', '100'],
        ['K_A', 'soma', 'Gbar', '50'],
        ['LeakConductance', '#', 'Gbar', "1" ],
        
        #apical dendrites
        
        ['Na', 'apical#', 'Gbar', '(p<=12) ? 150 : ((p>12 && p<=24) ? 0 : ((p>24 && p<=36) ? 200 : 0))'],
        ['K_DR', 'apical#', 'Gbar', '(p<=12) ? 50 : ((p>12 && p<=24) ? 0 : ((p>24 && p<=36) ? 200 : 0))'],
        ['Ca', 'apical#', 'Gbar', '(p<=12) ? 80 : ((p>12 && p<=24) ? 50 : ((p>24 && p<=60) ? 170 : ((p>60 && p<=84) ? 100 : ((p>84 && p<=108) ? 50 : 0))))'],
        ['K_AHP', 'apical#', 'Gbar', '(p<=108) ? 8 : 0'],
        ['K_C', 'apical#', 'Gbar', '(p<=12) ? 200 : ((p>12 && p<=24) ? 50 : ((p>24 && p<=84) ? 150 : ((p>84 && p<=108) ? 50 : 0)))'],
        
        #basal dendrites
        
        ['Na', 'dend#', 'Gbar', '(p<=12) ? 150 : ((p>12 && p<=24) ? 0 : ((p>24 && p<=36) ? 200 : 0))'],
        ['K_DR', 'dend#', 'Gbar', '(p<=12) ? 50 : ((p>12 && p<=24) ? 0 : ((p>24 && p<=36) ? 200 : 0))'],
        ['Ca', 'dend#', 'Gbar', '(p<=12) ? 80 : ((p>12 && p<=24) ? 50 : ((p>24 && p<=60) ? 120 : ((p>60 && p<=84) ? 50 : 0)))'],
        ['K_AHP', 'dend#', 'Gbar', '(p<=84) ? 8 : 0'],
        ['K_C', 'dend#','Gbar','(p<=12) ? 200 : ((p>12 && p<=24) ? 50 : ((p>24 && p<=60) ? 100 : ((p>60 && p<=84) ? 50 : 0)))']
        ],
        
    stimList = [['soma', '1', '.', 'inject', '(t>0.1 && t<0.2) ? 1e-10 :0' ]],
    plotList = [
        ['soma', '1', '.', 'Vm', 'Membrane potential'],
        ],
    #moogList = [['#', '1', '.', 'Vm', 'Soma potential']]
)

rdes.buildModel()
moose.reinit()
moose.start( 0.3 )
#rdes.displayMoogli( 0.001, 0.7, rotation = 0.02 )
rdes.display()
