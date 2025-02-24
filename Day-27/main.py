from tkinter import *

FONT = ("Calibria", 24, "normal")
PADDING = 10


window = Tk()
window.title("Mile to Kilometer Converter")
window.minsize(width=300, height=200)
window.config(padx=50, pady=50)

equal_to = Label(text="is equal to", font=FONT, padx=20)
equal_to.grid(column=0, row=1)

init_unit = Label(text="Miles", font=FONT)
init_unit.grid(column=2, row=0)

final_unit = Label(text="Km", font=FONT)
final_unit.grid(column=2, row=1)

answer = Label(text="0", font=FONT, padx=PADDING, pady=PADDING)
answer.grid(column=1, row=1)


def miles_to_kilometers():
    miles = float(input_v.get())
    kilo = miles * 1.60934
    answer.config(text=f"{kilo}")


button = Button(text="Calculate", command=miles_to_kilometers, font=FONT, cursor="hand2")
button.grid(column=1, row=2)

input_v = Entry(width=10, font=FONT, cursor="xterm")
input_v.insert(END, string="0")
input_v.grid(column=1, row=0)

window.mainloop()
