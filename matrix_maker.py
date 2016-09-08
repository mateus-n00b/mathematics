'''
Programa para a criacao de matrizes.

Mateus-n00b, Setembro 2016

Versao 1.0

Licenca GPL
'''
import random,os
C = []
lin = raw_input("QTD LINES>> ")
col = raw_input ("QTD COLUMMS>> ")
matrix = open("%sx%s.in" % (lin,col),'w')

if  lin.isdigit() or col.isdigit():
	lin = int(lin)
	col = int(col)
	for i in range(0,lin):
	     C+= [[random.randint(1,100) for x in range(0,col)]]
	    
	C = str(C).replace("[","")
	C = C.replace("]","\n")
	C = C.replace(",","")
	matrix.write(str(C))
	matrix.close()
else:
	print "Invalid entry! Exiting..."
