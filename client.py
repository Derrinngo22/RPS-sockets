import socket
from tkinter import *
from threading import Thread


def receive():
    while True:
        msg = s.recv(1024).decode("utf-8")
        msg_list.insert(END, msg)
        msg_list.see(END)

def send(event=None):
    msg = my_msg.get()
    my_msg.set("") 
    s.send(msg.encode())
    if msg == "{quit}":
        s.close()
        top.quit()

def rock(event=None):
    my_msg.set('R')
    send()

def paper(event=None):
    my_msg.set('P')
    send()

def scissors(event=None):
    my_msg.set('S')
    send()

def stats(event=None):
    my_msg.set("stats")
    send()

def close():
    my_msg.set("{quit}")
    send()

top = Tk()
top.title("RPS Showdown!")
messages_frame = Frame(top)
button_frame = Frame(top)
button_frame.pack(fill=X, side=BOTTOM)
my_msg = StringVar() 
scrollbar = Scrollbar(messages_frame) 
msg_list = Listbox(messages_frame, height=15, width=50, yscrollcommand=scrollbar.set)
scrollbar.pack(side=RIGHT, fill=Y)
msg_list.pack(side=LEFT, fill=BOTH)
msg_list.pack()
messages_frame.pack()

rock_button = Button(button_frame, text="Rock", command=rock)
paper_button = Button(button_frame, text="Paper", command=paper)
scissors_button = Button(button_frame, text="Scissors", command=scissors)
stats_button = Button(button_frame, text="Stats", command=stats)

button_frame.columnconfigure(0,weight=0)
button_frame.columnconfigure(1,weight=0)
button_frame.columnconfigure(2,weight=0)
button_frame.columnconfigure(3,weight=0)

rock_button.grid(row=0, column=0, padx=(50,0))
paper_button.grid(row=0, column=1)
scissors_button.grid(row=0, column=2)
stats_button.grid(row=0, column=3, padx=50)

top.protocol("WM_DELETE_WINDOW", close)

#socket communication
ADDR = (socket.gethostname(), 12000)

s = socket.socket()
s.connect(ADDR)

receive_thread = Thread(target=receive)
receive_thread.start()
mainloop()  

