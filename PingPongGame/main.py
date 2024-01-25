from tkinter import *

def onClick():


window = Tk()
window.title = "Mile to km converter"
window.config(padx=20, pady=20)


miles_label = Label(text="miles")
miles_input = Entry(width=7)
miles_input.grid(column=1, row=0)

km_label = Label(text="km")
is_equal_to = Label(text="is equal to")

cal_btn = Button("Calculate", command=onClick)



window.mainloop()

