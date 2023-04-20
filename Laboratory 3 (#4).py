from tkinter import *
window = Tk()
window.title("Button")
window.geometry("350x150")

class Color_Changer:
    def __init__(self,win):
        self.button1 = Button(win,text="Color", bg="Blue",fg="Red")
        self.button1.place(x=50,y=100)
        self.button2 = Button(win,text="<---Click to change the color of the button")
        self.button2.place(x=100,y=100)
        self.button2.bind('<Button-1>', self.change)

    def change(self, event):
        color = self.button1.cget("background")
        if color == "blue":
            self.button1.config(bg="yellow")
        else:
            self.button1.config(bg="blue")

mywin = Color_Changer(window)
window.mainloop()
