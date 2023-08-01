
import socket 
import threading 


print("......Welcome to python chating application.....")
print("1:- for cilent ")
print("2:- for server ")
address = {}
user = int(input())

if user == 2:
    PORT = 6677
    HEADER = 64
    FORMAT = 'utf-8'
    HOSTNAME = socket.gethostname()
    SERVER = socket.gethostbyname(HOSTNAME)
    # SERVER = "20.0.4.26"
    ADDR = (SERVER,PORT)
    server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    server.bind(ADDR)
    DISCONNECT_MESSAGE = "!CONNECT"

    # SERVER SIDE 
    def handle_cilent(conn,addr):
        print(f"[{addr}]  wanted to chat..\n")
        connected = True
        while connected:
            msg_length = conn.recv(HEADER).decode(FORMAT)
            if msg_length :
                msg_length = int(msg_length)
                msg = conn.recv(msg_length).decode(FORMAT)
                if msg == DISCONNECT_MESSAGE:
                    connected = False
                    
            
                while True:
                    print(f"[{addr}]  {msg} ")
                    user_mess = input("Ur mesage \n")
                    conn.send(user_mess.encode(FORMAT))
                    msg_length = conn.recv(HEADER).decode(FORMAT)
                    if msg_length :
                        msg_length = int(msg_length)
                        msg = conn.recv(msg_length).decode(FORMAT)
                        if msg == DISCONNECT_MESSAGE:
                            connected = False
                            
        conn.close()

    # SERVER START
    def start():
        server.listen()
        while True:
            conn,addr = server.accept()
            address[addr] = conn
            print("hii")
            print(address)
            thread = threading.Thread(target=handle_cilent,args=(conn,addr))
            thread.start()
            


    print("SERVER STARTING....")
    start()
elif user == 1:
    PORT = 6677
    FORMAT = "utf-8"
    # HOSTNAME = socket.gethostname()
    # SERVER = socket.gethostbyname(HOSTNAME)
    SERVER = "20.0.5.158"
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
