from base_app import BaseApp
import tkinter as tk
from tkinter import messagebox
import random
import os

# function class to be under the parent
class BrainRouletteApp(BaseApp):
    def __init__(self):
        super().__init__("Brain Roulette Game", "800x600", "white")

        self.players = []
        self.category = None
        self.question_manager = QuestionManager()

        self.current_frame = None
        self.show_intro()