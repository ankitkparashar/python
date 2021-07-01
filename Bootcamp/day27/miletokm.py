import tkinter

window = tkinter.Tk()
window.title("Mile to Km Converter")
window.minsize(width=200, height=100)
window.config(padx=20, pady=20)

# Input
input_miles = tkinter.Entry(width=10)
input_miles.grid(column=1, row=0)

# Labels
label_1 = tkinter.Label(text="Miles", font=("Arial", 12))
label_1.grid(column=2, row=0)

label_2 = tkinter.Label(text="is equal to", font=("Arial", 12))
label_2.grid(column=0, row=1)

label_3 = tkinter.Label(text="Km", font=("Arial", 12))
label_3.grid(column=2, row=1)

label_4 = tkinter.Label(text="0", font=("Arial", 12))
label_4.grid(column=1, row=1)


# Button
def calculate_miles():
    label_4["text"] = int(input_miles.get()) * 1.609


button = tkinter.Button(text="Calculate", command=calculate_miles)
button.grid(column=1, row=2)

window.mainloop()
