#!/usr/bin/python

import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:

	print "\nSending evil buffer..."
	
	#Connect to IP, POP3 port
	s.connect(('10.11.8.156',110))

	#Receive banner
	data = s.recv(1024)
	
	#Print banner
	print data

	#Send username "test", receive and print reply
	s.send('USER test' + '\n\n')
	data = s.recv(1024)
	print data

	#Send password "test", receive and print reply
	s.send('PASS test\r\n')
	data = s.recv(1024)
	print data

	#Close socket
	s.close()
	print "\nDone!"

except:

	print "Could not connect to POP3!"
