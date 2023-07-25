import json
import random
import tkinter as tk
from tkinter import filedialog, messagebox

def load_flashcards(filename):
    with open(filename, 'r') as file:
        flashcards_data = json.load(file)
    return flashcards_data['flashcards']

def show_flashcard(index):
    global flashcards, question_label, answer_label
    if not flashcards:
        messagebox.showinfo("Flashcard Studying Tool", "No flashcards loaded. Please load a JSON file.")
        return

    card = flashcards[index]
    question = card['question']
    answer = card['answer']

    question_label.config(text=f"Question: {question}")
    answer_label.config(text="")
    
    def reveal_answer():
        answer_label.config(text=f"Answer: {answer}")
        
    reveal_button.config(command=reveal_answer)

def open_file():
    global flashcards, current_index
    file_path = filedialog.askopenfilename(filetypes=[("JSON Files", "*.json")])
    if file_path:
        try:
            flashcards = load_flashcards(file_path)
            current_index = 0
            show_flashcard(current_index)
        except FileNotFoundError:
            messagebox.showinfo("Flashcard Studying Tool", "Flashcards file not found. Please select a valid 'json' file.")
        except json.JSONDecodeError:
            messagebox.showinfo("Flashcard Studying Tool", "Invalid JSON format. Please select a valid 'json' file.")

def next_flashcard():
    global current_index
    if flashcards and current_index < len(flashcards) - 1:
        current_index += 1
        show_flashcard(current_index)

def previous_flashcard():
    global current_index
    if flashcards and current_index > 0:
        current_index -= 1
        show_flashcard(current_index)

def main():
    global flashcards, question_label, answer_label, reveal_button, current_index

    flashcards = []
    current_index = 0

    root = tk.Tk()
    root.title("Flashcard Studying Tool")

    menu_bar = tk.Menu(root)
    root.config(menu=menu_bar)

    file_menu = tk.Menu(menu_bar, tearoff=0)
    menu_bar.add_cascade(label="File", menu=file_menu)
    file_menu.add_command(label="Open JSON File", command=open_file)
    file_menu.add_separator()
    file_menu.add_command(label="Exit", command=root.destroy)

    question_label = tk.Label(root, text="Press 'File' -> 'Open JSON File' to load flashcards.")
    question_label.pack(pady=20)

    answer_label = tk.Label(root, text="")
    answer_label.pack(pady=20)

    reveal_button = tk.Button(root, text="Show Card")
    reveal_button.pack()

    previous_button = tk.Button(root, text="Previous", command=previous_flashcard)
    previous_button.pack(side=tk.LEFT, padx=10)

    next_button = tk.Button(root, text="Next", command=next_flashcard)
    next_button.pack(side=tk.RIGHT, padx=10)
    
    root.mainloop()

if __name__ == "__main__":
    main()
