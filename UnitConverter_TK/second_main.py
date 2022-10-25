from tkinter import *

def add(*args):
    sum = 0
    for n in args:
        sum += n
    return sum

def button_click():
    my_label.config(text = input_field.get())

#window
window = Tk()
window.title("Learning tkinter class")
window.minsize(width=600, height=300)

#label
my_label = Label(text="I am a lable")
my_label.grid(column=0, row=0)

#button
button = Button(text="click me",command=button_click)
button.grid(column=1, row=1)
button_new = Button(text="New Button",command=button_click)
button_new.grid(column=2, row=0)

#entry
input_field = Entry()
input_field.grid(column=2, row=2)

amit = 0

print(add(1, 5, 7, 8, 5,3))

window.mainloop()