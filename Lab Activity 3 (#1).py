from tkinter import *
class Mywindow:
    def __init__(self, win):
        self.lbl1 = Label(win, text="Laboratory Activity 5")
        self.lbl1.place(x=50, y=20)
        self.lbl2 = Label(win, text="Submitted to: Mam Sayo")
        self.lbl2.place(x=50, y=40)

window = Tk()
mywin = Mywindow(window)
window.geometry("230x80")
window.title("Label")
window.mainloop()

