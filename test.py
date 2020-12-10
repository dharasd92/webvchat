from socket import AF_INET, socket, SOCK_STREAM
from threading import Thread
import time

#GLOBAL CONSTANTS
BUFFSIZ=512

quit="quit"
FORMAT="utf8"
HOST="localhost"
PORT = 5500
ADDR = (HOST,PORT)
client_socket=socket(AF_INET, SOCK_STREAM)
client_socket.connect(ADDR)
messages=[]
def receive_message():
    #receive message from server
    #:param msg:str 

    while True:
        try:
            msg=client_socket.recv(BUFFSIZ).decode(FORMAT)
            messages.append(msg)
            print(msg)
        except Exception as e:
            print("[EXCEptION",e)
            break

def send_message(msg):
    client_socket.send(bytes(msg, FORMAT))
    if msg== "{quit}":
        client_socket.close()


         


receive_thread = Thread( target= receive_message)
receive_thread.start()
send_message("sourav")
input()
send_message("hello")
input()
send_message("how are you >?")
input()
send_message("{quit}")