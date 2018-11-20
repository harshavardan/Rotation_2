#Reproducing Traub 1991. I wrote an swc file with an apical dendrite and a basal dendrite with dimentions from the paper. The area of the cyclidrical soma from the paper was used to find the radius of a sphere with the same area. This area was used in the swc file. So far, only Na and K_DR channels have been added.
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
        ],
    chanDistrib = [
        ['Na', 'soma', 'Gbar', '30' ],
        ['K_DR', 'soma', 'Gbar', '15' ],
        ['Na', 'dend#', 'Gbar', '(p<=12) ? 15 : ((p>12 && p<=24) ? 0 : ((p>24 && p<=36) ? 20 : 0))'],
        ['K_DR', 'dend#', 'Gbar', '(p<=12) ? 15: ((p>12 && p<=24) ? 5 : ((p>24 && p<=36) ? 0 : (p>36 && p<=48) ? 48 : (p>48 && p<=60) ? 20 : 0))'],
        ['Na', 'apical#', 'Gbar', '(p<=12) ? 15 : ((p>12 && p<=24) ? 0 : (p>24 && p<=36) ? 20 : 0)'],
        ['K_DR', 'apical#', 'Gbar', '(p<=12)? 5 : (p>12 && p<=24) ? 0 : (p>24 && p<=36) ? 20 : 0)']
        ],
    stimList = [['soma', '1', '.', 'inject', '(t>0.1 && t<0.6) * 1e-10' ]],
    plotList = [['soma', '1', '.', 'Vm', 'Membrane potential']],
    #moogList = [['#', '1', '.', 'Vm', 'Soma potential']]
)

rdes.buildModel()
moose.reinit()
moose.start( .7 )
#rdes.displayMoogli( 0.001, 0.3, rotation = 0.02 )
rdes.display()