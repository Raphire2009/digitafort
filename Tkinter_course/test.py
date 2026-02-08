


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

