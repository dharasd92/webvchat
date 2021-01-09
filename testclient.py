from client import Client
from threading import Thread
import time
name=input('To Start messaging, enter your name :')
c1=Client(name)

def update_message():
    mssg=[]
    run=True
    while(run):
        time.sleep(0.1)
        new_messages=c1.get_messages()
        mssg.extend(new_messages)
        for msg in new_messages:
            print(msg)
            if msg=="{quit}":
                run=False
                break

Thread(target=update_message).start()

mssg=input("Enter your message\n")
run=True
while(run):
    if(mssg=='Exit' or mssg=='exit'):
        run=False
        c1.disconnect()
    else:
        c1.send_message(mssg)
        mssg=input()
