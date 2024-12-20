import socket
target_host = "127.0.0.1"
target_port = 9998
#1.  create a socket object
client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
#2. send some data, here we are using sendto() instead of send() because we are 
#using UDP over TCP
client.sendto(b"AAABBBCCC",(target_host,target_port))
# receive some data using recvfrom() function, because we are UDP again
data, addr = client.recvfrom(4096)
print(data.decode())
client.close()