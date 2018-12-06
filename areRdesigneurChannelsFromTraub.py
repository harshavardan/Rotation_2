import math
import matplotlib.pyplot as plt


x=range(-100,100)
#x1=range(-40,160) #taking into the relative voltages used in the paper
#EREST_ACT=-0.060

####Activation variable for Na 

###From paper

##fr=[]
##br=[]
##for i in range(len(x)):
    ##fr.append(1e3*0.32*(13.1-x1[i])/(math.e**((13.1-x1[i])/4.0)-1.0))
    ##br.append(1e3*0.28*(-40.1+x1[i])/(math.e**((-40.1+x1[i])/5.0)-1.0))
    
##plt.figure( figsize=(10,5) )
##plt.subplot(1,2,1)
##alpha,=plt.plot(x,fr)
##beta,=plt.plot(x,br)
##plt.xlabel("V(mV)")
##plt.legend([alpha,beta],["alpha","beta"])
##plt.title("Activation gate, Na channel, Traub 1991")

###From rdesigneurProtos

##AA=320e3*(0.0131 + EREST_ACT)
##BA=-320e3
##CA=-1.0
##DA=-1.0*(0.0131 + EREST_ACT)
##FA=-4.0e-3

##AB=-280e3 * (0.0401 + EREST_ACT)
##BB=280e3
##CB=-1.0
##DB=-1.0 * (0.0401 + EREST_ACT)
##FB= 5.0e-3

##frrd=[] #Uses parameters from rdesigneurProtos.py
##brrd=[] #Uses parameters from rdesigneurProtos.py
##for i in range(len(x)):
    ##frrd.append((AA+BA*x[i]*1e-3)/(CA+math.e**((x[i]*1e-3+DA)/FA)))
    ##brrd.append((AB+BB*x[i]*1e-3)/(CB+math.e**((x[i]*1e-3+DB)/FB)))

##plt.subplot(1,2,2)
##alpha1,=plt.plot(x,frrd)
##beta1,=plt.plot(x, brrd)
##plt.legend([alpha1,beta1],["alpha","beta"])
##plt.xlabel("V (mV)")
##plt.title("Activation gate, make_Na()")
##plt.show()

###Activation variable for Ca

##From paper

#fr=[]
#br=[]
#for i in range(len(x)):
    #fr.append(1e3*1.6/(1+math.e**(-0.072*(x1[i]-65.0))))
    #br.append(1e3*0.02*(x1[i]-51.1)/(math.e**((x1[i]-51.1)/5.0)-1.0))

#plt.figure( figsize=(10,5) )
#plt.subplot(1,2,1)
#alpha,=plt.plot(x,fr)
#beta,=plt.plot(x,br)
#plt.xlabel("V(mV)")
#plt.legend([alpha,beta],["alpha","beta"])
#plt.title("Activation gate, Ca channel, Traub 1991")
    
##From rdesigneurProtos
#AA=1.6e3
#BA=0.0
#CA=1.0
#DA=-1.0 * (0.065 + EREST_ACT)
#FA=-0.01389

#AB=-20e3 * (0.0511 + EREST_ACT)
#BB=20e3
#CB=-1.0
#DB=-1.0 * (0.0511 + EREST_ACT)
#FB= 5.0e-3

#frrd=[] #Uses parameters from rdesigneurProtos.py
#brrd=[] #Uses parameters from rdesigneurProtos.py
#for i in range(len(x)):
    #frrd.append((AA+BA*x[i]*1e-3)/(CA+math.e**((x[i]*1e-3+DA)/FA)))
    #brrd.append((AB+BB*x[i]*1e-3)/(CB+math.e**((x[i]*1e-3+DB)/FB)))
    
#plt.subplot(1,2,2)
#alpha1,=plt.plot(x,frrd)
#beta1,=plt.plot(x, brrd)
#plt.legend([alpha1,beta1],["alpha","beta"])
#plt.xlabel("V (mV)")
#plt.title("Activation gate, make_Ca()")
#plt.show()

##inf and tau calculations
#inf=[]
#tau=[]
#for i in range(len(x)):
    #inf.append(frrd[i]/(frrd[i]+brrd[i]))
    #tau.append(1.0/(frrd[i]+brrd[i]))
    
#plt.plot(x,inf)
#plt.show()

#plt.plot(x,tau)
#plt.show()

####Activation variable for KDR

###From paper

##fr=[]
##br=[]
##for i in range(len(x)):
    ##fr.append(1e3*0.016*(35.1-x1[i])/(math.e**((35.1-x1[i])/5.0)-1.0))
    ##br.append(1e3*0.25*math.e**((20.0-x1[i])/40.0))
    
##plt.figure( figsize=(10,5) )
##plt.subplot(1,2,1)
##alpha,=plt.plot(x,fr)
##beta,=plt.plot(x,br)
##plt.xlabel("V(mV)")
##plt.legend([alpha,beta],["alpha","beta"])
##plt.title("Activation gate, K_DR, Traub 1991")
    
###From rdesigneurProtos

##AA=16e3*(0.0351 + EREST_ACT)
##BA=-16e3
##CA=-1.0
##DA=-1.0 * (0.0351 + EREST_ACT)
##FA=-0.005

##AB=250
##BB=0.0
##CB=0.0
##DB=-1.0 * (0.02 + EREST_ACT)
##FB= 0.04

###[ 16e3 * (0.0351 + EREST_ACT), -16e3, -1.0, -1.0 * (0.0351 + EREST_ACT),
###-0.005, 250, 0.0, 0.0, -1.0 * (0.02 + EREST_ACT), 0.04, 3000, -0.1, 0.05 ]

##frrd=[] #Uses parameters from rdesigneurProtos.py
##brrd=[] #Uses parameters from rdesigneurProtos.py
##for i in range(len(x)):
    ##frrd.append((AA+BA*x[i]*1e-3)/(CA+math.e**((x[i]*1e-3+DA)/FA)))
    ##brrd.append((AB+BB*x[i]*1e-3)/(CB+math.e**((x[i]*1e-3+DB)/FB)))
    
##plt.subplot(1,2,2)
##alpha1,=plt.plot(x,frrd)
##beta1,=plt.plot(x, brrd)
##plt.legend([alpha1,beta1],["alpha","beta"])
##plt.xlabel("V (mV)")
##plt.title("Activation gate, make_K_DR()")
##plt.show()


####Activation variable for KC

###From paper

##fr=[]
##br=[]
##for i in range(len(x)):
    ##if x1[i]<=50:
        ##fr.append(1e3*math.e**((x1[i]-10.0)/11.0-(x1[i]-6.5)/27.0)/18.975)
        ##br.append((1e3*2*math.e**((6.5-x1[i])/27.0)) - 1e3*math.e**((x1[i]-10.0)/11.0-(x1[i]-6.5)/27.0)/18.975)
        
    ##else:
        ##fr.append(1e3*2*math.e**((6.5-x1[i])/27.0))
        ##br.append(0)
        
##plt.figure( figsize=(10,5) )
##plt.subplot(1,2,1)
##alpha,=plt.plot(x,fr)
##beta,=plt.plot(x,br)
##plt.xlabel("V(mV)")
##plt.legend([alpha,beta],["alpha","beta"])
##plt.title("Activation gate, K_C, Traub 1991")
        
###From rdesigneurProtos

##frrd=[]
##brrd=[]

##for i in range(len(x)):
    ##a=0.0
    ##b=0.0
    ##if (x[i]*1e-3 < EREST_ACT + 0.05):
        ##a= math.exp( 53.872 * (x[i]*1e-3  - EREST_ACT) - 0.66835 ) / 0.018975
        ##b= 2000.0* (math.exp( (EREST_ACT + 0.0065 - x[i]*1e-3 )/0.027)) - a
    ##else:
        ##a= 2000.0 * math.exp( ( EREST_ACT + 0.0065 - x[i]*1e-3 )/0.027 )
        ##b= 0.0
    ##frrd.append(a)
    ##brrd.append(b)
        
    
##plt.subplot(1,2,2)
##alpha1,=plt.plot(x,frrd)
##beta1,=plt.plot(x, brrd)
##plt.legend([alpha1,beta1],["alpha","beta"])
##plt.xlabel("V (mV)")
##plt.title("Activation gate, make_K_C()")
##plt.show()

####Activation variable for KA

###From paper

##fr=[]
##br=[]
##for i in range(len(x)):
    ##fr.append(1e3*0.02*(13.1-x1[i])/(math.e**((13.1-x1[i])/10.0)-1.0))
    ##br.append(1e3*0.0175*(x1[i]-40.1)/(math.e**((x1[i]-40.1)/10.0)-1.0))

##plt.figure( figsize=(10,5) )
##plt.subplot(1,2,1)
##alpha,=plt.plot(x,fr)
##beta,=plt.plot(x,br)
##plt.xlabel("V(mV)")
##plt.legend([alpha,beta],["alpha","beta"])
##plt.title("Activation gate, K_A, Traub 1991")
    
###From rdesigneurProtos

##AA=20e3 * (0.0131 + EREST_ACT)
##BA=-20e3
##CA=-1.0
##DA=-1.0 * (0.0131 + EREST_ACT)
##FA=-0.01

##AB=-17.5e3 * (0.0401 + EREST_ACT)
##BB=17.5e3
##CB=-1.0
##DB=-1.0 * (0.0401 + EREST_ACT)
##FB=0.01

##frrd=[] #Uses parameters from rdesigneurProtos.py
##brrd=[] #Uses parameters from rdesigneurProtos.py
##for i in range(len(x)):
    ##frrd.append((AA+BA*x[i]*1e-3)/(CA+math.e**((x[i]*1e-3+DA)/FA)))
    ##brrd.append((AB+BB*x[i]*1e-3)/(CB+math.e**((x[i]*1e-3+DB)/FB)))
    
##plt.subplot(1,2,2)
##alpha1,=plt.plot(x,frrd)
##beta1,=plt.plot(x, brrd)
##plt.legend([alpha1,beta1],["alpha","beta"])
##plt.xlabel("V (mV)")
##plt.title("Activation gate, make_K_A()")
##plt.show()


###( [ 20e3 * (0.0131 + EREST_ACT), -20e3, -1.0, -1.0 * (0.0131 + EREST_ACT),
###-0.01, -17.5e3 * (0.0401 + EREST_ACT), 17.5e3, -1.0, -1.0 * (0.0401 + EREST_ACT), 0.01, 3000, -0.1, 0.05 ] )

####Inactivation variable for Na

###From paper

##fr=[]
##br=[]
##for i in range(len(x)):
    ##fr.append(1e3*0.128*math.e**((17.0-x1[i])/18.0))
    ##br.append(1e3*4.0/(1+math.e**((40.0-x1[i])/5.0)))
    
##plt.figure( figsize=(10,5) )
##plt.subplot(1,2,1)
##alpha,=plt.plot(x,fr)
##beta,=plt.plot(x,br)
##plt.xlabel("V(mV)")
##plt.legend([alpha,beta],["alpha","beta"])
##plt.title("Inactivation gate, Na channel, Traub 1991")

###From rdesigneurProtos

##EREST_ACT=-0.060
##AA=128.0
##BA= 0.0
##CA=0.0
##DA= -1.0 * (0.017 + EREST_ACT)
##FA=0.018

##AB=4.0e3
##BB=0.0
##CB= 1.0
##DB= -1.0 * (0.040 + EREST_ACT)
##FB= -5.0e-3

##frrd=[]

##for i in range(len(x)):
    ##frrd.append((AA+BA*x[i]*1e-3)/(CA+math.e**((x[i]*1e-3+DA)/FA)))
    
##brrd=[]

##for i in range(len(x)):
    ##brrd.append((AB+BB*x[i]*1e-3)/(CB+math.e**((x[i]*1e-3+DB)/FB)))
    
##plt.subplot(1,2,2)
##alpha1,=plt.plot(x,frrd)
##beta1,=plt.plot(x,brrd)
##plt.legend([alpha1,beta1],["alpha","beta"])
##plt.xlabel("V (mV)")
##plt.title("Inactivation gate, make_Na()")
##plt.tight_layout()
##plt.show()

###Inactivation variable for Ca

##From paper

#fr=[]
#br=[]
#a=0.0
#b=0.0

#for i in range(len(x)):
    #if x1[i]<=0:
        #a=1e3*0.005
        #b=0.0
    #else:
        #a=1e3*math.e**(-x1[i]/20.0)/200.0
        #b=1e3*0.005-a
    #fr.append(a)
    #br.append(b)

#plt.figure( figsize=(10,5) )
#plt.subplot(1,2,1)
#alpha,=plt.plot(x,fr)
#beta,=plt.plot(x,br)
#plt.xlabel("V(mV)")
#plt.legend([alpha,beta],["alpha","beta"])
#plt.title("Inactivation gate, Ca channel, Traub 1991")        


##From rdesigneurProtos

#frrd=[]
#brrd=[]
#a=0
#b=0

#for i in range(len(x)):
        #if ( x[i]*1e-3 > EREST_ACT):
            #a = 5.0 * math.exp( -50 * (x[i]*1e-3 - EREST_ACT) )
        #else:
            #a = 5.0
        #b=5-a
        #frrd.append(a)
        #brrd.append(b)

#plt.subplot(1,2,2)
#alpha1,=plt.plot(x,frrd)
#beta1,=plt.plot(x,brrd)
#plt.legend([alpha1,beta1],["alpha","beta"])
#plt.xlabel("V (mV)")
#plt.title("Inactivation gate, make_Ca()")
#plt.tight_layout()
#plt.show()

####Inactivation variable for KA

###From paper

##fr=[]
##br=[]
##for i in range(len(x)):
    ##fr.append(1e3*0.0016*math.e**((-13.0-x1[i])/18.0))
    ##br.append(1e3*0.05/(1+math.e**((10.1-x1[i])/5.0)))

##plt.figure( figsize=(10,5) )
##plt.subplot(1,2,1)
##alpha,=plt.plot(x,fr)
##beta,=plt.plot(x,br)
##plt.xlabel("V(mV)")
##plt.legend([alpha,beta],["alpha","beta"])
##plt.title("Inactivation gate, KA channel, Traub 1991")     

###From rdesigneurProtos

##AA=1.6
##BA=0.0
##CA=0.0
##DA=0.013 - EREST_ACT
##FA=0.018

##AB=50.0
##BB=0.0
##CB=1.0
##DB=-1.0 * (0.0101 + EREST_ACT)
##FB=-0.005

###[ 1.6, 0.0, 0.0, 0.013 - EREST_ACT, 0.018, 50.0, 0.0, 1.0, 
### -1.0 * (0.0101 + EREST_ACT), -0.005, 3000, -0.1, 0.05 ]

##frrd=[] #Uses parameters from rdesigneurProtos.py
##brrd=[] #Uses parameters from rdesigneurProtos.py
##for i in range(len(x)):
    ##frrd.append((AA+BA*x[i]*1e-3)/(CA+math.e**((x[i]*1e-3+DA)/FA)))
    ##brrd.append((AB+BB*x[i]*1e-3)/(CB+math.e**((x[i]*1e-3+DB)/FB)))
    
##plt.subplot(1,2,2)
##alpha1,=plt.plot(x,frrd)
##beta1,=plt.plot(x, brrd)
##plt.legend([alpha1,beta1],["alpha","beta"])
##plt.xlabel("V (mV)")
##plt.title("Inactivation gate, make_K_A()")
##plt.show()

x=range(0,100) #Ca conc in uM
CA_SCALE=1.0

frrd=[]
brrd=[]
fr=[]
br=[]

for i in range(len(x)):
    tu=(x[i]*1e-3)*(250/0.01) #conc in mM converted to Traub units
    fr.append(min(1e3*0.2e-4*tu, 1e3*0.01))
    br.append(1e3*0.001)
    
    frrd.append(min( 250.00 * CA_SCALE * (x[i]*1e-3), 10 )) #conc in mM
    #frrd.append(min( 0.2e-4*(x[i]*1e-3)*250/0.01, 10 )) #mM
    brrd.append(1.0)

plt.figure( figsize=(10,5) )
plt.subplot(1,2,1)
alpha,=plt.plot(x,fr)
beta,=plt.plot(x,br)
plt.xlabel("Ca conc (uM)")
plt.legend([alpha,beta],["alpha","beta"])
plt.title("Activation gate, K AHP channel, Traub 1991")

plt.subplot(1,2,2)
alpha1,=plt.plot(x,frrd)
beta1,=plt.plot(x, brrd)
plt.legend([alpha1,beta1],["alpha","beta"])
plt.xlabel("Ca conc")
plt.title("Activation gate, make_K_AHP()")
plt.show()

plt.plot(x,)