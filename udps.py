import socket

server_address = ('localhost',4000)
buffer = 1024

udp_server = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)
udp_server.bind(server_address)

while(True):
    try:
        message, address = udp_server.recvfrom(buffer)
        print(message.decode())
    
    except:
        print("Error")