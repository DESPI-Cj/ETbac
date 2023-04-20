import tkinter as tk

def toggle_color():
    if label["bg"] == "blue":
        label.config(bg="yellow")
    else:
        label.config(bg="blue")

root = tk.Tk()
root.title("Button")
label = tk.Label(root, text="Color",fg='red', bg="blue")
label.pack(pady=50)

button = tk.Button(root, text="Click to change the color of the button", command=toggle_color)
button.pack(pady=10)

root.mainloop()
