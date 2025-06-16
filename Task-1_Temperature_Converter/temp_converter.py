import tkinter as tk
from tkinter import messagebox

def convert():
    try:
        temp = float(entry.get())
        if var.get() == 1:
            result = (temp * 9/5) + 32
            output.config(text=f"{result:.2f} °F")
        else:
            result = (temp - 32) * 5/9
            output.config(text=f"{result:.2f} °C")
    except ValueError:
        messagebox.showerror("Invalid input", "Please enter a number")

root = tk.Tk()
root.title("Temperature Converter")
entry = tk.Entry(root)
entry.pack(pady=10)
var = tk.IntVar(value=1)
tk.Radiobutton(root, text="Celsius to Fahrenheit", variable=var, value=1).pack()
tk.Radiobutton(root, text="Fahrenheit to Celsius", variable=var, value=2).pack()
tk.Button(root, text="Convert", command=convert).pack(pady=10)
output = tk.Label(root, text="")
output.pack()
root.mainloop()