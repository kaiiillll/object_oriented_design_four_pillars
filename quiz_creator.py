# import the needed function from the base app 
from base_app import BaseApp
import tkinter as tk
from tkinter import messagebox

class QuizCreator(BaseApp):
    def __init__(self):
        super().__init__("Teacher's Quiz Maker", "500x550", "#e6f2ff")
        self.build_ui()

# def function for the buttons and interfaces         
    def build_ui(self):
        tk.Label(self, text="Question:").pack(pady=5)
        self.question_entry = tk.Text(self, height=4, width=50)
        self.question_entry.pack(pady=5)

        tk.Label(self, text="Subject:").pack(pady=5)
        self.subject_var = tk.StringVar(value="Math")
        subjects = ["Math", "Science", "History", "English", "General"]
        tk.OptionMenu(self, self.subject_var, *subjects).pack(fill="x", padx=50)

        tk.Label(self, text="Difficulty:").pack(pady=5)
        self.difficulty_var = tk.StringVar(value="Easy")
        difficulties = ["Easy", "Medium", "Hard"]
        tk.OptionMenu(self, self.difficulty_var, *difficulties).pack(fill="x", padx=50)

        tk.Label(self, text="Options:").pack(pady=5)
        self.option_a = tk.Entry(self, width=50)
        self.option_a.pack(pady=2)
        self.option_b = tk.Entry(self, width=50)
        self.option_b.pack(pady=2)
        self.option_c = tk.Entry(self, width=50)
        self.option_c.pack(pady=2)
        self.option_d = tk.Entry(self, width=50)
        self.option_d.pack(pady=2)

        tk.Label(self, text="Correct Answer (a-d):").pack(pady=5)
        self.correct_answer = tk.Entry(self, width=5)
        self.correct_answer.pack()

        tk.Button(self, text="Save Question", command=self.save_questions, bg="green", fg="white").pack(pady=10)
        tk.Button(self, text="Preview", command=self.preview).pack(pady=5)
        tk.Button(self, text="Clear", command=self.clear_fields).pack(pady=5)

# then proceed to copy all the remaining codes from my original 