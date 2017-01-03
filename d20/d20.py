#!/usr/bin/python
 
import socket
import time

ip="192.168.21.106"
port=21664
for i in range (1,100):
  s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
  s.connect((ip,port))
  x= s.recv(1024)
  s.close()
  print str(x)
  y=x.split(" ")
  time.sleep(int(y[3]))
  port = int(y[1])

