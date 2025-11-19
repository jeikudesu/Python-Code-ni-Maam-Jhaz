# TKINTER WIDGETS
import tkinter as tk

window = tk.Tk()
window.title("Simple Tkinter Form")
window.geometry("300x200")

label = tk.Label(window, text="Enter your username:")
label.pack()

entry = tk.Entry(window)
entry.pack()

def submit():
    print("Submitted:", entry.get())

button = tk.Button(window, text="Submit", command=submit)
button.pack()

window.mainloop()
