#!/usr/bin/env python

import time

chksums = [0xc82065c2,0x94b12c65,0x7a6ccece,0x9493866c,0xfac9fa1]

def crc(x,a):
  x=0xffffffff & ~x
  for i in xrange(4):
    x ^= ord(a[i])
    for j in xrange(8):
      x= (x>>1)^ (0xedb88320 & -(x&1))
  return 0xffffffff & ~x

alpha="0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
s="HV16"

for i in xrange(len(chksums)):
  next=0
  for n in range(48,123):
    if next==1:
      break
#    print "Starting letter is: "+str(chr(n))
    for nn in range(48,123):
      if next==1:
        break
      for nnn in range(48,123):
        if next==1:
          break
        for nnnn in range(48,123):
          string1 = chr(n)+""+chr(nn)+""+chr(nnn)+""+chr(nnnn)
          c2=crc(0,string1)
          if hex(chksums[i]) in hex(c2):
            print string1
            s+="-"+string1
            next=1 
            break
            
#print hex(crc(0,"8X9z"))
print "\n"+s
