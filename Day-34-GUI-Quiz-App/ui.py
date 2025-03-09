from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"
QUESTION_FONT = ("Arial", 20, "italic")
SCORE_FONT = ("Arial", 18, "normal")


class QuizInterface:

    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.windows = Tk()
        self.windows.title("Quiz App 2.0")
        # self.windows.minsize(width=600, height=600)
        self.windows.config(bg=THEME_COLOR, pady=20, padx=20)

        self.score_text = Label(text=f"Score: 0", bg=THEME_COLOR, fg="white", font=SCORE_FONT)
        self.score_text.grid(row=0, column=1)

        self.canvas = Canvas(width=300, height=250, bg="white")
        self.question_text = self.canvas.create_text(150, 125, text="Questions will appear hear", fill="black",
                                                     font=QUESTION_FONT, width=280)
        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)

        true_img = PhotoImage(file="images/true.png")
        false_img = PhotoImage(file="images/false.png")

        self.true_button = Button(image=true_img, highlightthickness=0, command=self.true_answer)
        self.true_button.grid(row=2, column=0)

        self.false_button = Button(image=false_img, highlightthickness=0, command=self.false_answer)
        self.false_button.grid(row=2, column=1)

        self.get_next_question()

        self.windows.mainloop()

    def get_next_question(self):
        if self.quiz.still_has_questions():
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
        else:
            self.canvas.itemconfig(self.question_text, text="You've reached the end of the quiz")
            self.true_button.config(state="disabled")
            self.false_button.config(state="disabled")

    def true_answer(self):
        self.give_feedback(self.quiz.check_answer("True"))
        return True

    def false_answer(self):
        self.give_feedback(self.quiz.check_answer("False"))

    def give_feedback(self, is_right):
        def default_bg():
            self.canvas.config(bg="white")

        if is_right:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.score_text.config(text=f"Score: {self.quiz.score}/{self.quiz.question_number}")
        self.windows.after(1000, default_bg)
        self.get_next_question()
