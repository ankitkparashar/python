import tkinter

window = tkinter.Tk()
window.title("My First GUI program")
window.minsize(width=500, height=300)
window.config(padx=20, pady=20)

# Label
my_label = tkinter.Label(text="I am a label", font=("Arial", 24, "bold"))
my_label.pack()
my_label.config(text="New text")
my_label.grid(column=0, row=0)


# Button
def button_clicked():
    my_label["text"] = input.get()


button = tkinter.Button(text="Click Here", command=button_clicked)
button.grid(column=1, row=1)
button_2 = tkinter.Button(text="New Button", command=button_clicked)
button_2.grid(column=2, row=0)

# Entry
input = tkinter.Entry(width=10)
input.grid(column=3, row=2)


window.mainloop()
