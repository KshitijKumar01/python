from tkinter import *


def miles_to_km():
    miles = float(miles_input.get())
    km = round(miles * 1.689)
    km_result_label.config(text= str(km))

window = Tk()
window.title("Miles to kilimeter converter")
window.minsize(width=180, height=100)
window.config(padx=10, pady=10)

miles_input = Entry(width=10)
miles_input.grid(column=1, row=0)

miles_label = Label(text='Miles')
miles_label.grid(column=2, row=0)

is_equal_to_label = Label(text="is equal to")
is_equal_to_label.grid(column=0, row=1)

km_result_label = Label(text="0")
km_result_label.grid(column=1, row=1)

km_label = Label(text="km")
km_label.grid(column=2, row=1)

calculate_button = Button(text="calculate", command=miles_to_km)
calculate_button.grid(column=1, row=2)




window.mainloop()
