#!/usr/bin/python3

import parsing_new as parsing
from tkinter import *
import random
import sys
import subprocess
from functools import partial
#from PIL import ImageTk, Image
root = Tk()
root.geometry("700x750+100+100")
root.configure(background='deepskyblue')
root.title("ATH10K TIMELINE")
#path = r"C:\Users\Pranav\Desktop"
#img = ImageTk.PhotoImage(Image.open(path))
#panel = Label(root, image = img)
#panel.pack(side = "bottom", fill = "both", expand = "yes")

main_menu = Menu(root)
root.config(menu=main_menu)
fileMenu = Menu(main_menu)
main_menu.add_cascade(label="STAs",menu=fileMenu)
T = Text(root,height=40, width=55,bg="linen",bd= 5)
txt = Text(root,height=21, width=20,bg="lightblue",bd=4)

def display():
    subprocess.call(['./Router.sh'])

def fetch():
    display()
    parsing.parse()
    T.config(state="normal")

    try:
        mac_file = open('mac_address.txt', 'r')
        T.delete(1.0, END)
        T.insert(INSERT, "MAC file found\n\n")
        mac_addr = mac_file.readlines()
        for mac in mac_addr:
            fileMenu.add_command(label=mac.rstrip('\n'), command=partial(sta_data, mac.rstrip('\n')))
    except IOError:
        T.insert(INSERT, "MAC file not found\n\n")
     
    T.config(state="disabled")

def sta_data(mac_addr):
    print(mac_addr)
    T.config(state="normal")

    T.insert(INSERT, "Showing parsed log for - " + mac_addr + "\n\n")
    mac_filename = 'MAC Address - ' + mac_addr.rstrip('\n')

    mac_file = open(mac_filename, 'r')
    mac_info = mac_file.read()
    mac_file.close()

    T.insert(INSERT, mac_info)
    T.insert(INSERT, "\n\n")

    log_file = open("data.txt", "r")
    lines = log_file.readlines()
    log_file.close()
    for line in lines:
        flag_loc = line.find('flags')
        ma = line.find(mac_addr)
        if ma > 0 and flag_loc > 0:
            flag_end = line.find('peer_bw_rxnss_override')
            flag = int(line[flag_loc + 6:flag_end - 1], 16)
            flag_list = parsing.flag_decode(flag)
            print(flag_list)
        else:
            continue

    flag_display(flag_list)
        
    T.config(state="disabled")
    

def display_log():
    pass
    
def flag_display(flags):
    txt.config(state="normal")
    txt.delete(1.0, END)
    
    for flag in flags:
        txt.insert(INSERT, flag + '\n')
    
    txt.config(state="disabled")

def _quit():
    root.destroy()

def mac():
    T.config(state="normal")
    T.insert(INSERT, "Debug log 1")
    T.config(state="disabled")

def dele():
    T.config(state="normal")
    T.delete(1.0, END)
    T.config(state="disabled")

    txt.config(state="normal")
    txt.delete(1.0, END)
    txt.config(state="disabled")


Button1 = Button(root,text="Fetch", command= fetch)

Button2 = Button(root,text="Display", command= display_log)

Button4 = Button(root,text="Quit", command=  quit)


Button1.pack()
Button1.place(x = 20, y = 50, height=50, width=100)
Button2.pack()
Button2.place(x = 20, y = 125, height=50, width=100)
Button4.pack()
Button4.place(x = 20, y = 275, height=50, width=100)
Button1.config(font=(' Serif', 15,"bold"),bd=8,bg="gray",fg="black")
Button2.config(font=('Serif', 15,"bold"),bd=8,bg="gray",fg="black")
Button4.config(font=('Serif', 15,"bold"),bd=8,bg="gray",fg="black")
T.pack()
T. place(x=220,y=50)
txt.pack()
txt. place(x=20,y=350)
btn = Button(root, text='Delete', command= dele)
btn.place(x = 20, y = 200, height=50, width=100)
btn.config(font=(' Serif', 15,"bold"),bd=8,bg="gray",fg="black")

root.mainloop()


