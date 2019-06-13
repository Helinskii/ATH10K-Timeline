from tkinter import *

class Window(Frame):

    def __init__(self, master = None):
        Frame.__init__(self, master)
        self.master = master
        self.init_window()

    def init_window(self):
        self.master.title("GUI")

        self.pack(fill = BOTH, expand = 1)

        print_label = Label(self, text = ' ', bg = 'white', height = '150', width = '200')
        print_label.pack(side = LEFT)

        temp_label = Label(self text = 'hello', bg = 'black', height = '150', width = '200')
        temp_label.pack(side = RIGHT)
        
        quitButton = Button(self, text = "Quit", command = self.client_exit)

        quitButton.place(x = 200, y = 150)

    def client_exit(self):
        exit()

root = Tk()

root.geometry("400x300")
app = Window(root)
root.mainloop()
