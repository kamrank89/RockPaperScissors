from tkinter import *
import random

global user_score, computer_score
user_score = 0
computer_score = 0

m = Tk()
blank_space = " " * 65
m.title(blank_space + "Rock Paper Scissors Game")
m.config(width=600, height=400, bg='grey')


# Frames
button_frame = Frame(m, width=300, height=200)
button_frame.grid_propagate(False)
button_frame.grid(row=0, column=0, padx=150)
text_frame = Frame(m, width=500, height=200)
text_frame.grid_propagate(False)
text_frame.grid(row=1, column=0, padx=50)

# Functions


def rock():
    global user_score, computer_score
    user_choice_label.config(text="your choice is : Rock")

    user_choice = "Rock"
    available_text = ["Rock", "Paper", "Scissors"]
    computer_choice = random.choice(available_text)
    if computer_choice == user_choice:
        # computer_score = 0
        # user_score = 0
        computer_choice_label.config(text=f"computer choice is : {computer_choice}")
        computer_score_label.config(text=f"computer score is : {computer_score}")
        user_score_label.config(text=f"your score is : {user_score}")
    if computer_choice == "Paper":
        computer_choice_label.config(text=f"computer choice is : {computer_choice}")
        computer_score += 1
        # user_score = 0
        computer_score_label.config(text=f"computer score is : {computer_score}")
        user_score_label.config(text=f"your score is : {user_score}")
    if computer_choice == "Scissors":
        computer_choice_label.config(text=f"computer choice is : {computer_choice}")
        user_score += 1
        # computer_score = 0
        user_score_label.config(text=f"your score is : {user_score}")
        computer_score_label.config(text=f"computer score is : {computer_score}")


def paper():
    global user_score, computer_score
    user_choice_label.config(text="your choice is : Paper")

    user_choice = "Paper"
    available_text = ["Rock", "Paper", "Scissors"]
    computer_choice = random.choice(available_text)
    if computer_choice == user_choice:

        computer_choice_label.config(text=f"computer choice is : {computer_choice}")
        computer_score_label.config(text=f"computer score is : {computer_score}")
        user_score_label.config(text=f"your score is : {user_score}")
    if computer_choice == "Scissors":
        computer_choice_label.config(text=f"computer choice is : {computer_choice}")
        computer_score += 1

        computer_score_label.config(text=f"computer score is : {computer_score}")
        user_score_label.config(text=f"your score is : {user_score}")
    if computer_choice == "Rock":
        computer_choice_label.config(text=f"computer choice is : {computer_choice}")
        user_score += 1

        user_score_label.config(text=f"your score is : {user_score}")
        computer_score_label.config(text=f"computer score is : {computer_score}")


def scissors():
    global user_score, computer_score
    user_choice_label.config(text="your choice is : Scissors")

    user_choice = "Scissors"
    available_text = ["Rock", "Paper", "Scissors"]
    computer_choice = random.choice(available_text)
    if computer_choice == user_choice:
        # computer_score = 0
        # user_score = 0
        computer_choice_label.config(text=f"computer choice is : {computer_choice}")
        computer_score_label.config(text=f"computer score is : {computer_score}")
        user_score_label.config(text=f"your score is : {user_score}")
    if computer_choice == "Rock":
        computer_choice_label.config(text=f"computer choice is : {computer_choice}")
        computer_score += 1
        # user_score = 0
        computer_score_label.config(text=f"computer score is : {computer_score}")
        user_score_label.config(text=f"your score is : {user_score}")
    if computer_choice == "Paper":
        computer_choice_label.config(text=f"computer choice is : {computer_choice}")
        user_score += 1
        # computer_score = 0
        user_score_label.config(text=f"your score is : {user_score}")
        computer_score_label.config(text=f"computer score is : {computer_score}")


# User Buttons
rock_button = Button(button_frame, text="Rock", activebackground='red', command=rock, width=15, bg='white')
rock_button.grid(row=0, column=0, padx=90, pady=15)

paper_button = Button(button_frame, text="Paper", command=paper, activebackground='red', width=15, bg='white')
paper_button.grid(row=1, column=0, padx=90, pady=15)

scissors_button = Button(button_frame, text="Scissors", command=scissors, activebackground='red', width=15, bg='white')
scissors_button.grid(row=2, column=0, padx=90, pady=15)

# Contents for the text frame
user_choice_label = Label(text_frame, text="your choice is : ")
user_choice_label.grid(row=1, column=0, padx=20, pady=10)

computer_choice_label = Label(text_frame, text="computer choice is : ")
computer_choice_label.grid(row=1, column=2, padx=120, pady=10)

computer_score_label = Label(text_frame, text="computer score is : ")
computer_score_label.grid(row=3, column=2)

user_score_label = Label(text_frame, text="your score is : ")
user_score_label.grid(row=3, column=0, padx=20)

# Exit button
exit_button = Button(text_frame, text="Exit", command=m.destroy, width =30, activebackground='red')
exit_button.grid_propagate(False)
exit_button.grid(row=5, column=0, columnspan=3, pady= 20, padx=40)

m.mainloop()
