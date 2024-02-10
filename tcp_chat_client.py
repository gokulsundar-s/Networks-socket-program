import socket

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server_address = ('localhost', 4000)
client_socket.connect(server_address)


while(True):
    message = input("Client: ")
    client_socket.send(message.encode())

    response = client_socket.recv(1024)
    print("Server:",response.decode())
        
    if(message=="Bye" or message=="bye" or message=="BYE"):
        break
    
client_socket.close()