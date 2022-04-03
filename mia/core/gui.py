import tkinter as tk
from tkinter import ttk
from typing import Callable, List


class Gui(tk.Tk):
    def __init__(self, window_title: str):
        super().__init__()
        self.window_title = window_title

    def start(self):
        self.create_widgets()
        self.mainloop()

    def create_widgets(self, widget_list: List[Callable]=None):
        self.create_root_window()
        self.create_mainframe()
        self.create_textbox()
        if (widget_list):
            for widget in widget_list:
                widget()
        self.set_styles()

    def create_root_window(self):
        # Size Root Window and Center on Screen
        self.title(self.window_title)
        window_width = int(self.winfo_screenwidth()/1.5)
        window_height = int(self.winfo_screenheight()/1.5)
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()
        x = int(int(screen_width/2) - int(window_width/2))
        y = int(int(screen_height/2) - int(window_height/2))
        self.geometry(f"{window_width}x{window_height}+{x}+{y}")
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)

    def create_mainframe(self):
        # Set up a main frame element to hold the widgets
        self.mainframe = ttk.Frame(self, padding='10')
        self.mainframe.grid(column=0, row=0, sticky='NSEW')
        self.mainframe.grid_columnconfigure(0, weight=1)
        self.mainframe.grid_rowconfigure(0, weight=1)

    def create_textbox(self):
        # Set up Textbox to display messages
        self.textbox = tk.Text(self.mainframe, font=('Arial 16'))
        self.textbox.config(state='disabled', wrap='word')
        self.textbox.grid(column=0, row=0, columnspan=3, sticky='NSEW', pady=(0, 10))
        self.textbox.grid_columnconfigure((0, 1, 2), weight=1)

    def set_styles(self):
        # Define Application Styles
        self.style = ttk.Style(self)
        self.style.configure('TFrame', background='black')
        self.style.configure('TButton', background='grey30', font=('Arial 16'))

    def update_textbox(self, text, trim_newline: bool=True, indent: bool=False):
        if (trim_newline):
            text = text.rstrip() + '\n'
        if (indent):
            text = '\t' + text
        self.textbox.config(state='normal')
        self.textbox.insert('end', text)
        self.textbox.config(state='disabled')
        self.textbox.see('end')

    def clear_textbox(self):
        self.textbox.config(state='normal')
        self.textbox.delete(1.0,'end')
        self.textbox.config(state='disabled')


if __name__=='__main__':
    test = Gui('Test')
    test.update_textbox('Test')
    test.start()
