import socket

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server_address = ('localhost', 4000)
server_socket.bind(server_address)

server_socket.listen(1)
print("Server is listening..!")

while True:
    client_socket, client_address = server_socket.accept()
    
    try:
        while(True):
            data = client_socket.recv(1024)
            print("Client:",data.decode())

            if(data.decode()=="Bye" or data.decode()=="bye" or data.decode()=="BYE"):
                response = "Good Bye! Have a nice day."
                client_socket.send(response.encode())
                print("Chat completed..!")
                break
            
            response = input("Server: ")
            client_socket.send(response.encode())
                
    except:
        print("An error occurred during communication.")
    finally:
        client_socket.close()
