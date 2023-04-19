from tkinter import *
class MyWindow:
    def __init__(self, win):
        self.lbl1 = Label(win, text="Charles Babbage", font = "Arial, 15", bg = "cyan" )
        self.lbl1.place(x=40, y=20)
window = Tk()
mywin = MyWindow(window)
window.geometry("230x80")
window.title("Father of Computer")
window.mainloop()

