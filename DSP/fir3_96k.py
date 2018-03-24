import matplotlib.pyplot as plt
from plot_mfreqz_impz import mfreqz, impz

#a = (-86825,63854,702930,-198615,-3055544,-569238,10827251,18186235,10827251,-569238,-3055544,-198615,702930,63854,-86825)

##FIR2 384K
#a = (-161,1552,-2058,-10709,23236,37108,-111595,-88101,361771,168661,-927998,
#-304275,2076632,632745,-4488722,-2018464,11457418,19940014,11457418,
#-2018464,-4488722,632745,2076632,-304275,-927998,168661,361771,-88101,
#-111595,37108,23236,-10709,-2058,1552,-161)
#n = len(a)
#SampleRate = 384000         #Hz
#PassBandEdge = 374000       #Hz
#StopBandEdge = 500000       #Hz
#StopBandAttenu = 53       #dB
#PassBandStart = 20          #Hz
#PassBandStop = 360000       #Hz
#PassBandRipple = 1.125        #dB

#FIR2 192K
a = (-90,-530,-820,1588,6825,3353,-20328,-34595,21687,114519,56390,-214540,-313747,
179066,775592,288441,-1209774,-1479191,982591,3372163,965643,-5253883,
-6416788,4568767,21930026,30464097,21930026,4568767,-6416788,-5253883,
965643,3372163,982591,-1479191,-1209774,288441,775592,179066,-313747,
-214540,56390,114519,21687,-34595,-20328,3353,6825,1588,-820,-530,-90)
n = len(a)
SampleRate = 192000         #Hz
PassBandStart = 20          #Hz
PassBandStop = 142000       #Hz
PassBandRipple = 0.8        #dB
PassBandEdge = 147000       #Hz
StopBandEdge = 214000       #Hz
StopBandAttenu = 85.5       #dB

#Frequency and phase response
mfreqz(a, 1, SampleRate=192000, PassBandStop=142000, PassBandRipple=0.8, 
    PassBandEdge=147000, StopBandEdge=214000, StopBandAttenu=85.5)
#Impulse and step response
impz(a)
#plt.show()