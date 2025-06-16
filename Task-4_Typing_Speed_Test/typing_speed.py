import tkinter as tk
from time import time

def start_timer(event):
    global start_time
    entry.delete(0, tk.END)
    start_time = time()

def calculate_speed(event):
    end_time = time()
    typed_text = entry.get()
    elapsed_time = end_time - start_time
    word_count = len(typed_text.split())
    wpm = word_count / (elapsed_time / 60)
    result.config(text=f"Speed: {wpm:.2f} WPM")

root = tk.Tk()
root.title("Typing Speed Test")
sample_text = "Type this sentence as fast as you can."
tk.Label(root, text=sample_text).pack()
entry = tk.Entry(root, width=50)
entry.pack()
entry.bind("<FocusIn>", start_timer)
entry.bind("<Return>", calculate_speed)
result = tk.Label(root, text="")
result.pack()
root.mainloop()