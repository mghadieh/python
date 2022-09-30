from tkinter import *
from tkinter import messagebox
from random import choice

word = ''

root = Tk()
root.title('Color Game')
root.geometry('600x500')

score = 0
timeleft = 10


def start_game(event):
    if timeleft == 60:
        count_down()
        shuffle()
        scoreLabel.config(text="Score: 0")
    else:
        check_answer()


def count_down():
    global timeleft
    if timeleft == 0:
        messagebox.showinfo("Time Over", "Score is: " + str(score))
    else:
        timeleft -= 1
        timeLabel.config(text='Time left: ' + str(timeleft))
        timeLabel.after(1000, count_down)


# Function to produce a new word with a new color
def shuffle():
    # Clear the input field and the result lable item in the GUI
    eAnswer.delete(0, END)
    # result.config(text='')
    result.after(400, lambda: result.config(text=''))

    global wordColor  # this variable needs to be accessed in check_answer function

    colors = ['red', 'yellow', 'brown', 'blue', 'orange', 'purple',
              'pink', 'black', 'green', 'cyan', 'white', 'navy']
    word = choice(colors)
    wordColor = choice(colors)
    colorLabel.config(text=word, fg=str(wordColor))


# Function to check the user's answer
def check_answer():
    global timeleft
    global score
    if timeleft > 0:
        eAnswer.focus_set()
        if eAnswer.get().lower() == wordColor.lower():
            result.config(text="Correct!")
            score += 1
        else:
            result.config(text="Incorrect!")
    scoreLabel.config(text="Score: " + str(score))
    shuffle()


# This is where the colored word will appear
colorLabel = Label(root, text="", font=('Helvetica', 30))
colorLabel.pack(pady=30)

# This is where the score is going to be displayed
scoreLabel = Label(root, text="Press Enter to start", font=('Helvetica', 20))
scoreLabel.pack()

# Time label to display timeleft
timeLabel = Label(root, text="Time left: " +
                  str(timeleft), font=('Helvetica', 15))
timeLabel.pack(pady=10)

# Answer input field
eAnswer = Entry(root, font=('Helvetica', 20))
eAnswer.pack(pady=20)

myFrame = Frame(root)
myFrame.pack(pady=20)

# # Create button to reshuffle
# btn_refresh = Button(myFrame, text="Another word",
#                      font=("Helvetica", 15), command=shuffle)
# # btn_refresh.pack(pady=10)
# btn_refresh.grid(row=0, column=0, padx=10)

# Create button to check answer inputted
btn_check = Button(myFrame, text="Check", font=(
    "Helvetica", 15), command=check_answer)
# btn_check.pack(pady=20)
btn_check.grid(row=0, column=1, padx=10)

# Display if user's answer is correct or incorrect
result = Label(root, text='', font=("Helvetica", 25))
result.pack(pady=20)


eAnswer.focus_set()
# Binding the event (Pressing Enter) to the root and start the game
root.bind('<Return>', start_game)
# Main loop function
root.mainloop()


####################

# from tkinter import *
# from random import choice
# from random import shuffle
# from tkinter import messagebox

# root = Tk()
# root.title('Color Game')
# root.geometry("600x400")
# root.iconbitmap("C:/Users/Administrator/Desktop/coloricon.ico")

# myLabel = Label(root, text="", font=("Helvetica", 50))
# myLabel.pack(pady=20)

# score = 0
# timeleft = 60


# def startGame(event):
#     if timeleft == 60:
#         countdown()
#         shuffler()
#         scorelabel.config(text="Score: 0")
#     else:
#         answer()


# def countdown():
#     global timeleft
#     if timeleft == 0:
#         messagebox.showinfo("Time Over", "Time is over and your score is " + str(score))
#     if timeleft > 0:
#         timeleft -= 1
#         timelabel.config(text="Time Left: " + str(timeleft))
#         timelabel.after(1000, countdown)


# def shuffler():
#     eAnswer.delete(0, END)
#     # ansLabel.config(text="")
#     ansLabel.after(400, lambda: ansLabel.config(text=''))


#     global color
#     colors = ['red', 'yellow', 'brown', 'blue', 'orange', 'purple', 'pink', 'black', 'green', 'cyan', 'white', 'navy']

#     word = choice(colors)
#     color= choice(colors)

#     myLabel.config(text=word, fg= str(color))


# def answer():
#     global score
#     global timeleft

#     if timeleft > 0:
#         eAnswer.focus_set()
#         if eAnswer.get().lower() == color.lower():
#             score += 1
#             ansLabel.config(text="Correct!")
#         else:
#             ansLabel.config(text="Incorrect")
#         scorelabel.config(text="Score: " + str(score))

#         shuffler()


# scorelabel = Label(root, text="Enter to start", font=('Helvetica', 24))
# scorelabel.pack()

# timelabel = Label(root, text="Time left: " + str(timeleft), font=('Helvetica', 12))
# timelabel.pack()

# eAnswer = Entry(root, font=("Helvetica", 25))
# eAnswer.pack(pady=20)

# myFrame = Frame(root)
# myFrame.pack(pady=20)

# # myButton = Button(myFrame, text="Pick Another Word", command=shuffler)
# # myButton.grid(row=0, column=0, padx=10)

# ansButton = Button(myFrame, text="Answer!", command=answer)
# ansButton.grid(row=0, column=1, padx=10)

# ansLabel = Label(root, text="", font=("Helvetica", 20))
# ansLabel.pack(pady=20)

# root.bind('<Return>', startGame)
# eAnswer.focus_set()

# root.mainloop()
