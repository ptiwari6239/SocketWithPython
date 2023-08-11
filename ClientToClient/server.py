    
import socket 
import threading 
class store:
    def __init__(self,address,conn,username):
        self.addr = address
        self.connec = conn
        self.usr = username

    def connection(self):
        return self.connec
    
    def address(self):
        return self.addr
    
    def usrname(self):
        return self.usr

information = {}
def add_person(adrr,conn,username):
    person = store(adrr,conn,username)
    information[username] = person


def access_person(reference,msg):
    if reference in information:
        person = information[reference]
        person.connec.send(msg.encode(FORMAT))
        print(f"message send to username: {person.usr} succesful")
        # print(person.usrname())
    else:
        print("Person not found!")


PORT = 6677
FORMAT = "utf-8"
HEADER = 64
hostname=socket.gethostname()
SERVER = socket.gethostbyname(hostname)
ADDR = (SERVER,PORT)
server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server.bind(ADDR)
DISCONNECT_MESSAGE = "!CONNECT"
def handle_cilent(conn,addr,name):
        print(f"[{name}]  wanted to chat..\n")
        connected = True
        while connected:    
                
                user_mess = input("SERVER MESSAGE")
                conn.send(user_mess.encode(FORMAT))
                msg_length = conn.recv(HEADER).decode(FORMAT)
                if msg_length :
                    msg_length = int(msg_length)
                    msg = conn.recv(msg_length).decode(FORMAT)
                    print(msg)
                    if msg == DISCONNECT_MESSAGE:
                        connected = False
                UserToSend = "Enter receiver's name" 
                conn.send(UserToSend.encode(FORMAT))
                msg_length = conn.recv(HEADER).decode(FORMAT)
                if msg_length :
                    msg_length = int(msg_length)
                    receiver_name = conn.recv(msg_length).decode(FORMAT)
                access_person(receiver_name,msg)      
        conn.close()
def start():
    server.listen()
    print(f"[SERVER] server is listening on {SERVER}")
    while True:
        conn, addr = server.accept()
        user_name = "Enter Your Name"
        conn.send(user_name.encode(FORMAT))
        msg_length = conn.recv(HEADER).decode(FORMAT)
        if msg_length :
            msg_length = int(msg_length)
            msg = conn.recv(msg_length).decode(FORMAT)            
        add_person(addr,conn,msg)
        
        thread = threading.Thread(target=handle_cilent,args=(conn,addr,msg))
        thread.start()
        print(f"[ACTIVE CONNECTION] {threading.active_count()-1}" )

print("[SERVER] server is starting...")
start()
