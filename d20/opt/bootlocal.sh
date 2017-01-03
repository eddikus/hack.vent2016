#!/bin/sh
knocker&
TERM=linux
# su -c aafire - tc

echo "trap '' 2" >> /home/tc/.profile
echo "aafire" >> /home/tc/.profile
