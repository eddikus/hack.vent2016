#!/usr/bin/python

import sys

dkey="KR40*^d?r!CdhX<w$`B;G.T{6*,TW"
#dkey="KR40*"
#skey="HV16-"
solution=""
z=3
for k in dkey:
  l = ord(k)
  if l == 46:
    l=127
  print l
  x = (l ^ z)	#'K' xor z
  #print "XOR: "+k+" ^ "+str(z)+" == "+chr(x)
  print "HEX: "+hex(l)+" ^ "+str(hex(z))+" == "+hex(x)
  solution+=chr(int(x))
  z+=1

print "-----------"
print solution
