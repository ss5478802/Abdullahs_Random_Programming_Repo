from tkinter import *
import pyperclip

app = Tk()
fg = "white"
bg = "black"
def change_bg(label, label2):
    global fg, bg
    if label.get(1.0, END).replace("\n", "") == "":
        fg, bg = bg, fg
        label2.config(fg=fg, bg=bg)
    else:
        try:
            fg, bg = label.get(1.0, END).split(", ")
            bg = bg.replace("\n", "")
            label2.config(fg=fg, bg=bg)
            label.delete(1.0, END)
        except:
            label.delete(1.0, END)


greeting = Label(text="Hello, World!", bg="black", fg="white")
greeting.pack()
fore = Text(height=10)
fore.pack()
changeBg = Button(text="Click me!", command=lambda: change_bg(fore, greeting))
changeBg.pack()
app.mainloop()
