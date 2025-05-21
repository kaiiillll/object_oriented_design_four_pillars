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
    def save_questions(self):
        question = self.question_entry.get("1.0", tk.END).strip()
        subject = self.subject_var.get()
        difficulty = self.difficulty_var.get()
        options = {
            "a": self.option_a.get(),
            "b": self.option_b.get(),
            "c": self.option_c.get(),
            "d": self.option_d.get()
        }
        correct = self.correct_answer.get().lower()

        if not all([question, subject, difficulty, options["a"], options["b"], options["c"], options["d"], correct]):
            messagebox.showerror("Error", "Please fill all fields!")
            return

        if correct not in ["a", "b", "c", "d"]:
            messagebox.showerror("Error", "Correct answer must be a, b, c, or d!!")
            return

# saving the information into the txt file 
        with open("created_questions.txt", "a") as file:
            file.write(f"Subject: {subject}\n")
            file.write(f"Difficulty: {difficulty}\n")
            file.write(f"Question: {question}\n")
            file.write(f"a) {options['a']}\n")
            file.write(f"b) {options['b']}\n")
            file.write(f"c) {options['c']}\n")
            file.write(f"d) {options['d']}\n")
            file.write(f"Correct: {correct}\n\n")

        messagebox.showinfo("Saved", "Question saved successfully!")
        self.clear_fields()
        
    def preview(self):
        preview_text = f"Subject: {self.subject_var.get()}\n"
        preview_text += f"Difficulty: {self.difficulty_var.get()}\n"
        preview_text += f"Question: {self.question_entry.get('1.0', tk.END).strip()}\n"
        preview_text += f"a) {self.option_a.get()}\n"
        preview_text += f"b) {self.option_b.get()}\n"
        preview_text += f"c) {self.option_c.get()}\n"
        preview_text += f"d) {self.option_d.get()}\n"
        preview_text += f"Correct: {self.correct_answer.get().lower()}"

        messagebox.showinfo("Preview", preview_text)

    def clear_fields(self):
        self.question_entry.delete("1.0", tk.END)
        self.subject_var.set("Math")
        self.difficulty_var.set("Easy")
        self.option_a.delete(0, tk.END)
        self.option_b.delete(0, tk.END)
        self.option_c.delete(0, tk.END)
        self.option_d.delete(0, tk.END)
        self.correct_answer.delete(0, tk.END)

if __name__ == "__main__":
    app = QuizCreator()
    app.mainloop()
