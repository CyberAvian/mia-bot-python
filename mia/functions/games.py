import random
import tkinter as tk
from tkinter import ttk

from mia.core.gui import Gui


class Games(Gui):
    def __init__(self, window_title):
        super().__init__(window_title)
        self.round = 1
        self.score = 0
        self.first_number = 0
        self.second_number = 0

    def start(self):
        self.create_widgets([self.create_higher_button, self.create_lower_button, self.create_quit_button])
        self.display_rules()
        self.start_round()
        self.mainloop()

    def create_mainframe(self):
        self.mainframe = ttk.Frame(self, padding='10')
        self.mainframe.grid(column=0, row=0, sticky='NSEW')
        self.mainframe.grid_columnconfigure((0, 1, 2), weight=1)
        self.mainframe.grid_rowconfigure(0, weight=1)

    def create_higher_button(self):
        self.higher = ttk.Button(self.mainframe, text='Higher', command=lambda: self.play_round('higher'))
        self.higher.grid(column=0, row=1, sticky='NSEW', padx=5)

    def create_lower_button(self):
        self.lower = ttk.Button(self.mainframe, text='Lower', command=lambda: self.play_round('lower'))
        self.lower.grid(column=1, row=1, sticky='NSEW', padx=5)

    def create_quit_button(self):
        self.quit = ttk.Button(self.mainframe, text='Quit', command=self.destroy)
        self.quit.grid(column=2, row=1, sticky='NSEW', padx=5)

    def display_rules(self):
        header = 'Rules:'
        rules = 'A number will be displayed. ' \
                'Guess whether that next number will be higher or lower than the displayed number. '\
                'Numbers range from 0 to 100\n\n'
        message = f"{header}\n\t{rules}"
        self.update_textbox(message, trim_newline=False)

    def start_round(self):
        self.first_number = random.randint(0,100)
        self.second_number = random.randint(0,100)
        while (self.second_number == self.first_number):
            self.second_number = random.randint(0,100)

        self.update_textbox(f"Round {self.round}:")
        self.update_textbox(f"First Number: {self.first_number}", indent=True)

    def play_round(self, guess: tk.Event):
        self.update_textbox(f"Second Number: {self.second_number}", indent=True)
        self.update_textbox(f"Guess: {guess.capitalize()}", indent=True)

        correct_answer = 'higher' if self.first_number < self.second_number else 'lower'
        result = True if guess == correct_answer else False
        self.score_round(result)

    def score_round(self, round_result: bool):
        if (round_result):
            self.score += 1
            message = "Correct!"
        else:
            message = "Incorrect!"
        self.round += 1
        self.update_textbox(message)
        self.update_textbox(f"Score: {self.score}\n\n", trim_newline=False)
        self.start_round()


if __name__=='__main__':
    root = Games('Hi Lo')
    root.start()
