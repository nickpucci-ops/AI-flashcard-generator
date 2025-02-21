import tkinter as tk
from generator import generate_flashcard

win = tk.Tk()
win.title("Llama flashcard generator")

def create():
    response = generate_flashcard()
    #store response into card
    #store card
    
win.geometry("400x200")
b = tk.Button(
        win,
        text='Generate',
        command=create
)
b.pack()

win.mainloop()

