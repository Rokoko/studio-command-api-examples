
# ReceiveRecordingMessages.py
#  A UDP Server to receive recording messages from the Studio
# Rokoko (c) 2023

import socket

localIP     = "" # use broadcast, for local "127.0.0.1"
localPort   = 14048
bufferSize  = 1024

# Create a datagram socket
UDPServerSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)

# Bind to address and ip
UDPServerSocket.bind((localIP, localPort))

print ("Start Listening for Recording Messages at port {port}".format(port=localPort))

# Listen for incoming datagrams
while(True):

    bytesAddressPair = UDPServerSocket.recvfrom(bufferSize)

    message = bytesAddressPair[0]
    address = bytesAddressPair[1]

    clientMsg = "Message from Client:{}".format(message)
    clientIP  = "Client IP Address:{}".format(address)
    
    print(clientMsg)
    print(clientIP)