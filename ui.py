from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"


class QuizInterface:

    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("Quizzler")

        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        # question field
        self.canvas_white = Canvas(width=300, height=250, bg="white", highlightthickness=0)
        self.canvas_white.grid(row=1, column=0, columnspan=2, pady=50)
        self.question_text = self.canvas_white.create_text(
            150,
            125,
            text="hi there",
            font=("Ariel", 15, "italic"),
            fill=THEME_COLOR,
            width=280
        )
        # Buttons
        image_true = PhotoImage(file="./images/true.png")
        image_false = PhotoImage(file="./images/false.png")
        self.button_true = Button(image=image_true, highlightthickness=0, command=self.user_guess_right)
        self.button_false = Button(image=image_false, highlightthickness=0, command=self.user_guess_wrong)
        self.button_true.grid(row=2, column=0)
        self.button_false.grid(row=2, column=1)

        # score
        self.score_text = Label(text="Score 0", fg="white", bg=THEME_COLOR, highlightthickness=0)
        self.score_text.grid(row=0, column=1)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        self.canvas_white.config(bg="white")
        if self.quiz.still_has_questions():
            self.score_text.config(text=f"Score: {self.quiz.score}")
            q_text = self.quiz.next_question()
            self.canvas_white.itemconfig(self.question_text, text=q_text)
        else:
            self.canvas_white.itemconfig(self.question_text, text="You have reached the end of the quiz.")
            self.button_true.config(state="disabled")
            self.button_false.config(state="disabled")

    def user_guess_right(self):
        is_right = self.quiz.check_answer("true")
        print(is_right)
        self.give_feedback(is_right)

    def user_guess_wrong(self):
        is_right = self.quiz.check_answer("false")
        print(is_right)
        self.give_feedback(is_right)

    def give_feedback(self, is_right: bool):
        if is_right:
            self.canvas_white.config(bg="green")
        else:
            self.canvas_white.config(bg="red")
        self.window.after(1000, self.get_next_question)
