import socket
host = "20.0.12.224"
port = 9999
sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
sock.bind((host,port))
sock.listen()
conn , addr = sock.accept()

data = conn.recv(1024).decode()
filename = "newFile.txt"
fo = open(filename,"w")
while data:
    if data:
        fo.write(data)
        data = conn.recv(1024).decode()
fo.close()
conn.close()
