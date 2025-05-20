# import the needed function from the base app 
from base_app import BaseApp
import tkinter as tk
from tkinter import messagebox

class QuizCreator(BaseApp):
    def __init__(self):
        super().__init__("Teacher's Quiz Maker", "500x550", "#e6f2ff")
        self.build_ui()

# need to make class to be under the parent which is the base 
# then proceed to copy all the remaining codes from my original 