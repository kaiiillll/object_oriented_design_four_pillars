from base_app import BaseApp
import tkinter as tk
from tkinter import messagebox
import random
import os

# function class to be under the parent
class BaseApp(tk.Tk):
    def __init__(self, title, geometry, bg_color):
        super().__init__()
        self.title(title)
        self.geometry(geometry)
        self.configure(bg=bg_color)

class QuestionManager:
    def __init__(self):
        self.questions = []  

class IntroAnimation(tk.Frame):
    def __init__(self, parent, next_callback):
        super().__init__(parent)
        tk.Label(self, text="Welcome to Brain Roulette!").pack()
        tk.Button(self, text="Continue", command=next_callback).pack()
        
# Interfaces for the game
class PlayerRegistration(tk.Frame):
    def __init__(self, parent, on_complete):
        super().__init__(parent)
        self.on_complete = on_complete
        self.entry = tk.Entry(self)
        self.entry.pack()
        tk.Button(self, text="Submit", command=self.submit).pack()

    def submit(self):
        players = [self.entry.get()]
        self.on_complete(players)

class MainMenu(tk.Frame):
    def __init__(self, parent, players, start_wheel_callback):
        super().__init__(parent)
        tk.Label(self, text="Select Category").pack()
        tk.Button(self, text="Math", command=lambda: start_wheel_callback("Math")).pack()

class Wheel(tk.Frame):
    def __init__(self, parent, categories, on_spin_complete):
        super().__init__(parent)
        tk.Label(self, text="Spinning the Wheel...").pack()
        tk.Button(self, text="Stop", command=lambda: on_spin_complete(categories[0])).pack()

class QuestionScreen(tk.Frame):
    def __init__(self, parent, players, category, question_manager, on_complete):
        super().__init__(parent)
        tk.Label(self, text=f"Question from {category}").pack()
        tk.Button(self, text="Finish", command=lambda: on_complete({"score": 1})).pack()

        