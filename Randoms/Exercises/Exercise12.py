import os
import random

# changing the wd to the correct one.
os.chdir("/Users/mohamadghadieh/Documents/Mohamad/Projects/Python/Excercises/cleanFileData")

# books.txt is a file download from the internet. It contains more than we need of information.
# exercise_file is a text file that will only contain the information we need to do this exercise.


def getData():
    exercise_file = open('ex12_file.txt', 'w')
    with open('Ex12_books.txt', 'r') as file:
        lines = file.readlines()
        for line in lines[1:]:
            words = line.strip().split(';')
            req_words = words[:3]
            exercise_file.write(';'.join(req_words) + ';' +
                                '"' + str(random.randint(10, 200)) + '"\n')
    exercise_file.close()


def creatFile():
    book_number = int(input("Enter book number: "))
    book_title = input("Enter book title: ")
    book_auther = input("Enter book author: ")
    book_price = int(input("Enter book price: "))
    writeToFile(book_number, book_title, book_auther, book_price)


def writeToFile(num, title, author, price):
    with open('ex12_file.txt', 'a') as file:
        file.write('"{}";"{}";"{}";"{}"'.format(
            str(num), title, author, str(price)))
        file.write('\n')


def countRec(author):
    count = 0
    with open('ex12_file.txt', 'r') as file:
        lines = file.readlines()        # List of strings
        test = lines[3]
        for line in lines:
            words = line.strip().split(';')     # list of strings
            if author == words[2][1:-1]:
                count += 1
    return count


def run():
    if not os.path.exists('ex12_file.txt') or os.path.getsize('ex12_file.txt') == 0:
        getData()
    creatFile()

    author = input("Enter name of author to search: ")
    count = countRec(author)
    print("The author '{}' has {} books in our list.".format(author, count))


run()
