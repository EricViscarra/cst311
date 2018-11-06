#TCPserver.py
from socket import *
import time
serverPort = 12000
# Create a TCP socket
serverSocket = socket(AF_INET,SOCK_STREAM)
# Assign IP address and port number to socket
serverSocket.bind(('',serverPort))
serverSocket.listen(1)
print ('The server is ready to receive')
#We will use count to differentiate the connections
#and stop after two connections are dealt with
count = 0
#time will be to see who sent the first message
start = time.time()
while True:
	count += 1
	#For the first connection
	if count == 1:
		#From the first we will get the message and time
		connectionSocket1, addr1 = serverSocket.accept()
		sentence1 = connectionSocket1.recv(1024).decode()
		stop1 = time.time()
	#Second Conncetion
	elif count == 2:
		#From the second we will get the message and time
		connectionSocket2, addr2 = serverSocket.accept()
		sentence2 = connectionSocket2.recv(1024).decode()
		stop2 = time.time()
	#After 2 connections we stop accepting and break
	if count > 1:
	break
#stop2 will always be longer than stop1 no matter what
longer = stop2-start
shorter = stop1-start
#If the difference between message times is so low that
#A human couldn't possibly do it, then we assume that it
#was queued up before message1 came in, so we say it came first
difference = longer-shorter
if difference < .01:
	ACK = sentence2 + ' received before ' + sentence1
	print (sentence2)
	print (sentence1)
else:
	ACK = sentence1 + ' received before ' +sentence2
	print (sentence1)
	print (sentence2)
#Sending acknoledgements to both clients
connectionSocket1.send(ACK.encode())
connectionSocket2.send(ACK.encode())
print (ACK)
print ('Sent acknowledgements to both X and Y')
#Ending connection with them both
connectionSocket1.close()
connectionSocket2.close()