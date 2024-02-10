import socket

print("Enter your marks below:")

m1 = input("Probability & statistics:")
m2 = input("Database management system:")
m3 = input("Python programming:")
m4 = input("Design and analysis of algorithms:")
m5 = input("Operating systems:")
m6 = input("Web technologies:")

msgFromClient = m1+" "+m2+" "+m3+" "+m4+" "+m5+" "+m6

bytesToSend         = str.encode(msgFromClient)
serverAddressPort   = ("10.1.74.70", 4000)
bufferSize          = 1024
UDPClientSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)

UDPClientSocket.sendto(bytesToSend, serverAddressPort)

msgFromServer = UDPClientSocket.recvfrom(bufferSize)

msg = ((msgFromServer[0]).decode()).split()

print("\nYOUR GRADES:\n")
print("Probability & statistics:",msg[0])
print("Database management system:",msg[1])
print("Python programming:",msg[2])
print("Design and analysis of algorithms:",msg[3])
print("Operating systems:",msg[4])
print("Web technologies:",msg[5])