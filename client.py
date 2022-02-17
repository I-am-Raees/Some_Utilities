# import the utilities that will be required 
from email import message           # message is the input name of the image that will be used
import socket                       #Socket is the Particular library where


client=socket.socket(socket.AF_INET,socket.SOCK_STREAM)   #Used the sock stream for the TCP connection
client.connect(("localhost",1002))                        #Used the 1002 socket port number


message=input("Enter Image Name That Is Stored IN The Server:")
client.send(message.encode())
client.close()
