#I wrote an swc file with an apical dendrite and a basal dendrite
#with dimensions from the paper. The area of the cyclidrical soma
#from the paper was used to find the radius of a sphere with the 
#same area. This area was used in the swc file.

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
        ['make_K_A()', 'K_A']
        ],
    passiveDistrib = [
        ['#', 'CM', '0.030', 'RM', '1.0', 'RA', '1.0' ]
        ],
    chanDistrib = [
        ['Na', 'soma', 'Gbar', '30' ],
        ['K_DR', 'soma', 'Gbar', '15' ],
        ['Ca', 'soma', 'Gbar', '4'],
        ['Ca_conc', '#', 'tau', '0.020'],
        ['K_AHP', 'soma', 'Gbar', '0.8'],
        ['K_C', 'soma', 'Gbar', '10'],
        ['K_A', 'soma', 'Gbar', '5'],
        
        #apical dendrites
        
        ['Na', 'apical#', 'Gbar', '(p<=12) ? 15 : ((p>12 && p<=24) ? 0 : ((p>24 && p<=36) ? 20 : 0))'],
        ['K_DR', 'apical#', 'Gbar', '(p<=12) ? 5 : ((p>12 && p<=24) ? 0 : ((p>24 && p<=36) ? 20 : 0))'],
        ['Ca', 'apical#', 'Gbar', '(p<=12) ? 8 : ((p>12 && p<=24) ? 5 : ((p>24 && p<=60) ? 17 : ((p>60 && p<=84) ? 10 : ((p>84 && p<=108) ? 5 : 0))))'],
        ['K_AHP', 'apical#', 'Gbar', '(p<=108) ? 0.8 : 0'],
        ['K_C', 'apical#', 'Gbar', '(p<=12) ? 20 : ((p>12 && p<=24) ? 5 : ((p>24 && p<=84) ? 15 : ((p>84 && p<=108) ? 5 : 0)))'],
        
        #basal dendrites
        
        ['Na', 'dend#', 'Gbar', '(p<=12) ? 15 : ((p>12 && p<=24) ? 0 : ((p>24 && p<=36) ? 20 : 0))'],
        ['K_DR', 'dend#', 'Gbar', '(p<=12) ? 5 : ((p>12 && p<=24) ? 0 : ((p>24 && p<=36) ? 20 : 0))'],
        ['Ca', 'dend#', 'Gbar', '(p<=12) ? 8 : ((p>12 && p<=24) ? 5 : ((p>24 && p<=60) ? 12 : ((p>60 && p<=84) ? 5 : 0)))'],
        ['K_AHP', 'dend#', 'Gbar', '(p<=84) ? 0.8 : 0'],
        ['K_C', 'dend#','Gbar','(p<=12) ? 20 : ((p>12 && p<=24) ? 5 : ((p>24 && p<=60) ? 10 : ((p>60 && p<=84) ? 5 : 0)))']
        ],
        
    stimList = [['soma', '1', '.', 'inject', '(t>0.1 && t<1.1) * 0.12e-9' ]],
    plotList = [
        ['soma', '1', '.', 'Vm', 'Membrane potential'],
        ],
    #moogList = [['#', '1', '.', 'Vm', 'Soma potential']]
)

rdes.buildModel()
moose.reinit()
moose.start( 5 )
#rdes.displayMoogli( 0.001, 0.7, rotation = 0.02 )
rdes.display()



#'(p<=12) ?  : ((p>12 && p<=24) ?  : ((p>24 && p<=36) ?  : ((p>36 && p<=48) ?  : ((p>48 && p<=60) ?  : ((p>60 && p<=72) ?  : ((p>72 && p<=84) ?  : ((p>84 && p<=96) ?  : (p>96 && p<=108) ?  : )))))))'