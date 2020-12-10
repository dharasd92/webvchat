from client import Client
from threading import Thread
import time
c1=Client("tim")
c2=Client("joe")



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

c1.send_message("hi")
time.sleep(5)
c2.send_message("hello")
time.sleep(5)
c1.send_message("Whatsup")
time.sleep(5)

c2.send_message("nothing mucgh ")
#time.sleep(3)
time.sleep(5)
c1.send_message("boring")
time.sleep(5)
c1.disconnect()
#time.sleep(3)
time.sleep(2)
c2.disconnect()