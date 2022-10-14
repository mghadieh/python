from curses.ascii import isupper


def count_Caps():
    count = 0
    with open('poem.txt', 'r') as file:
        lines = file.readlines()
        for line in lines:
            words = line.strip().split()
            for word in words:
                if word[0].isupper():
                    count += 1
    print('The number of uppercase characters is {}.'.format(count))


count_Caps()
