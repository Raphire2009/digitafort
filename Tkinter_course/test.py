

#label = tk.Label(root, text="Hello ")
#label.pack()

"""
def on_click_button():
    print('Button is working ')

button = tk.Button(root, text="click me", command=on_click_button)
button.pack()

entry = tk.Entry(root, width=30)
entry.pack()

text = tk.Text(root, height=50, width=30)
text.pack()
"""

#frame = tk.Frame(root, borderwidth=4, relief="groove")
#frame.pack(padx=30, pady=50)
#frame_label = tk.Label(frame, text="victor  kdddddddddddddddddddddddddddddkdkdddddddddddddddddddddd")
#frame_label.pack()

#add intvar 
#var = tk.StringVar()
#radiobutton1 = tk.Radiobutton(root, text="Option A", variable=var, value="A")
#radiobutton2 = tk.Radiobutton(root, text="Option B", variable=var, value="B")
#radiobutton1.pack()
#radiobutton2.pack()

#scale = tk.Scale(root, from_=0, to=100, orient=tk.HORIZONTAL)
#scale.pack()
#list = tk.Listbox(root)
#list.insert(tk.END, "Item 1")
#list.insert(tk.END, "Item 2")
#list.pack()


"""
import tkinter as tk
from  tkinter import messagebox
from tkinter import filedialog
root = tk.Tk()

root.title(" Your App")
root.geometry("400x300")
root.withdraw

def open_file():
    filePath = filedialog.askopenfilename(
        title="open a file ", 
        filetypes=(("test file", "*.md"), ("all file", "*.")))
    if filePath:
        print(f"selected file Path:{filePath}")

open_file()
root.destroy()





class Myapp:
    
    def __init__(self, master):
        self.master = master 
        master.title("My App")
        
        self.label = tk.Label(master, text="Hello World")
        self.label.pack(pady=10)

        self.greet_button = tk.Button(master, text="Greet", command=self.greet)
        self.greet_button.pack()

        self.close_button = tk.Button(master, text="Close", command=master.quit)
        self.close_button.pack()
    
    def greet(self):
        self.label.config(text="Greeting")

"""


import tkinter as tk
from tkinter import messagebox
import sqlite3


# the page framework
root = tk.Tk()
root.title("temperature converter ")
root.geometry("300x150")




#1. c
# 2. f

def convert_temperature():
    c_text  = c_entry.get()
    f_text = f_entry.get()

    try:
        if c_text:
            c_value = float(c_text)
            f_result = (c_value * 9/5) + 32

            f_entry.delete(0,tk.END)
            f_entry.insert(0, f"{f_result:.2f}")
        elif f_text:
            f_value = float(f_text)
            c_result = (f_value -32) * 5/9

            c_entry.delete(0,tk.END)
            c_entry.insert(0, f"{c_result:.2f}")
        else:
            messagebox.showwarning()
    except ValueError:
        messagebox.showerror("Input Error", "Invalid temp")



#
def clear_temp():
    c_entry.delete(0, tk.END)
    f_entry.delete(0, tk.END)





#adding the widgets
c_label  = tk.Label(root,text="celsuis:")
c_entry = tk.Entry(root,width=20)

f_label = tk.Label(root,text="F :")
f_entry = tk.Entry(root, width=20)


c_temp_b = tk.Button(root, text="Convert", command=convert_temperature)
clear_temp_b = tk.Button(root, text="Clear", command=clear_temp)



#arrange the widgets
c_label.grid(row=0, column=0, padx=10, pady=5, sticky="w")
c_entry.grid(row=0, column=1, padx=10, pady=5)


f_label.grid(row=1, column=0, padx=10, pady=5, sticky="w")
f_entry.grid(row=1, column=1, padx=10, pady=5)

c_temp_b.grid(row=2, column=0, padx=2, pady=10)
clear_temp_b.grid(row=3, columnspan=1, pady=5)


root.mainloop()


