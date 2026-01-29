
import tkinter as tk


root = tk.Tk()


root.title(" Your App")

##menu = tk.Menu(root)

root.geometry("400x300")

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

frame = tk.Frame(root, borderwidth=4, relief="groove")
frame.pack(padx=30, pady=50)
frame_label = tk.Label(frame, text="victor  kdddddddddddddddddddddddddddddkdkdddddddddddddddddddddd")
frame_label.pack()





root.mainloop()







