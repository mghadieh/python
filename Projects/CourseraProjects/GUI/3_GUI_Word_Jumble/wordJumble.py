from datetime import timedelta
from tkinter import *
from tkinter import messagebox

from matplotlib.pyplot import text
import random

root = Tk()
root.title("Word Jumble")
root.geometry('600x400')
root.iconbitmap('./icon.ico')


score = 0
timeLeft = 60


def start_game(event):
    global timeLeft
    if timeLeft == 60:
        scoreLabel.config(text='Score: ')
        countdown()
        shuffle()
    else:
        check_answer()


def countdown():
    global timeLeft
    if timeLeft == 0:
        messagebox.showinfo('Time Over', 'Score is: ' + str(score))
    else:
        timeLeft -= 1
        timeLabel.config(text="Time left:" + str(timeLeft))
        timeLabel.after(1000, countdown)


def shuffle():
    global correct_word
    global shuffled_word
    # clear previous data from previous run
    eAnswer.delete(0, END)
    resultLabel.config(text="")
    Countries = ['Egypt', 'Sudan', 'Oman', 'Yemen', 'Syria', 'Algeria', 'Qatar', 'Lebanon', 'Tunisia', 'Libya',
                 'Kuwait', 'Jordan', 'Iraq', 'France', 'Germany', 'Spain', 'China', 'India', 'Canada', 'Brazil',
                 'Italy', 'Poland', 'Sweden', 'Norway', 'Greece', 'Netherlands', 'Japan', 'Iran', 'Portugal', 'Mexico',
                 'Cuba', 'Argentina', 'Colombia']
    correct_word = random.choice(Countries)
    lst = list(correct_word)
    random.shuffle(lst)

    shuffled_word = ''
    for char in lst:
        shuffled_word += char

    wordLabel.config(text=shuffled_word)


def check_answer():
    global score
    if eAnswer.get().lower() == correct_word.lower():
        resultLabel.config(text='Correct')
        score += 1
    else:
        resultLabel.config(text='Incorrect')
    scoreLabel.config(text='Score: ' + str(score))
    resultLabel.after(400, shuffle)


wordLabel = Label(root, text='', font=('Helvetica', 50))
wordLabel.pack(pady=20)

scoreLabel = Label(root, text="Press enter to start.", font=('Helvetica', 20))
scoreLabel.pack(pady=10)

timeLabel = Label(root, text="Time left: 60", font=('Helvetica', 20))
timeLabel.pack(pady=10)

eAnswer = Entry(root, font=('Helvetica', 20))
eAnswer.pack(pady=20)

# btn_run = Button(root, text='Run', font=('Helvetica', 20), command=shuffle)
# btn_run.pack(pady=10)

btn_check = Button(root, text="Run", command=check_answer)
btn_check.pack(pady=10)

resultLabel = Label(root, text='', font=('Helvetica', 15))
resultLabel.pack(pady=20)

root.bind('<Return>', start_game)
eAnswer.focus_set()
root.mainloop()
