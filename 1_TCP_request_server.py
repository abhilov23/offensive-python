import socket
#we are sending a request to the server using the socket
#in return of that server returns us the response

target_host = "www.google.com"
target_port = 80
# create a socket object
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# connect the client
client.connect((target_host,target_port))
# send some data
client.send(b"GET / HTTP/1.1\r\nHost: google.com\r\n\r\n")
# receive some data
response = client.recv(4096)
print(response.decode())
client.close()