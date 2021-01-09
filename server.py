from socket import AF_INET, socket, SOCK_STREAM
from threading import Thread
import time
import datetime
from person import Person
#global variables
HOST='localhost'
PORT=5500
BUFFSIZE=1024
ADDR=(HOST, PORT)

MAX_CONNECTION=10
BUFFSIZE=512
FORMAT='utf8'
persons = []
quit="quit"

SERVER=socket(AF_INET,SOCK_STREAM)
SERVER.bind(ADDR)

def broadcast(mssg,name):
    ##send new message tow ll new client
    ##param msg: bytes ["Ut8"]
    ##param name: str

    for person in persons:
        client=person.client
        try:
            client.send(bytes(name+":",FORMAT)+mssg)
        except Exception as e:
            print("[EXCEPTION]",e)

def wait_for_connection():
    #wait for new connection when got start new thread
    while(True):
        try:
            client,addr=SERVER.accept()
            person1=Person(addr,client)
            persons.append(person1)
            print(f"[CONNECTION]{addr} connected to server at {datetime.datetime.now()}")
            Thread(target=client_communication,args=(person1,)).start()
        except Exception as e:
            print("[FAILURE]",e)
            break

    print("SERVER CRASH")


def client_communication(person):
    ##thread to handle all messages from client
    #params  is PErson object 
    #get person name
    client=person.client
    #addr=person.addr
    name=client.recv(BUFFSIZE).decode(FORMAT)
    person.set_name(name)
    msg= bytes(f"{name} : has joined the chat!",FORMAT)

    broadcast(msg,"") #bradcast welcome messagfe
    while(True):
        
            msg=client.recv(BUFFSIZE)
            if msg==bytes("{quit}",FORMAT):
           
                client.close()
                persons.remove(person)
                #client.send(bytes(("{quit}",FORMAT)))
                broadcast(bytes(f"{name} : has left the chat",FORMAT)," ")
                print(f"[DISCONNNECTED] {name} disconnected")
                break
            else:
                broadcast(msg,name+": ") 
                print(f"{name}:",msg.decode(FORMAT))
        
    

if __name__ == "__main__":
    SERVER.listen(MAX_CONNECTION)
    print("WAITING FOR CONNECTION........")
    ACCEPT_THREAD=Thread(target=wait_for_connection)
    ACCEPT_THREAD.start()
    ACCEPT_THREAD.join()
    SERVER.close()
