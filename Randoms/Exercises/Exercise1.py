'''
Excerise 1
Write a function in python to read the content from a text file "poem.txt" line by line and display the same on screen.
'''
# I created a random file poem.txt, if you don't have the file, ucomment the 3 lines below before running the program

# file = open('.\poem.txt', 'w')
# file.write('hello')
# file.close()

# Copied few paragraphs from wikipedia about poetry

def read_content():
    with open('poem.txt', 'r') as file:
        for line in file:
            # strip is used to remove the extra spaces inputted by copying the text from htnl
            print(line.strip())

read_content()