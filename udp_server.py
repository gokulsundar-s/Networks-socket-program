import socket
import mysql.connector as sql

mycon=sql.connect(host="localhost",user="root",passwd="gokul123",database="networks")
cursor=mycon.cursor()

localIP     = "10.1.34.55"
localPort   = 4000
bufferSize  = 1024

UDPServerSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)
 
UDPServerSocket.bind((localIP, localPort))

print("UDP server up and listening")

while(True):

    message, address = UDPServerSocket.recvfrom(bufferSize)

    show = ("SELECT Roll_number,Name,CGPA from cgpa where Roll_number='{}'").format(message.decode())
    cursor.execute(show)
    data=cursor.fetchall()
    print(message.decode())
    if(len(data)>=1):
        message = ",".join(str(data[0][i]) for i in range(3))
        UDPServerSocket.sendto(message.encode(), address)
        
    else:
        message="Data not found in database..!"
        UDPServerSocket.sendto(message.encode(), address)