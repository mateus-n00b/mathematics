'''
Realiza a multiplicacao de matrizes utilizando o modulo numpy.

Mateus-n00b, Outubro 2016

Versao 1.0

Licenca GPL
'''
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
var = open("/tmp/soSlow",'w')
var.write(str(np.dot(mA,mB)))
var.close()
