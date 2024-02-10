import socket

localIP     = "10.1.74.70"
localPort   = 4000
bufferSize  = 1024

UDPServerSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)
 
UDPServerSocket.bind((localIP, localPort))

print("UDP server up and listening")

while(True):

    message, address = UDPServerSocket.recvfrom(bufferSize)
    
    print(address)
    
    s1 = (message.decode()).split()
    s2 = ""
    for i in s1:
        if(int(i)>=91 and int(i)<=100):
            s2 += "O "
        elif(int(i)>=81 and int(i)<=90):
            s2 += "A+ "
        elif(int(i)>=71 and int(i)<=80):
            s2 += "A "
        elif(int(i)>=61 and int(i)<=70):
            s2 += "B+ "
        elif(int(i)>=51 and int(i)<=60):
            s2 += "B "
        elif(int(i)>=41 and int(i)<=50):
            s2 += "C "
        else:
            s2 += "U "
    message = s2
    
    UDPServerSocket.sendto(message.encode(), address)
        
        
