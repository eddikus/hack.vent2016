#!/usr/bin/python

import sys

a = 4
b = 7
c = 1337
d = 424242

x = (a | b)
print str(a)+" OR "+str(b)+"=  "+str(x)
y = (c & d)
print str(c)+ " AND "+str(d)+" ="+str(y)

z = (x^y)
print str(x)+" XOR "+str(y)+"= "+str(z)

j=(~z)
print "Z NOT = "+ str(j)

k=(0xB055 | j)
print "0xB055 OR "+str(j)+"= "+str(k)


### Other attempts to figure out why the hint use 32-bit?? maybe 32 bit python?
#j=(~z & 0xFF)
#print j

#k=(0xB055 | j)
#print k

#j=(~z & 0xFFFF)
#print j

#k=(0xB055 | j)
#print k

#j=(~z & 0xFFFFFF)
#print j

#k=(0xB055 | j)
#print k

