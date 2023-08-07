import socket

sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
add = "20.0.10.136"
port = 9999
sock.connect((add,port))

# while True:
filename = "file.pdf"
try:
    fi = open(filename,"r")
    data = fi.read()
    if not data:
        print("no file found")
    while data:
        sock.send(str(data).encode())
        data = fi.read()
    fi.close()
except IOError:
    print("something wrong with the code")
