import socket

msgFromClient       = input("Enter the Roll Number:")

bytesToSend         = str.encode(msgFromClient)
serverAddressPort   = ("10.1.34.55", 4000)
bufferSize          = 1024
UDPClientSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)

UDPClientSocket.sendto(bytesToSend, serverAddressPort)

msgFromServer = UDPClientSocket.recvfrom(bufferSize)
msg = msgFromServer[0]

lst = (msg.decode()).split(",")

if(lst[0][0].isdigit()):
    print("Roll number:",lst[0])
    print("Name:",lst[1])
    print("CGPA:",lst[2])
else:
    print(lst[0])
