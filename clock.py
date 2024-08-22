import tkinter as tk
from time import strftime

root = tk.Tk()
root.title("Digital Clock")

def time():
    current_time = strftime('%H:%M:%S')
    current_date1 = strftime('%D')
    current_date2 = strftime('%d %B %Y')
    
    display_text = f"{current_time}\n{current_date1}\n{current_date2}"
    label.config(text=display_text)
    
    label.after(1000, time)

label = tk.Label(root, font=('calibri', 40, 'bold'), background='yellow', foreground='black')
label.pack(anchor='center')

time()
root.mainloop()

