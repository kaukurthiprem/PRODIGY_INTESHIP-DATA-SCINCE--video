from tkinter import Label, Tk
import time

root = Tk()
root.title("Digital Clock")
root.geometry("250x100")
label = Label(root, font=("Arial", 40), background="black", foreground="cyan")
label.pack(anchor='center')

def update_time():
    current_time = time.strftime("%H:%M:%S")
    label.config(text=current_time)
    label.after(1000, update_time)

update_time()
root.mainloop()