#TCPclient.py
from socket import *
serverName = 'localhost'
serverPort = 12000
#Making a socket to communicate with server
clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((serverName,serverPort))
#Sending Client and Name information
sentence = raw_input('Input lowercase sentence:')
print (sentence)
clientSocket.send(sentence.encode())
#Getting response from server about who sent first
result = clientSocket.recv(1024)
print ('From Server:', result.decode())
#Closing Socket
clientSocket.close()