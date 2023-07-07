from tkinter import *

window = Tk()
window.title("Mile to Km Converter")
window.config(padx = 20, pady = 20)

input = Entry()
input.grid(column = 1, row = 0)

label = Label()
label.config(text="Miles")
label.grid(column = 2, row = 0)

label_1= Label()
label_1.config(text = "Is equal to")
label_1.grid(column = 0, row = 2)

label_2 = Label()
label_2.config(text = "0")
label_2.grid(column = 1, row = 2)

label_3 = Label()
label_3.config(text = "Km")
label_3.grid(column = 2, row = 2)

def calculate():
    miles = float(input.get())
    conversion = miles * 1.609344
    kilometer = (round(conversion,2))
    label_2.config(text = kilometer)

button = Button(text = "Calculate", command = calculate)
button.grid(column = 1, row = 3)


window.mainloop()