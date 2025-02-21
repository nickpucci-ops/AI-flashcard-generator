import tkinter as tk
from generator import generate_flashcard

def window():
    win = tk.Tk()
    win.title("Llama flashcard generator")
    return win

def create():
    response = generate_flashcard()
    


win.geometry("400x200")
b = tk.Button(
        win,
        text='Generate',
        command=create
)
