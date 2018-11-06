#UDPPingerClient.py 
#We need the following module to send 10 pings and implement timeout 
from socket import * 
import time 
#Create a UDP socket for client 
clientSocket = socket(AF_INET, SOCK_DGRAM) 
#Input to be sent to server as a ping 
message = raw_input('Input lowercase sentence') 
min = 5000 
max = 0 
all = 0 
lost = 0 
for i in range (1,11): 
	#Start time before sending packet 
	start = time.time() 
	#Sending packet 
	clientSocket.sendto(message.encode(), ('localhost', 12000)) 
	#implementing timeout of 1 second 
	clientSocket.settimeout(1.0) 
	#settimeout will throw an exception when timeout happens 
	#so we will put the rest of the code in a try-except block 
	try: 
		#Get message back from server if it has been sent 
		modifiedMessage, serverAddress = clientSocket.recvfrom(2048) 
	except: 
		#This will occur if a timeout exception is throw, in which 
		#case we will say it timed out and the loop will move forward 
		#also appropriate values will be incremented 
		print ("Request timed out") 
		lost += 1 
	continue
	#when a message is received back from the server we time RTT, add 
	#appropriate values into all, and set min max when necessary 
	stop = time.time() 
	all += stop-start 
	if stop-start > max: 
		max = stop-start 
	elif stop-start < min:
		min = stop-start 
	print modifiedMessage.decode() 
	#average start-stop time as of this point is calculated and printed 
	print ("Round Trip Time: " + str(stop-start)+ " seconds") 
	#Now that we are out of the loop we will calculate total average and loss percentage 
	average = all/10 
	lost = lost*10 
	#Printing loss percentage, total average, min, and max 
	print ("Loss Percentage: "+str(lost)+"%") 
	print ("Average Round Trip Time: "+str(average)+ " seconds") 
	print ("Min: "+str(min)+ " seconds") 
	print ("Max: "+str(max)+ " seconds") 
	#close socket 
	clientSocket.close()