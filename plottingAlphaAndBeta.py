import matplotlib.pyplot as plt
import math

#Parameters taken from ./chans/naTraub1991.xml
mfr=1.28e3     #m gate, forward, rate
mfs=0.004      #m gate, forward, scale
mfm=-4.69e-2   #m gate, forward, midpoint

mbr=1.4e3      #m gate, backward, rate
mbs=-0.005     #m gate, backward, scale
mbm=-1.99e-2   #m gate, backward, midpoint

x=range(-100,100)
fr=[] #forward rate
for i in range(len(x)):
    value=(x[i]*1e-3-mfm)/mfs
    fr.append(value*mfr/(1-math.e**-value)) #HHExpLinearRate

br=[] #backwad rate
for i in range(len(x)):
    value=(x[i]*1e-3-mbm)/mbs
    br.append(value*mbr/(1-math.e**-value)) #HHExpLinearRate

alpha,=plt.plot(x,fr)
beta,=plt.plot(x,br)
plt.xlabel("V (mV)")
plt.legend([alpha,beta],["alpha","beta"])
plt.title("Alpha and beta for m gate of Na channel from Traub, 1991")
plt.show()

#Parameters taken from make_Na() in rdesignuerProtos.py

EREST_ACT=0.060
AA=320e3*(0.0131 + EREST_ACT)
BA=-320e3
CA=-1.0
DA=-1.0*(0.0131 + EREST_ACT)
FA=-4.0e-3

AB=-280e3 * (0.0401 + EREST_ACT)
BB=280e3
CB=-1.0
DB=-1.0 * (0.0401 + EREST_ACT)
FB= 5.0e-3

frna=[] #alpha for make_Na()

for i in range(len(x)):
    frna.append((AA+BA*x[i]*1e-3)/(CA+math.e**((x[i]*1e-3+DA)/FA)))
    
brna=[]

for i in range(len(x)):
    brna.append((AB+BB*x[i]*1e-3)/(CB+math.e**((x[i]*1e-3+DB)/FB)))
    
alpha,=plt.plot(x,frna)
beta,=plt.plot(x,brna)
plt.legend([alpha,beta],["alpha","beta"])
plt.xlabel("V (mV)")
plt.title("Alpha and beta for m gate of make_Na()")
plt.show()