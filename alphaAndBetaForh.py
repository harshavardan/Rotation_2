import matplotlib.pyplot as plt
import math

#Parameters taken from ./chans/naTraub1991.xml
mfr=1.28e2     #h gate, forward, rate
mfs=-0.018     #h gate, forward, scale
mfm=-4.3e-2    #h gate, forward, midpoint

mbr=4e3        #h gate, backward, rate
mbs=0.005      #h gate, backward, scale
mbm=-2e-2      #h gate, backward, midpoint

x=range(-100,100)
fr=[] #forward rate
for i in range(len(x)):
    value=(x[i]*1e-3-mfm)/mfs
    fr.append(mfr*math.e**value) #HHExpRate

br=[] #backward rate
for i in range(len(x)):
    value=(x[i]*1e-3-mbm)/mbs
    br.append(mbr/(1+math.e**-value)) #HHSigmoidRate

plt.figure( figsize=(12,6) )
plt.subplot(1,2,1)
alpha,=plt.plot(x,fr)
beta,=plt.plot(x,br)
plt.xlabel("V (mV)")
plt.legend([alpha,beta],["alpha","beta"])
plt.title("Alpha and beta for h gate of Na channel from Traub, 1991")


#Parameters taken from make_Na() in rdesignuerProtos.py

EREST_ACT=-0.060
AA=128.0
BA= 0.0
CA=0.0
DA= -1.0 * (0.017 + EREST_ACT)
FA=0.018

AB=4.0e3
BB=0.0
CB= 1.0
DB= -1.0 * (0.040 + EREST_ACT)
FB= -5.0e-3

frna=[] #alpha for make_Na()

for i in range(len(x)):
    frna.append((AA+BA*x[i]*1e-3)/(CA+math.e**((x[i]*1e-3+DA)/FA)))
    
brna=[]

for i in range(len(x)):
    brna.append((AB+BB*x[i]*1e-3)/(CB+math.e**((x[i]*1e-3+DB)/FB)))
    
plt.subplot(1,2,2)
alpha1,=plt.plot(x,frna)
beta1,=plt.plot(x,brna)
plt.legend([alpha1,beta1],["alpha","beta"])
plt.xlabel("V (mV)")
plt.title("Alpha and beta for h gate of make_Na()")
plt.tight_layout()
plt.show()

#plt.legend([alp])