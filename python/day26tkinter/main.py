from tkinter import *

#creating new window
window = Tk()
window.title("widget example")
window.minsize(width=500, height=500)

#labels
label = Label(text="this is old text")
label.config(text="this is new text")
label.pack()

#buttons
def action():
    print("Do something")

button = Button(text='click me', command=action)
button.pack()

# entry
entry = Entry(width=30)
entry.insert(END, string="some text to begin with")
print(entry.get())
entry.pack()

#text
text = Text(height=5, width=30)
text.focus()
text.insert(END, "Example of multiline text entry")
print(text.get("1.0", END))
text.pack()


#spin box
def spinbox_used():
    print(spinbox.get())
spinbox = Spinbox(from_=0, to=10, width=10, command=spinbox_used)
spinbox.pack()

#scale 
def scale_used(value):
    print(value)
scale = Scale(from_=0, to=100, command=scale_used)
scale.pack()

window.mainloop()