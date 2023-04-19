from tkinter import *
class MyWindow:
    def __init__(self, win):
        self.txt1 = Entry(win, bd=2, width=25)
        self.txt1.place(x=30, y=25, height = 40)
        self.txt1.insert(0, "This is where I type my text")
window = Tk()
mywin = MyWindow(window)
window.geometry("230x80")
window.title("Text Field")
window.mainloop()