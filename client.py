from socket import AF_INET, socket, SOCK_STREAM
from threading import Thread,Lock
import time
#from person import Person
#global variables


class Client:
    #global variables for communication with server
    HOST='localhost'
    PORT=5500
    BUFFSIZE=1024
    ADDR=(HOST,PORT)
    MAX_CONNECTION=10
    BUFFSIZ=512
    FORMAT='utf8'
    

    def __init__(self,name):
        self.client_socket=socket(AF_INET, SOCK_STREAM)
        self.client_socket.connect(self.ADDR)
        self.messages=[]
        receive_thread = Thread( target= self.receive_message)
        receive_thread.start()
        self.send_message(name)
        self.lock=Lock()

    def receive_message(self):
    #receive message from server
    #:param msg:str 
        while True:
            try:
                msg=self.client_socket.recv(self.BUFFSIZ).decode(self.FORMAT)
                self.lock.acquire()
                self.messages.append(msg)
                self.lock.release()
                #print(msg)
            except Exception as e:
                print("[EXCEptION",e)
                break
    
    def send_message(self,msg):
        try:
            self.client_socket.send(bytes(msg, self.FORMAT))
            if msg== "{quit}":
                self.client_socket.close()
        except Exception as e:
            self.client_socket=socket(AF_INET,SOCK_STREAM)
            self.client_socket=socket.connect(self.ADDR)
            print(e)

    def get_messages(self):
        #return self string
        message_copy=self.messages[:]
        #make tsure memory safe to read from
        self.lock.acquire()
        self.messages=[]
        self.lock.release()
        return message_copy
    
    def disconnect(self):
        self.send_message("{quit}")
