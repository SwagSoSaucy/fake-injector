from tkinter import *
from functools import partial
from colorama import Fore,Back, Style
import sys
import os
import socket


print(Fore.GREEN + 'Enter the password')
x = input()
if x == 'balls':
    print('access granted')

    def enter():
        win = Tk()
        win.title('REI Script editor')
        win.geometry('1440x600')
        text = Text(win, width=1440, height=200, font=('Arial',20,'bold'),fg='#FFA500',bg='#000000')
        text.pack()


        win.mainloop


    def click():
        exit()


    def worm():
        script = sys.argv
        name=str(script[0])

        
        os.system('start cmd')
        os.mkdir('clone')
        os.system(r"copy cmd.exe clone")
        os.system(r"copy" + name + "clone")
        




    

    root = Tk()
    root.title('REI')
    root.geometry('800x800')
    
    root.config(background="#000000")
    label = Label(root,text='roblox script injector',font=('Arial',20,'bold'),fg='#FFA500',bg='#000000')
    label.pack()
    label2 = Label(root,text='after you have typed the script, press the load button',font=('Arial',20,'bold'),fg='#FFA500',bg='#000000')
    label2.pack(padx=10, pady=10)
    
    button = Button(root,text='INJECT ',font=('Arial',40,'bold'),fg='#FFA500',bg="#000000")
    a = Button(root, text='EXIT',font=('Arial',40,'bold'),fg='#FFA500',bg="#000000")
    a.pack(side=RIGHT, padx=10, pady=10)

    a.config(command=click)
    button.config(command=enter)

    b = Button(root,text='LOAD',font=('Arial',40,'bold'),fg='#FFA500',bg="#000000")
    b.pack(side=TOP, padx=30, pady=30)

    b.config()
    





    button.pack(side=LEFT, padx=10, pady=10)





    root.iconbitmap("DukeWithHelmet.ico")
    
    root.mainloop()
    


else:
    print('out of my program')
    exit()

