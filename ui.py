import tkinter as tk
import _tkinter
from quiz_brain import QuizBrain
import time


THEME_COLOR = "#375362"


class QuizInterface:

    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain

        self.window = tk.Tk("Quiz")
        self.window.configure(bg=THEME_COLOR, padx=20, pady=20)

        self.score_text = tk.Label(text="Score: 0",
                                   fg="white",
                                   bg=THEME_COLOR,
                                   font=("Ariel", 12, "bold"),
                                   highlightthickness=0)
        self.score_text.grid(column=0, row=0)

        self.canvas = tk.Canvas(width=300,
                                height=250,
                                bg="white")
        self.question_text = self.canvas.create_text(150,
                                                     125,
                                                     width=260,
                                                     text="Question!",
                                                     font=("Ariel", 18, "italic"))
        self.canvas.grid(column=0, columnspan=2, row=1, padx=0, pady=30)

        self.yes_image = tk.PhotoImage(file="images/true.png")
        self.yes_button = tk.Button(image=self.yes_image,
                                    bg=THEME_COLOR,
                                    padx=50,
                                    pady=50,
                                    highlightthickness=0,
                                    borderwidth=0,
                                    command=self.true_pressed)
        self.yes_button.grid(column=0, row=2)

        self.no_image = tk.PhotoImage(file="images/false.png")
        self.no_button = tk.Button(image=self.no_image,
                                   bg=THEME_COLOR,
                                   padx=50,
                                   pady=50,
                                   highlightthickness=0,
                                   borderwidth=0,
                                   command=self.false_pressed)
        self.no_button.grid(column=1, row=2)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg="white")
        self.update_score()
        response = self.quiz.next_question()
        q_text = response[1]
        self.canvas.itemconfig(self.question_text, text=q_text)

        if response[0]:
            pass
        else:
            self.yes_button.config(state="disabled")
            self.no_button.config(state="disabled")

    def true_pressed(self):
        self.get_answer("true")

    def false_pressed(self):
        self.get_answer("false")

    def get_answer(self, answer: str):
        response = self.quiz.check_answer(answer)
        self.flash(response[0])

    def flash(self, answer: bool):
        if answer:
            self.canvas.config(bg="green")
            self.window.after(1000, self.get_next_question)
        else:
            self.canvas.config(bg="red")
            self.window.after(1000, self.get_next_question)

    def update_score(self):
        self.score_text.config(text=f"Score: {self.quiz.score}")
