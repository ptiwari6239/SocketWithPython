
import socket 
import threading 


print("......Welcome to python chating application.....")
PORT = 6677
FORMAT = "utf-8"
  
SERVER = ""   # ip address of server 
HEADER = 64
ADDR = (SERVER,PORT)
cilent = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
cilent.connect(ADDR)

def send(msg):
    message = msg.encode(FORMAT)
    msg_length = len(message)
    send_length = str(msg_length).encode(FORMAT)
    send_length += b' ' * (HEADER - len(send_length))
    cilent.send(send_length)
    cilent.send(message)
        


while True:
    print(cilent.recv(2048).decode(FORMAT))
    cilent_message = input()
    send(cilent_message)
