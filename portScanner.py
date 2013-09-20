# Author: Ronnie Nigash
# Date: 9/19/13
# Description: Scans common ports for particular website, allows for user to enter specific port
	
from socket import *
targetHost = raw_input("What is the web address?: ")

targetPorts = [21, 22, 23, 25, 42, 43, 53, 67, 79, 80, 102, 110, 115, 119, 123, 135, 137, 143, 161, 179, 379, 389, 443, 445, 465, 636, 993, 995, 1026, 1080, 1090, 1433, 1434, 1521, 1677, 1701, 1720, 1723, 1900, 2409, 3101, 3306, 3389, 3390, 3535, 4321, 4664, 5190, 5500, 5631, 5632, 5900, 7070, 7100, 8000, 8080, 8799, 8880, 9100, 19430, 39720]

targetPortsInput = raw_input("Any particular port first?: ") # <-- port is first run, then continues through other common ports

targetPorts.reverse() # <-- puts the list backwards
targetPorts.append(targetPortsInput) # <-- appends the wanted value at end
targetPorts.reverse() # <-- reverses the list, now appended value is at front

def connectionScan(targetHost, targetPort):
    try:
        connectionSocket=socket(AF_INET, SOCK_STREAM)
        connectionSocket.settimeout(10)
        connectionSocket.connect((targetHost, targetPort))
        connectionSocket.settimeout(None)
        print("%d/tcp open" % targetPort)
    except:
        print("%d/tcp closed" % targetPort)

def portScan(targetHost, targetports):
    try:
        targetIP = gethostbyname(targetHost)
    except:
        print("Cannot resolve '%s': Unknown host" % targetHost)
        return
    try:
        targetName = gethostbyaddr(targetIP)
        print('\nScan results for: %s' % targetName)
    except:
        print('\nScan results for: %s' % targetIP)
    for port in targetPorts:
        print('Scanning port %s' % port)
        connectionScan(targetHost, int(port))

def main():
    portScan(targetHost, targetPorts)

if __name__=='__main__':
    main()