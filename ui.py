from tkinter import *
from quiz_brain import QuizBrain
THEME_COLOR = "#375362"


class QuizInterface:

    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain

        self.window = Tk()
        self.window.title("Quizzy")
        self.window.config(bg=THEME_COLOR, padx=20, pady=20)

        self.score = Label(text="Score: 0", bg=THEME_COLOR, fg="white", font=("Arial", 11, "normal"))
        self.score.grid(row=0, column=1, pady=20)

        self.canvas = Canvas(width=300, height=250, bg="white")
        self.question_text = self.canvas.create_text(150, 125, text="My Question here", width=280,
                                                     fill=THEME_COLOR, font=("Arial", 18, "italic"))
        self.canvas.grid(row=1, column=0, padx=20, pady=30, columnspan=2)

        true_img = PhotoImage(file="images/true.png")
        self.true_btn = Button(image=true_img, highlightthickness=0, command=self.check_true)
        self.true_btn.grid(row=2, column=0, pady=20)
        false_img = PhotoImage(file="images/false.png")
        self.false_btn = Button(image=false_img, highlightthickness=0, command=self.check_false)
        self.false_btn.grid(row=2, column=1, pady=20)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg="white")
        self.score.config(text=f"Score: {self.quiz.score}")
        if self.quiz.still_has_questions():
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
        else:
            self.canvas.itemconfig(self.question_text, text="You've reached the end of quiz")
            self.true_btn.config(state="disabled")
            self.false_btn.config(state="disabled")

    def check_true(self):
        is_right = self.quiz.check_answer("true")
        self.give_feedback(is_right)

    def check_false(self):
        is_right = self.quiz.check_answer("false")
        self.give_feedback(is_right)

    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")

        # using sleep here will mess up with tkinter main loop
        self.window.after(1000, self.get_next_question)
