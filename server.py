import socket

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_address = ("localhost",4000)

server_socket.bind(server_address)

server_socket.listen(1)

while True:
    client_socket, client_address = server_socket.accept()
    try:
        message = client_socket.recv(1024)
        print(message.decode())
    
    except:
        print("Error")
        break

client_socket.close()