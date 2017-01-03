#!/usr/bin/python

import sys,os
import time

fname = sys.argv[1]

f = open(fname)

lines = f.readlines()
f.close()
final=""
unclean=""
for line in lines:
  x=line.split(',')
  m=x[0]
  b=x[1]
  p=x[2]
  l=0x1337	#4149
  
  for y in range (33,127):
    # m = a * 0x1337 * b % p
    z=y*long(l)*long(b)%long(p)
    #print "y: "+ str(y)
    #print "Z: "+ str(z)
    #print "M: "+ m
    if z == long(m):
      #print "########################"
      #print str(y) + ": "+ str(unichr(y))
      final+=str(unichr(y))
      unclean+=str(y)
#      time.sleep(5)
      break

print final
print unclean
