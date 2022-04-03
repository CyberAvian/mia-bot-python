import tkinter as tk
from tkinter import ttk

from mia.core.bot import Bot
from mia.core.gui import Gui
from mia.functions.search import Search
from mia.functions.games import Games

class Mia(Gui):
    def __init__(self):
        super().__init__('Mia')
        self.mic_on_icon = tk.PhotoImage(file='mia\\assets\\microphone-on.png')
        self.mic_off_icon = tk.PhotoImage(file='mia\\assets\\microphone-off.png')
        self.brain = Bot(1)
        self.search_engine = Search
        self.games_list = ['high low']

    def start(self):
        self.create_widgets([self.create_text_input, self.create_mic_input, self.create_submit])
        self.bind_keys()
        self.display_help()
        self.mainloop()

    def create_text_input(self):
        # Set up Text Input Widget
        self.text_input = ttk.Entry(self.mainframe, background='lightgrey', font=('Arial 16'))
        self.text_input.grid(column=0, row=1, sticky='SEW')
        self.text_input.focus_set()

    def create_mic_input(self):
        # Create Microphone Icon to capture microphone input
        self.mic_input = ttk.Button(self.mainframe, image=self.mic_off_icon, command=self.get_mic_input)
        self.mic_input.grid(column=1, row=1, sticky='NSEW', padx=5)

    def create_submit(self):
        # Submit button
        self.submit = ttk.Button(self.mainframe, text='Submit', command=self.get_text_input)
        self.submit.grid(column=2, row=1, sticky='NSEW', padx=5)

    def bind_keys(self):
        self.bind('<Return>', self.get_text_input)
        self.bind('<Control-m>', self.get_mic_input)

    def display_help(self):
        commands = {
            'Commands/Help': 'Display a list of commands',
            'Repeat/Say/Speak [text]': 'Convert the provided text to speech',
            'Lookup/Search [text]': 'Search the provided text on DuckDuckGo',
            'Clear': 'Clears the screen',
            'Exit/Quit/Stop': 'Quits and closes the program',
            'Play [game]': 'Plays the selected game. '\
                           'Selected game name must match one of the available games exactly.',
            'Games': 'Lists available games'
        }

        message = 'Available Commands:\n'
        for command in sorted(commands):
            description = commands[command]
            message += f"\t{command} - {description}\n"
        message += '\n'
        self.update_textbox(message, trim_newline=False)

    def get_text_input(self, event=None):
        text_input = self.text_input.get()
        self.update_textbox(text_input)
        self.text_input.delete(0, 'end')
        self.process_input(text_input)

    def get_mic_input(self, event=None):
        mic_input = self.bot.listen()
        if not mic_input:
            mic_input = 'I did not catch that...'
        self.update_textbox(mic_input)
        self.process_input(mic_input)

    def process_input(self, input: str):
        command = input.split()[0].lower()
        text = ' '.join(input.split()[1:]).lower()

        if (command in ['help', 'commands']):
            help_message = self.display_help()
            self.update_textbox(help_message)
        elif (command in ['games']):
            message = "Available Games:\n"
            for game in self.games_list:
                message += f"\t{game.capitalize()}"
            self.update_textbox(message)
        elif (command in ['play']):
            if (text == 'high low'):
                selected_game = Games('High Low')
                selected_game.start()
        elif (command in ['repeat', 'say', 'speak']):
            self.speak_back(text)
        elif (command in ['search', 'lookup']):
            result = self.search_engine.get_result(text)
            if result == "":
                result = "No results found."
            self.update_textbox(result)
            self.speak_back(result)
        elif (command in ['clear']):
            self.clear_textbox()
        elif (command in ['exit', 'stop', 'quit']):
            self.destroy()

    def speak_back(self, text: str):
        self.bot.speak(text)


if __name__=='__main__':
    root = Mia()
    root.start()
