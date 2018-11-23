#Traub 1991 uses varying thickness of the calcium shell (a shell in each membrane, in which the calcium is present) to see if I could begin to get what the paper got. 

import moose
import math
import matplotlib.pyplot as plt
import rdesigneur as rd

rdes = rd.rdesigneur(
    cellProto = [
        ['./cells/dummy.swc','elec'],
        ],
    chanProto = [
        ['make_Na()', 'Na'],
        ['make_K_DR()', 'K_DR'],
        ['make_Ca()', 'Ca'],
        ['make_Ca_conc()', 'Ca_conc' ],
        ],

    chanDistrib = [
        ['Na', 'soma', 'Gbar', '150' ], # conductance units are S/m^2
        ['K_DR', 'soma', 'Gbar', '150' ],
        ['Ca', 'soma', 'Gbar', '40'],
        ['Ca_conc', 'soma', 'tau', '0.01333', 'thick', '1'],
        ['Ca_conc', 'apical#', 'tau', '0.01333', 'thick', '10'],
        ['Ca_conc', 'dend#', 'tau', '0.01333', 'thick', '100'],
        
        #apical dendrites
        
        ['Na', 'dend_e_1_0', 'Gbar', '(p<=12) ? 150 : ((p>12 && p<=24) ? 0 : ((p>24 && p<=36) ? 200 : 0))'],
        ['K_DR', 'dend_e_1_0', 'Gbar', '(p<=12) ? 50 : ((p>12 && p<=24) ? 0 : ((p>24 && p<=36) ? 200 : 0))'],
        ['Ca', 'dend_e_1_0', 'Gbar', '(p<=12) ? 80 : ((p>12 && p<=24) ? 50 : ((p>24 && p<=60) ? 170 : ((p>60 && p<=84) ? 100 : ((p>84 && p<=108) ? 50 : 0))))'],
        
        #basal dendrites
       
        ['Na', 'dend_e_2_0', 'Gbar', '(p<=12) ? 150 : ((p>12 && p<=24) ? 0 : ((p>24 && p<=36) ? 200 : 0))'],
        ['K_DR', 'dend_e_2_0', 'Gbar', '(p<=12) ? 50 : ((p>12 && p<=24) ? 0 : ((p>24 && p<=36) ? 200 : 0))'],
        ['Ca', 'dend_e_2_0', 'Gbar', '(p<=12) ? 80 : ((p>12 && p<=24) ? 50 : ((p>24 && p<=60) ? 170 : ((p>60 && p<=84) ? 100 : ((p>84 && p<=108) ? 50 : 0))))'],
        ],
        
    stimList = [['soma', '1', '.', 'inject', '(t>0.2 && t<0.8) ? 0 :0' ]],
    plotList = [
        ['soma', '1', '.', 'Vm', 'Membrane potential'],
        ['#', '1','Ca_conc','Ca', 'Calcium concentration']        
        ],
)

rdes.buildModel()
moose.reinit()
moose.start( 1 )
rdes.display()