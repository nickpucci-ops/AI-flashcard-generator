import tkinter as tk
from generator import generate_flashcard

win = tk.Tk() #init tk window
win.title("Llama flashcard generator")
win.geometry("400x300")

topic_label = tk.Label(win, text="Ask for a definition")
topic_label.pack()

topic_entry = tk.Entry(win, width=40)
topic_entry.pack()

flashcard_label = tk.Label(win, text="Flashcard", font=("Arial", 12, "bold"))
flashcard_label.pack()

definition_text = tk.Label(win, text="", wraplength=350, justify="left")
definition_text.pack()

def create():
    """
    Method for getting and generating definition in tkinter window. User types question, then clicks generate.
    Returns definition in flashcard format
    """
    user_input = topic_entry.get()
    if not user_input.strip():
        definition_text.config(text="Please enter a topic")
        return
    
    definition_text.config(text="Generating...")
    win.update_idletasks()

    response = generate_flashcard(user_input)
    flashcard_text = f"Topic: {user_input}\nDefinition: {response}"
    definition_text.config(text=flashcard_text)

    #store response into card
    #store card
    
b = tk.Button(
        win,
        text='Generate',
        command=create
)
b.pack()

win.mainloop()

