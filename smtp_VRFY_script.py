#!/usr/bin/python
import socket
import sys

if len(sys.argv) != 2:
    print "Usage: vrfy.py <username>"
    sys.exit(0)
    
#Create socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#Connect to server
connect = s.connect(('10.11.1.22', 25))

#Receive banner
banner = s.recv(1024)

print banner

#VRFY user
s.send('VRFY ' + sys.argv[1] + '\r\n')
result = s.recv(1024)
print result

#Close socket
s.close()
