from tkinter import *

window = Tk()
window.geometry('400x400')

text_canvas = None

def wait(event):
    global text_canvas
    if text_canvas is not None:
        window.after_cancel(text_canvas)

    text_canvas = window.after(5000, clear_text)

def clear_text():
    text_entry.delete('1.0','end')

text_entry = Text(window,font=('Times New Roman',12))
text_entry.tag_config('top_left',justify="left")
text_entry.pack()
text_entry.bind('<Key>',wait)
window.mainloop()

