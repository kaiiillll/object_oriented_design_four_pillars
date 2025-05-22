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
        
# registration and animation
    def clear_frame(self):
        if self.current_frame:
            self.current_frame.destroy()
            self.current_frame = None

    def show_intro(self):
        self.clear_frame()
        self.current_frame = IntroAnimation(self, self.show_player_registration)
        self.current_frame.pack(expand=True, fill="both")

    def show_player_registration(self):
        self.clear_frame()
        self.current_frame = PlayerRegistration(self, self.start_main_menu)
        self.current_frame.pack(expand=True, fill="both")