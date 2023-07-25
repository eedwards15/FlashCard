import json
import tkinter as tk
from tkinter import filedialog, messagebox
from FlashcardManager import FlashcardManager

def show_flashcard():
    card = flashcard_manager.get_current_flashcard()
    if not card:
        messagebox.showinfo("Flashcard Studying Tool", "No flashcards loaded. Please load a JSON file.")
        return

    question = card['question']
    answer = card['answer']

    question_label.config(text=f"Question: {question}")
    answer_label.config(text="")
    
    def reveal_answer():
        answer_label.config(text=f"Answer: {answer}")
        
    reveal_button.config(command=reveal_answer)

def open_file():
    file_path = filedialog.askopenfilename(filetypes=[("JSON Files", "*.json")])
    if file_path:
        try:
            flashcard_manager.load_flashcards(file_path)
            show_flashcard()
        except FileNotFoundError:
            messagebox.showinfo("Flashcard Studying Tool", "Flashcards file not found. Please select a valid 'json' file.")
        except json.JSONDecodeError:
            messagebox.showinfo("Flashcard Studying Tool", "Invalid JSON format. Please select a valid 'json' file.")

def next_flashcard():
    if flashcard_manager.move_to_next_flashcard():
        show_flashcard()

def previous_flashcard():
    if flashcard_manager.move_to_previous_flashcard():
        show_flashcard()

def main():
    global question_label, answer_label, reveal_button, flashcard_manager

    flashcard_manager = FlashcardManager()

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
