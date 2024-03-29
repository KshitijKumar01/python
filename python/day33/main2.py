from tkinter import *
import requests


def get_quote():
    response = requests.get(url="https://api.kanye.rest")
    data = response.json()
    s = data["quote"]
    canvas.itemconfig(quote_text, text=s)

path_background = "C:\\Users\\acer\\Desktop\\CHANDIGARH UNIVERSITY\\AI ML\\python\\day33\\background.png"

path_kanye = "C:\\Users\\acer\\Desktop\\CHANDIGARH UNIVERSITY\\AI ML\\python\\day33\\kanye.png"

window = Tk()
window.title("Kanye Says...")
window.config(padx=50, pady=50)

canvas = Canvas(width=300, height=414)
background_img = PhotoImage(file=path_background)
canvas.create_image(150, 207, image=background_img)
quote_text = canvas.create_text(150, 207, text="Kanye quotes goes here!!!", width=250, font=("Arial", 30, "bold"), fill="white")
canvas.grid(row=0, column=0)

kanye_img = PhotoImage(file=path_kanye)
kanye_button = Button(image=kanye_img, highlightthickness=0, command=get_quote)
kanye_button.grid(row=1, column=0)



window.mainloop()