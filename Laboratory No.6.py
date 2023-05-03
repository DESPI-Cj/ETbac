from tkinter import*
window = Tk()
window.geometry("500x500")
window.title("Table")

class Table:
    def __init__(self,win):
        self.num_rows = 4

    def create_table(self):
        # Create labels for 'a', 'a^2', and 'a^3'
        Label( text="a").grid(row=0, column=0)
        Label( text="a^2").grid(row=0, column=1)
        Label( text="a^3").grid(row=0, column=2)

        # Populate the table with values
        for i in range(1, self.num_rows + 1):
            Label( text=str(i)).grid(row=i, column=0)  # 'a' values
            Label( text=str(i ** 2)).grid(row=i, column=1)  # 'a^2' values
            Label( text=str(i ** 3)).grid(row=i, column=2)  # 'a^3' values

ETvac = Table(window)
ETvac.create_table()
window.mainloop()
