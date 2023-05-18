from tkinter import *

window = Tk()
window.geometry("1080x975+10+10")
window.title("Unit Converter")


class UnitConverter:
    def __init__(self, win):
        self.txt1 = Entry(win, bd=15, width="20", bg="black", font=("Arial", 70), fg="white")
        self.txt1.grid(row=0, sticky="nw", padx=5)

        self.btn1 = Button(win, bd=1, height="-15", text="C", width=26, font=("Arial", 28, "bold"), bg="orange")
        self.btn1.grid(sticky="nw", padx=4)
        self.btn1.bind('<Button-1>', self.clear)

        self.btn2 = Button(win, bd=1, width="13", text="7", height="3", font=("Arial", 14), bg="seashell4")
        self.btn2.grid(row=2, sticky="w", padx=5, pady=2)
        self.btn2.bind('<Button-1>', self.seven)

        self.btn3 = Button(win, bd=1, width="13", text="8", height="3", font=("Arial", 14), bg="seashell4")
        self.btn3.grid(row=2, sticky="w", padx=157, pady=2)
        self.btn3.bind('<Button-1>', self.eigth)

        self.btn4 = Button(win, bd=1, width="13", text="9", height="3", font=("Arial", 14), bg="seashell4")
        self.btn4.grid(row=2, sticky="w", padx=309, pady=2)
        self.btn4.bind('<Button-1>', self.nine)

        self.btn5 = Button(win, bd=1, width="13", text="/", height="3", font=("Arial", 14), bg="orange")
        self.btn5.grid(row=2, sticky="w", padx=460, pady=2)
        self.btn5.bind('<Button-1>', self.divide)

        self.btn6 = Button(win, bd=1, width="13", text="4", height="3", font=("Arial", 14), bg="seashell4")
        self.btn6.grid(row=3, sticky="w", padx=5, pady=2)
        self.btn6.bind('<Button-1>', self.four)

        self.btn7 = Button(win, bd=1, width="13", text="5", height="3", font=("Arial", 14), bg="seashell4")
        self.btn7.grid(row=3, sticky="w", padx=157, pady=2)
        self.btn7.bind('<Button-1>', self.five)

        self.btn8 = Button(win, bd=1, width="13", text="6", height="3", font=("Arial", 14), bg="seashell4")
        self.btn8.grid(row=3, sticky="w", padx=309, pady=2)
        self.btn8.bind('<Button-1>', self.six)

        self.btn9 = Button(win, bd=1, width="13", text="*", height="3", font=("Arial", 14), bg="orange")
        self.btn9.grid(row=3, sticky="w", padx=460, pady=2)
        self.btn9.bind('<Button-1>', self.multiply)

        self.btn10 = Button(win, bd=1, width="13", text="1", height="3", font=("Arial", 14), bg="seashell4")
        self.btn10.grid(row=4, sticky="w", padx=5, pady=2)
        self.btn10.bind('<Button-1>', self.one)

        self.btn11 = Button(win, bd=1, width="13", text="2", height="3", font=("Arial", 14), bg="seashell4")
        self.btn11.grid(row=4, sticky="w", padx=157, pady=2)
        self.btn11.bind('<Button-1>', self.two)

        self.btn12 = Button(win, bd=1, width="13", text="3", height="3", font=("Arial", 14), bg="seashell4")
        self.btn12.grid(row=4, sticky="w", padx=309, pady=2)
        self.btn12.bind('<Button-1>', self.three)

        self.btn13 = Button(win, bd=1, width="13", text="-", height="3", font=("Arial", 14), bg="orange")
        self.btn13.grid(row=4, sticky="w", padx=460, pady=2)
        self.btn13.bind('<Button-1>', self.subtraction)

        self.btn14 = Button(win, bd=1, width="20", text="0", height="3", font=("Arial", 14), bg="seashell4")
        self.btn14.grid(row=5, sticky="w", padx=5, pady=2)
        self.btn14.bind('<Button-1>', self.zero)

        self.btn15 = Button(win, bd=1, width="20", text=".", height="3", font=("Arial", 14), bg="seashell4")
        self.btn15.grid(row=5, sticky="w", padx=232, pady=2)
        self.btn15.bind('<Button-1>', self.decimal)

        self.btn16 = Button(win, bd=1, width="13", text="+", height="3", font=("Arial", 14), bg="orange")
        self.btn16.grid(row=5, sticky="w", padx=460, pady=2)
        self.btn16.bind('<Button-1>', self.addition)

        self.btn17 = Button(win, bd=1, justify="center", width="26", height="-15", text="=", font=("Arial", 28, "bold"), bg="orange")
        self.btn17.grid(sticky="nw", padx=5)
        self.btn17.bind('<Button-1>', self.result)

        # button for converter
        self.shiftbutton = Button(win, bd=1, width="20", text="Shift: Off", height="-15", bg="red", font=("Arial", 28, "bold"))
        self.shiftbutton.grid(row = 1, sticky="ne", padx=4,)
        self.shiftbutton.bind('<Button-1>', self.shift_command)
        # =======================================================================================================================
        # -Distance--------------------------------------------------------------------
        self.btc1 = Button(win, bd=1, width="13", text="m to yd", height="3", font=("Arial", 14), bg="seashell4")
        self.btc1.grid(row=2, sticky="e", padx=5, pady=2)
        self.btc1.bind('<Button-1>', self.meter_to_yard)

        self.btc2 = Button(win, bd=1, width="13", text="in to cm", height="3", font=("Arial", 14), bg="seashell4")
        self.btc2.grid(row=2, sticky="e", padx=157, pady=2)
        self.btc2.bind('<Button-1>', self.inch_to_cm)

        self.btc3 = Button(win, bd=1, width="13", text="ft to m", height="3", font=("Arial", 14), bg="seashell4")
        self.btc3.grid(row=2, sticky="e", padx=309, pady=2)
        self.btc3.bind('<Button-1>', self.feet_to_meter)

        self.btc4 = Button(win, bd=1, width="13", text="mi to km", height="3", font=("Arial", 14), bg="seashell4")
        self.btc4.grid(row=3, sticky="e", padx=5, pady=2)
        self.btc4.bind('<Button-1>', self.mile_to_km)
        # -Mass------------------------------------------------------------------------
        self.btc5 = Button(win, bd=1, width="13", text="oz to g", height="3", font=("Arial", 14), bg="seashell4")
        self.btc5.grid(row=3, sticky="e", padx=157, pady=2)
        self.btc5.bind('<Button-1>', self.oz_to_g)

        self.btc6 = Button(win, bd=1, width="13", text="lb to kg", height="3", font=("Arial", 14), bg="seashell4")
        self.btc6.grid(row=3, sticky="e", padx=309, pady=2)
        self.btc6.bind('<Button-1>', self.lb_to_kg)

        self.btc7 = Button(win, bd=1, width="13", text="t to kg", height="3", font=("Arial", 14), bg="seashell4")
        self.btc7.grid(row=4, sticky="e", padx=5, pady=2)
        self.btc7.bind('<Button-1>', self.t_to_kg)

        self.btc8 = Button(win, bd=1, width="13", text="g to kg", height="3", font=("Arial", 14), bg="seashell4")
        self.btc8.grid(row=4, sticky="e", padx=157, pady=2)
        self.btc8.bind('<Button-1>', self.g_to_kg)
        # -Time------------------------------------------------------------------------------
        self.btc9 = Button(win, bd=1, width="13", text="s to min", height="3", font=("Arial", 14), bg="seashell4")
        self.btc9.grid(row=4, sticky="e", padx=309, pady=2)
        self.btc9.bind('<Button-1>', self.sec_to_min)

        self.btc10 = Button(win, bd=1, width="13", text="min to hr", height="3", font=("Arial", 14), bg="seashell4")
        self.btc10.grid(row=5, sticky="e", padx=5, pady=2)
        self.btc10.bind('<Button-1>', self.min_to_hr)

        self.btc11 = Button(win, bd=1, width="13", text="hr to day", height="3", font=("Arial", 14), bg="seashell4")
        self.btc11.grid(row=5, sticky="e", padx=157, pady=2)
        self.btc11.bind('<Button-1>', self.hr_to_day)

        self.btc12 = Button(win, bd=1, width="13", text="day to month", height="3", font=("Arial", 14), bg="seashell4")
        self.btc12.grid(row=5, sticky="e", padx=309, pady=2)
        self.btc12.bind('<Button-1>', self.day_to_month)

        self.btc13 = Button(win, bd=1, width="26", text="month to year", height="3", font=("Arial", 14), bg="seashell4")
        self.btc13.grid(sticky="e", row=6, padx =5)
        self.btc13.bind('<Button-1>', self.month_to_year)

        # ================================================================================================================
        self.value = 0
        self.operation = 0
        self.n1 = 0
        self.n2 = 0
        self.shift = "off"

    # Function that adds a number by clicking the associated button
    def one(self, event):
        num1 = self.txt1.get()
        self.txt1.delete(0, END)
        self.txt1.insert(1, str(num1) + "1")

    def two(self, event):
        num1 = self.txt1.get()
        self.txt1.delete(0, END)
        self.txt1.insert(1, str(num1) + "2")

    def three(self, event):
        num1 = self.txt1.get()
        self.txt1.delete(0, END)
        self.txt1.insert(1, str(num1) + "3")

    def four(self, event):
        num1 = self.txt1.get()
        self.txt1.delete(0, END)
        self.txt1.insert(1, str(num1) + "4")

    def five(self, event):
        num1 = self.txt1.get()
        self.txt1.delete(0, END)
        self.txt1.insert(1, str(num1) + "5")

    def six(self, event):
        num1 = self.txt1.get()
        self.txt1.delete(0, END)
        self.txt1.insert(1, str(num1) + "6")

    def seven(self, event):
        num1 = self.txt1.get()
        self.txt1.delete(0, END)
        self.txt1.insert(1, str(num1) + "7")

    def eigth(self, event):
        num1 = self.txt1.get()
        self.txt1.delete(0, END)
        self.txt1.insert(1, str(num1) + "8")

    def nine(self, event):
        num1 = self.txt1.get()
        self.txt1.delete(0, END)
        self.txt1.insert(1, str(num1) + "9")

    def zero(self, event):
        num1 = self.txt1.get()
        self.txt1.delete(0, END)
        self.txt1.insert(1, str(num1) + "0")

    # Clear Function
    def clear(self, event):
        self.txt1.delete(0, END)
        self.n1 = 0
        self.n2 = 0
        self.operation = 0

    # Decimal Function
    def decimal(self, event):
        num1 = self.txt1.get()
        self.txt1.delete(0, END)
        self.txt1.insert(1, str(num1) + ".")

    # Arithmetic Functions
    def addition(self, event):
        self.n1 += float(self.txt1.get())
        self.txt1.delete(0, END)
        self.operation = "+"

    def subtraction(self, event):
        if self.n1 == 0:
            self.n1 = float(self.txt1.get())
            self.txt1.delete(0, END)
            self.operation = "-"
            print(self.n1)
        else:
            self.n1 -= float(self.txt1.get())
            self.txt1.delete(0, END)
            self.operation = "-"
            print(self.n1)

    def multiply(self, event):
        if self.n1 == 0:
            self.n1 = 1
            self.n1 *= float(self.txt1.get())
            self.txt1.delete(0, END)
            self.operation = "*"
        else:
            self.n1 *= float(self.txt.get())
            self.txt1.delete(0, END)
            self.operation = "*"

    def divide(self, event):
        if self.n1 == 0:
            self.n1 = float(self.txt1.get())
            self.txt1.delete(0, END)
            self.operation = "/"
        else:
            self.n1 /= float(self.txt.get())
            self.txt1.delete(0, END)
            self.operation = "/"

    def result(self, event):
        if self.operation == "+":
            n3 = 0
            self.n2 = float(self.txt1.get())
            self.txt1.delete(0, END)
            n3 = self.n1 + self.n2
            self.txt1.insert(0, float(n3))
            self.n1 = float(self.txt1.get())
        if self.operation == "-":
            n3 = 0
            self.n2 = float(self.txt1.get())
            self.txt1.delete(0, END)
            n3 = self.n1 - self.n2
            self.txt1.insert(0, float(n3))
            self.n1 = float(self.txt1.get())
        if self.operation == "*":
            n3 = 0
            self.n2 = float(self.txt1.get())
            self.txt1.delete(0, END)
            n3 = self.n1 * self.n2
            self.txt1.insert(0, float(n3))
            self.n1 = float(self.txt1.get())
        if self.operation == "/":
            n3 = 0
            self.n2 = float(self.txt1.get())
            self.txt1.delete(0, END)
            n3 = self.n1 / self.n2
            self.txt1.insert(0, float(n3))
            self.n1 = float(self.txt1.get())

        self.n1 = 0

    # def for converter
    def shift_command(self, event):
        if self.shift == "off":
            self.shift = "on"
            self.shiftbutton.configure(text="Shift: On", bg="green")
            self.btc1.configure(text="yd to m")
            self.btc2.configure(text="cm to in")
            self.btc3.configure(text="m to ft")
            self.btc4.configure(text="km to mi")
            self.btc5.configure(text="g to oz")
            self.btc6.configure(text="kg to lb")
            self.btc7.configure(text="kg to t")
            self.btc8.configure(text="kg to g")
            self.btc9.configure(text="min to s")
            self.btc10.configure(text="hr to min")
            self.btc11.configure(text="day to hr")
            self.btc12.configure(text="month to day")
            self.btc13.configure(text="year to month")


        else:
            self.shift = "off"
            self.shiftbutton.configure(text="Shift: Off", bg="red")
            self.btc1.configure(text="m to yd")
            self.btc2.configure(text="in to cm")
            self.btc3.configure(text="ft to m")
            self.btc4.configure(text="mi to km")
            self.btc5.configure(text="oz to g")
            self.btc6.configure(text="lb to kg")
            self.btc7.configure(text="t to kg")
            self.btc8.configure(text="g to kg")
            self.btc9.configure(text="s to min")
            self.btc10.configure(text="min to hr")
            self.btc11.configure(text="hr to day")
            self.btc12.configure(text="day to month")
            self.btc13.configure(text="month to year")

    # ====Function for Distance Conversion===================================================================================================================
    def meter_to_yard(self, event):
        if self.shift == "off":
            # Get the value in the input field
            value = self.txt1.get()
            # Convert the value from meters to yards
            yards = float(value) * 1.09361
            # Set the input field to display the converted value
            self.txt1.delete(0, END)
            self.txt1.insert(0, round(yards, 5))
        else:
            value = self.txt1.get()
            meters = float(value) / 1.09361
            self.txt1.delete(0, END)
            self.txt1.insert(0, round(meters, 5))

    def inch_to_cm(self, event):
        if self.shift == "off":
            value = self.txt1.get()
            cm = float(value) * 2.54
            self.txt1.delete(0, END)
            self.txt1.insert(0, round(cm, 5))
        else:
            value = self.txt1.get()
            inch = float(value) / 2.54
            self.txt1.delete(0, END)
            self.txt1.insert(0, round(inch, 5))

    def feet_to_meter(self, event):
        if self.shift == "off":
            value = self.txt1.get()
            meters = float(value) * 0.3048
            self.txt1.delete(0, END)
            self.txt1.insert(0, round(meters, 5))
        else:
            value = self.txt1.get()
            feet = float(value) / 0.3048
            self.txt1.delete(0, END)
            self.txt1.insert(0, round(feet, 5))

    def mile_to_km(self, event):
        if self.shift == "off":
            value = self.txt1.get()
            km = float(value) * 1.60934
            self.txt1.delete(0, END)
            self.txt1.insert(0, round(km, 5))
            print(km)
        else:
            value = self.txt1.get()
            mile = float(value) / 1.60934
            self.txt1.delete(0, END)
            self.txt1.insert(0, round(mile, 5))

    # ====Function for Mass Conversion===================================================================================================================
    def oz_to_g(self, event):
        if self.shift == "off":
            value = self.txt1.get()
            g = float(value) * 28.35
            self.txt1.delete(0, END)
            self.txt1.insert(0, round(g, 5))

    def lb_to_kg(self, event):
        if self.shift == "off":
            value = self.txt1.get()
            kg = float(value) * 0.45359237
            self.txt1.delete(0, END)
            self.txt1.insert(0, round(kg, 5))

    def t_to_kg(self, event):
        if self.shift == "off":
            value = self.txt1.get()
            kg = float(value) * 1000
            self.txt1.delete(0, END)
            self.txt1.insert(0, round(kg, 5))

    def g_to_kg(self, event):
        if self.shift == "off":
            value = self.txt1.get()
            kg = float(value) * 0.001
            self.txt1.delete(0, END)
            self.txt1.insert(0, round(kg, 5))
        else:
            value = self.txt1.get()
            g = float(value) / 0.001
            self.txt1.delete(0, END)
            self.txt1.insert(0, round(g, 5))

    # ========================================================================================================================
    def sec_to_min(self, event):
        if self.shift == "off":
            value = self.txt1.get()
            sec = float(value) * 60
            self.txt1.delete(0, END)
            self.txt1.insert(0, round(sec, 5))
        else:
            value = self.txt1.get()
            min = float(value) / 60
            self.txt1.delete(0, END)
            self.txt1.insert(0, round(min, 5))

    def min_to_hr(self, event):
        if self.shift == "off":
            value = self.txt1.get()
            hr = float(value) / 60
            self.txt1.delete(0, END)
            self.txt1.insert(0, round(hr, 5))
        else:
            value = self.txt1.get()
            min = float(value) * 60
            self.txt1.delete(0, END)
            self.txt1.insert(0, round(min, 5))

    def hr_to_day(self, event):
        if self.shift == "off":
            value = self.txt1.get()
            day = float(value) / 24
            self.txt1.delete(0, END)
            self.txt1.insert(0, round(day, 5))
        else:
            value = self.txt1.get()
            hr = float(value) * 24
            self.txt1.delete(0, END)
            self.txt1.insert(0, round(hr, 5))

    def day_to_month(self, event):
        if self.shift == "off":
            value = self.txt1.get()
            month = float(value) / 30.44
            self.txt1.delete(0, END)
            self.txt1.insert(0, round(month, 5))
        else:
            value = self.txt1.get()
            day = float(value) * 30.44
            self.txt1.delete(0, END)
            self.txt1.insert(0, round(day, 5))

    def month_to_year(self, event):
        if self.shift == "off":
            value = self.txt1.get()
            year = float(value) / 12
            self.txt1.delete(0, END)
            self.txt1.insert(0, round(year, 5))
        else:
            value = self.txt1.get()
            month = float(value) * 12
            self.txt1.delete(0, END)
            self.txt1.insert(0, round(month, 5))


mywin = UnitConverter(window)
window.mainloop()