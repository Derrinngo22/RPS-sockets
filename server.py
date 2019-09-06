import socket
import threading
import random

valid_input = ['R','P','S']
s = socket.socket()
host = socket.gethostname()
port = 12000
s.bind((host, port))

s.listen(5)
c = None

dict = {'R':"Rock", 'P':"Paper", 'S':"Scissors"}
win_count = 0
loss_count = 0
draw_count = 0
while True:
    if c is None:
        print ("Waiting for connection")
        c, addr = s.accept()
        print ('Got connection from ', addr)
        welcome_string = "Welcome to Rock, Paper, Scissors! "
        c.send(welcome_string.encode())
    else:
        user_choice = c.recv(1024).decode("utf-8").upper()
        if user_choice in valid_input:
            cpu_choice = random.choice(valid_input)
            msg = "I picked "+ dict.get(cpu_choice) + "!"
            c.send(msg.encode("utf-8"))
            msg = "You picked "+dict.get(user_choice)+ "!"
            c.send(msg.encode("utf-8"))
            if user_choice == 'R' and cpu_choice == 'S' or user_choice == 'S' and cpu_choice == 'P' or user_choice == 'P' and cpu_choice == 'R':
                msg = " You Win!"
                win_count += 1
            elif user_choice == cpu_choice:
                msg = " It's a Draw!"
                draw_count = draw_count+1
            else:
                msg = " You Lost!"
                loss_count += 1
            c.send(msg.encode("utf-8"))
        elif user_choice == "STATS":
            msg = "Wins: "+ str(win_count)+" Draws: "+ str(draw_count)+ " Losses: "+str(loss_count)
            c.send(msg.encode("utf-8"))
    
