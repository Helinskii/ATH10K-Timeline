from tkinter import *
import random
from PIL import ImageTk, Image
root = Tk()
root.geometry("700x750+100+100")
root.configure(background='deepskyblue')
root.title("ATH10K TIMELINE")
path = r"C:\Users\Pranav\Desktop"
img = ImageTk.PhotoImage(Image.open(path))
panel = Label(root, image = img)
panel.pack(side = "bottom", fill = "both", expand = "yes")

main_menu = Menu(root)
root.config(menu=main_menu)
fileMenu = Menu(main_menu)
main_menu.add_cascade(label="STAs",menu=fileMenu)
T = Text(root,height=40, width=55,bg="linen",bd= 5)
txt = Text(root,height=21, width=20,bg="lightblue",bd=4)
def _fun1():
    T.config(state="normal")
    mac()
    flag()
    T.config(state="disabled")
def _fun():
    fileMenu.add_command(label="MAC 1", command=_fun1)
    fileMenu.add_command(label="MAC 2", command=mac)
    fileMenu.add_command(label="MAC 3", command=mac)
    T.config(state="normal")
    T.config(state="disabled")
def flag():
    txt.config(state="normal")
    txt.insert(INSERT, "Flaf1\n")
    txt.insert(INSERT, "Flag2\n")
    txt.insert(INSERT, "Flag3\n")

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


Button1 = Button(root,text="Fetch",command= _fun)

Button2 = Button(root,text="Display",command= _fun1)

Button4 = Button(root,text="Quit",command=  quit)


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


