from tkinter import *

# Creating the window
window = Tk()
window.title('Calculator')
window.geometry('400x500')
window.configure(bg="#3399ff")
window.iconbitmap("calculator_icon.ico")

# equation = StringVar()
mainFrame = Frame(window, bg='#3399ff')
screenFrame = Frame(window, bg='#3399ff')

screenFrame.pack()
mainFrame.pack()

# Font
font_btn = ('Helvetica', 15, 'bold')
font_screen = ('ariel', 20, 'bold')

equation = StringVar()
equation.set('0')
expression = ''

# Setting up the backend of the calculator


def press(n):
    global expression
    expression += str(n)
    equation.set(expression)


def equal():  # Once the user hits '=' sign, the result will be evaluated and displayed onto the screen
    try:
        global expression
        result = str(eval(expression))
        equation.set(result)
    except:
        equation.set('Error')
    expression = ''


def clear():  # Once the user hits 'C' button, the screen will clear
    global expression
    expression = ''
    equation.set('0')


def backspace():  # Once the user hits '<<', the calculator will delete the last character
    global expression
    expression = expression[:-1]
    equation.set(expression)


# Creating the screen where the output will be displayed
screen = Entry(screenFrame, textvariable=equation,
               width=50, justify='right', font=font_screen)
screen.pack(ipadx=10, ipady=10, pady=20)

# Creating all the buttons for the GUI
btn_0 = Button(mainFrame, text='0', width=10, height=4,
               relief='ridge', bg="#80bfff", font=font_btn, command=lambda: press(0))
btn_1 = Button(mainFrame, text='1', width=10, height=4,
               relief='ridge', bg="#80bfff", font=font_btn, command=lambda: press(1))
btn_2 = Button(mainFrame, text='2', width=10, height=4,
               relief='ridge', bg="#80bfff", font=font_btn, command=lambda: press(2))
btn_3 = Button(mainFrame, text='3', width=10, height=4,
               relief='ridge', bg="#80bfff", font=font_btn, command=lambda: press(3))
btn_4 = Button(mainFrame, text='4', width=10, height=4,
               relief='ridge', bg="#80bfff", font=font_btn, command=lambda: press(4))
btn_5 = Button(mainFrame, text='5', width=10, height=4,
               relief='ridge', bg="#80bfff", font=font_btn, command=lambda: press(5))
btn_6 = Button(mainFrame, text='6', width=10, height=4,
               relief='ridge', bg="#80bfff", font=font_btn, command=lambda: press(6))
btn_7 = Button(mainFrame, text='7', width=10, height=4,
               relief='ridge', bg="#80bfff", font=font_btn, command=lambda: press(7))
btn_8 = Button(mainFrame, text='8', width=10, height=4,
               relief='ridge', bg="#80bfff", font=font_btn, command=lambda: press(8))
btn_9 = Button(mainFrame, text='9', width=10, height=4,
               relief='ridge', bg="#80bfff", font=font_btn, command=lambda: press(9))

btn_dot = Button(mainFrame, text='.', width=10, height=4,
                 relief='ridge', font=font_btn, command=lambda: press('.'))

btn_plus = Button(mainFrame, text='+', width=10, height=4,
                  relief='ridge', bg="#80bfff", font=font_btn, command=lambda: press('+'))
btn_minus = Button(mainFrame, text='-', width=10, height=4,
                   relief='ridge', bg="#80bfff", font=font_btn, command=lambda: press('-'))
btn_x = Button(mainFrame, text='x', width=10, height=4,
               relief='ridge', bg="#80bfff", font=font_btn, command=lambda: press('*'))
btn_div = Button(mainFrame, text='/', width=10, height=4,
                 relief='ridge', bg="#80bfff", font=font_btn, command=lambda: press('/'))
btn_equals = Button(mainFrame, text='=', width=10, height=4,
                    relief='ridge', bg="#80bfff", font=font_btn, command=equal)
btn_clear = Button(mainFrame, text='C', width=10, height=4,
                   relief='ridge', bg="#80bfff", font=font_btn, command=clear)
btn_del = Button(mainFrame, text='<<', width=10, height=4,
                 relief='ridge', bg="#80bfff", font=font_btn, command=backspace)

# Setting up the front end of the App

btn_1.grid(row=0, column=0)
btn_2.grid(row=0, column=1)
btn_3.grid(row=0, column=2)
btn_plus.grid(row=0, column=3)

btn_4.grid(row=1, column=0)
btn_5.grid(row=1, column=1)
btn_6.grid(row=1, column=2)
btn_minus.grid(row=1, column=3)

btn_7.grid(row=2, column=0)
btn_8.grid(row=2, column=1)
btn_9.grid(row=2, column=2)
btn_x.grid(row=2, column=3)

btn_0.grid(row=3, column=0)
btn_dot.grid(row=3, column=1)
btn_clear.grid(row=3, column=2)
btn_div.grid(row=3, column=3)

btn_equals.grid(row=4, column=0, columnspan=3, sticky=NSEW)
btn_del.grid(row=4, column=3)


# Mainloop
window.mainloop()
