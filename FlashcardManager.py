import json
import random

class FlashcardManager:
    def __init__(self):
        self.flashcards = []
        self.current_index = 0

    def load_flashcards(self, filename):
        with open(filename, 'r') as file:
            flashcards_data = json.load(file)
        self.flashcards = flashcards_data['flashcards']
        self.current_index = 0

    def get_current_flashcard(self):
        if not self.flashcards:
            return None
        return self.flashcards[self.current_index]

    def get_flashcard_count(self):
        return len(self.flashcards)

    def move_to_next_flashcard(self):
        if self.current_index < len(self.flashcards) - 1:
            self.current_index += 1
            return True
        return False

    def move_to_previous_flashcard(self):
        if self.current_index > 0:
            self.current_index -= 1
            return True
        return False
