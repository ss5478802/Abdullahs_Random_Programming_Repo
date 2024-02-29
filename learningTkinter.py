from tkinter import *

app = Tk()
fg = "white"
bg = "black"
def change_bg(label):
    global fg, bg
    label.config(bg=fg, fg=bg)
    fg, bg = bg, fg
greeting = Label(text="Hello, World!", bg="black", fg="white")
greeting.pack()
changeBg = Button(text="Click me!", command=lambda: change_bg(greeting))
changeBg.pack()
app.mainloop()
