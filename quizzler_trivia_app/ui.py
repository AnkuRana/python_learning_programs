import tkinter
from tkinter import *
from tkinter.ttk import *
from quiz_brain import QuizBrain
THEME_COLOR = "#375362"
RIGHT_COLOR = "#29B677"
WRONG_COLOR = "#EE665D"
FONT_SCORE = ("Arial", 15, "normal")
FONT_QUES = ("Arial", 15, "italic")


class QuizInterface:
    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("Trivia App")
        self.window.config(background=THEME_COLOR, padx=20, pady=20)
        self.score_label = Label(text=f"Score:0", font=FONT_SCORE, background=THEME_COLOR, foreground="white")
        self.score_label.grid(row=0, column=1, sticky="e")

        self.canvas = tkinter.Canvas()
        self.canvas.config(height=250, width=300, background="white")
        self.canvas_text = self.canvas.create_text(150, 125, text="Question will show here!", fill=THEME_COLOR,
                                                   font=FONT_QUES, width=280)
        self.canvas.grid(row=1, column=0, columnspan=2, pady=40, sticky="we")

        img_right = PhotoImage(file="./images/true.png")
        self.right_button = Button(image=img_right, command=self.click_right_button)
        self.right_button.grid(row=2, column=0)

        img_wrong = PhotoImage(file="./images/false.png")
        self.wrong_button = Button(image=img_wrong, command=self.click_wrong_button)
        self.wrong_button.grid(row=2, column=1)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(background="white")
        q_text = self.quiz.next_question()
        self.canvas.itemconfig(self.canvas_text, text=q_text)

    def click_right_button(self):
        is_right = self.quiz.check_answer("True")
        self.update_score()
        if self.quiz.still_has_questions():
            self.give_feedback(is_right)
        else:
            final_score = f"Your final score: {self.quiz.score}"
            self.canvas.itemconfig(self.canvas_text, text=final_score)
            self.right_button.config(state="disabled")
            self.wrong_button.config(state="disabled")

    def click_wrong_button(self):
        is_right = self.quiz.check_answer("False")
        self.update_score()
        if self.quiz.still_has_questions():
            self.give_feedback(is_right)
        else:
            final_score = f"Your final score: {self.quiz.score}"
            self.canvas.itemconfig(self.canvas_text, text=final_score)
            self.right_button.config(state="disabled")
            self.wrong_button.config(state="disabled")

    def update_score(self):
        self.score_label.config(text=f"Score: {self.quiz.score}")

    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(background=RIGHT_COLOR)
        else:
            self.canvas.config(background=WRONG_COLOR)
        self.window.after(500, self.get_next_question)


