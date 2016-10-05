import numpy as np
import os,time

# ------------ Matrix Sizes  ------------
# Choose an size. 
#mA = np.arange(25).reshape(5,5)
#mA = np.arange(400).reshape(20,20)
#mA = np.arange(10000).reshape(100,100)
#mA = np.arange(1000000).reshape(1000,1000)
mA = np.arange(4000000).reshape(2000,2000)
#mA = np.arange(16000000).reshape(4000,4000)
mB = mA
var = open("/tmp/resultado_local",'w')
var.write(str(np.dot(mA,mB)))
var.close()
