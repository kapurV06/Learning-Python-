import socket 
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#AF_INET = ipv4
#SOCK_STREAM = tcp
s.bind((socket.gethostname(),1234))
#socket is an endpoint that sends and receives data.
s.listen(5)

while True : 
  clientSocket,address = s.accept()
  print(f"Connection from {address}  has been established!")
  clientSocket.send(bytes("welcome to the server","utf-8"))