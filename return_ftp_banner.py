import socket
def retBanner(ip, port):
	try:
		socket.setdefaulttimeout(2)
		s = socket.socket()
		s.connect((ip, port))
		banner = s.recv(1024)
		return banner
	except:
		return

def checkVulns(banner):

	if 'Freefloat FTP server (version 1.00)' in banner:
		print '[+] FreeFloat FTP server is vulnerable.'

	elif '3Com 3CDaemon FTP server version 2.0' in banner:
		print '[+] 3CDaemon FTP server is vulnerable.'

	elif 'Ability Server 2.34' in banner:
		print '[+] Ability FTP server is vulnerable.'

	elif 'Sami FTP server 2.0.2' in banner:
		print '[+] Sami FTP server is vulnerable.'

	else:
		print '[-] FTP server is not vulernable.'

	return

def main():
	portList = [21,22,25,80,110]

	for y in range(1,255):
		ip = '10.11.' + str(y)
		for x in range(1,255):
			ip = '10.11.0.' + str(x)
			for port in portList:
				banner = retBanner(ip, port)
				if banner:
					print '[+] ' + ip + ': ' + banner
					checkVulns(banner)

if __name__ == '__main__':
	main()
