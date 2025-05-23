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
        self.questions = []  # Load your questions here

class IntroAnimation(tk.Frame):
    def __init__(self, parent, next_callback):
        super().__init__(parent)
        tk.Label(self, text="Welcome to Brain Roulette!").pack()
        tk.Button(self, text="Continue", command=next_callback).pack()
        