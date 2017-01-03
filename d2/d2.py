#!/usr/bin/python

import sys

std="1234567890-=qwertyuiop[]asdfghjkl;'zxcvbnm,./Q"
dro="1234567890[]',.pyfgcrl/=aoeuidhtns-;qjkxbmwvz\""

d2="DK16[OEdo[''lu[;\"Nl[R\"D4[2Qmi"

solution=""

for x in d2:
  y=x
  up=0
  if x.istitle():
    y = x.lower()
    up=1
  
  z=dro.index(y)

  a=std[z]
  if up ==1:
    a= a.upper()
  print y + " -> " +a
  solution +=a

print solution
