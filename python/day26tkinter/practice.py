import tkinter as tk

window = tk.Tk()

window.title("GUI programs")
window.minsize(width=500, height=300)


#entry
input = tk.Entry()
input.pack()

#label
label = tk.Label(text="Hello world", font=("Arial", 24, "bold"))
label.pack()

#button
def button_clicked():
    new_text = input.get()
    label.config(text = new_text)

button = tk.Button(text = "Click me", command=button_clicked)
button.pack()






window.mainloop()


#**************args**************

# def fun(*args):
#     sum = 0
#     for n in args:
#         sum += n
#     print(sum)

# fun(2,3,4,5,3,7,9)

#**************kwarsgs************

# def cal(**kwargs):
#     print(kwargs)
#     print(kwargs["add"])


# cal(add=3, multi=4)

# class Car:
#     def __init__(self, **kw):
#         self.make = kw.get("make")
#         self.model = kw.get("model")
#         self.color = kw.get("color")

# car = Car(make = "nisan")
# print(car.make)