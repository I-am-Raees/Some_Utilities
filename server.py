import socket
from unittest.mock import DEFAULT
from PIL import Image


server=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server.bind(("localhost",1002))

server.listen()
print("Server is ready to dislay the image ")


while True:
    client_socket,client_address=server.accept()
    filename = client_socket.recv(2048)
    try:

        im=Image.open(f"{filename.decode()}.jpg")
        im.show()
    except:
        im=Image.open(f"DEFAULT.jpg")
        im.show()
    
    client_socket.close()

         





