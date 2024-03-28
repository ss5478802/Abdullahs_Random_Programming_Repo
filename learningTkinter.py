# Learning tkinter
from tkinter import *
#import pyperclip

# Everything in tkinter is a widget (like a block)
# app is the main (biggest) block. Inside this we will add smaller widget (blocks)
app = Tk()

# Defines the default dimension of the main block (widget). So the window can be resized by the user later.
app.geometry("300x50")

# This is a label. This displays the text "Hello, World". This label is like a small block in the main window.
myLabel = Label(app, text="Hello, World!")

# This puts (pushes) the small block into the main window.
myLabel.pack()

# This starts the app and cause the app to run indefinetely until the user exits the app
app.mainloop()
