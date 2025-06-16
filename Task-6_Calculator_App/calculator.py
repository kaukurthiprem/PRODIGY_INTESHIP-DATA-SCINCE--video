import tkinter as tk

def click(btn):
    current = entry.get()
    entry.delete(0, tk.END)
    entry.insert(0, current + str(btn))

def calculate():
    try:
        result = eval(entry.get())
        entry.delete(0, tk.END)
        entry.insert(0, str(result))
    except:
        entry.delete(0, tk.END)
        entry.insert(0, "Error")

def clear():
    entry.delete(0, tk.END)

root = tk.Tk()
root.title("Calculator")
entry = tk.Entry(root, width=16, font=("Arial", 18))
entry.grid(row=0, column=0, columnspan=4)
buttons = [
    ('7','8','9','/'),
    ('4','5','6','*'),
    ('1','2','3','-'),
    ('0','.','=','+')
]
for r, row in enumerate(buttons):
    for c, char in enumerate(row):
        action = lambda ch=char: calculate() if ch=='=' else click(ch)
        tk.Button(root, text=char, width=5, command=action).grid(row=r+1, column=c)
tk.Button(root, text='C', command=clear).grid(row=5, column=0, columnspan=4, sticky='we')
root.mainloop()