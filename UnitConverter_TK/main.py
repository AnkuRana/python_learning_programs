from tkinter import *


def convert_to_km():
    value = float(input_field.get())
    value = round(value * 1.6, 2)
    result_label.config(text=value)


window = Tk()
window.title("Convert Miles to Kilometres")
window.minsize(width=300, height=150)
window.config(padx=40, pady=40)

# Text Field Entry
input_field = Entry()
input_field.grid(column=1, row=1)
input_field.insert(END, string="0")

# Label
miles_label = Label(text="miles")
miles_label.grid(column=2, row=1)

# label 2
info_label = Label(text="is equal to")
info_label.grid(column=0, row=2)

# label 3
result_label = Label(text="0")
result_label.grid(column=1, row=2)

# label 4
km_label = Label(text="Km")
km_label.grid(column=2, row=2)

# label 5
title_label = Label(text="Convert Miles to Kms", font="bold")
title_label.grid(column=1, row=0)

# Button
calculate = Button(text="Calculate", command=convert_to_km)
calculate.grid(column=1, row=3)


window.mainloop()
