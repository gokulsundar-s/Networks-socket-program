import socket

client_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

server_address = ('localhost',4000)
client_socket.connect(server_address)

while(True):
    try:
        inp = input()
        client_socket.send(inp.encode())
    except:
        print("Error")
        break
client_socket.close()