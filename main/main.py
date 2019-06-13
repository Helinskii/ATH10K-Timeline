#!/usr/bin/python3

import parsing
from tkinter import *
import random
import sys
import subprocess
from functools import partial

root = Tk()
root.geometry("780x830+100+100")
root.configure(background='RoyalBlue1')
root.title("ATH10K TIMELINE")

main_menu = Menu(root)
root.config(menu=main_menu)
fileMenu = Menu(main_menu)
main_menu.add_cascade(label="STAs",menu=fileMenu)

T = Text(root,height=47, width=65, bg="lemonchiffon",bd=5)
txt = Text(root,height=21, width=20, bg="lightblue",bd=4)
T.configure(state="disabled")

main_heading = Label(root, text = "Qualcomm\nChallenge")
main_heading.config(font=('Courier', 23,"bold"),bd=6,bg="RoyalBlue1",fg="lightcyan")
main_heading.pack()
main_heading.place(x=0, y=15, height=85, width=220)

flag_heading = Label(root, text = "Flags")
flag_heading.config(font=('Courier', 15,"bold"),bd=6,bg="RoyalBlue1",fg="lightcyan")
flag_heading.pack()
flag_heading.place(x=0, y=425, height=20, width=220)

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
    T.delete(1.0, END)
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

    flag_list = []
    
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

    txt.configure(state="normal")
    txt.delete(1.0, END)
    txt.configure(state="disabled")
    if flag_list:
        flag_display(flag_list)
        
    T.config(state="disabled")
    

def display_log():
    T.config(state="normal")
    T.delete(1.0, END)

    try:
        mac_file = open('mac_address.txt', 'r')
        mac_info = mac_file.readlines()
        mac_file.close()

    except IOError:
        T.insert(INSERT, "No parsed data found. Kindly click 'Fetch'.")

        # Debug Statement
        print("No parsed data found. Click 'Fetch'.")
        return

    
    mac_addr = []
    for mac in mac_info:
        mac_addr.append(mac.rstrip('\n'))

    # Debug Statement
    print(mac_addr)

    T.insert(INSERT, "Displaying all parsed logs\n\n")
    for addr in mac_addr:
        sta_file = open('MAC Address - ' + addr, 'r')
        all_text = sta_file.read()

        # Debug Statement
        print(all_text)
        T.insert(INSERT, all_text)
        sta_file.close()

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

Button3 = Button(root, text='Delete', command= dele)

Button4 = Button(root,text="Quit", command=  quit)

Button1.pack()
Button1.place(x = 62, y = 115, height=50, width=100)

Button2.pack()
Button2.place(x = 62, y = 190, height=50, width=100)

Button3.pack()
Button3.place(x = 62, y = 265, height=50, width=100)

Button4.pack()
Button4.place(x = 62, y = 340, height=50, width=100)

Button1.config(font=(' Serif', 15,"bold"),bd=8,bg="lightcyan",fg="black")
Button2.config(font=('Serif', 15,"bold"),bd=8,bg="lightcyan",fg="black")
Button3.config(font=(' Serif', 15,"bold"),bd=8,bg="lightcyan",fg="black")
Button4.config(font=('Serif', 15,"bold"),bd=8,bg="lightcyan",fg="black")

T.pack()
T.place(x=240,y=10)
txt.pack()
txt.place(x=20,y=450)


root.mainloop()


