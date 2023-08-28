from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"

class QuizInterface:

    def __init__(self, quiz_brain : QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("Quiz")
        self.window.config(padx=20, pady=20, bg= THEME_COLOR)

        self.score_label = Label(text="Score: 0", fg="white", bg=THEME_COLOR)
        self.score_label.grid(row=0, column = 1)

        self.canvas = Canvas(height=250, width=300, bg= "white")
        self.canvas.grid(row = 1, column = 0, columnspan = 2, pady = 50)
        self.question_text = self.canvas.create_text(150, 125, text = "sjema", font = ("Arial", 20, "italic"), width= 280)


        green_image = PhotoImage(file = "images/true.png")
        self.green_button = Button(image = green_image, highlightthickness=0, command= self.clicked_true)
        self.green_button.grid( row = 2, column =0)

        red_image = PhotoImage(file="images/false.png")
        self.red_button = Button(image = red_image, highlightthickness= 0, command=self.clicked_false)
        self.red_button.grid(row=2, column=1)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():

            self.score_label.config(text = f"Score: {self.quiz.score}")
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text= q_text)
        else:
            self.canvas.itemconfig(self.question_text, text= "The end!")
            self.green_button.config(state= "disabled")
            self.red_button.config(state="disabled")

    def clicked_true(self):
        self.get_feedback(self.quiz.check_answer("True"))

    def clicked_false(self):
        self.get_feedback(self.quiz.check_answer("False"))

    def get_feedback(self, is_right):
        if is_right:
            self.canvas.config(bg = "green")
        else:
            self.canvas.config(bg ="red")

        self.window.after(2000, self.get_next_question)

