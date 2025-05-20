# This base will be the parent of the other classes
# Import tkinter as a base app
import tkinter as tk

class BaseApp(tk.Tk):
    def __init__(self, title, size, bg_color="white"):
        super().__init__()
        self.title(title)
        self.geometry(size)
        self.configure(bg=bg_color)