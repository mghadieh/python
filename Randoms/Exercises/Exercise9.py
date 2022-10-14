from curses.ascii import isalpha


def hash_display():
    with open('poem.txt','r') as file:
        lines = file.readlines()
        for line in lines:
            words = line.strip().split()
            for word in words:
                for i in range(len(word)):
                    #if word[i].isalpha():
                    print(word[i],end='#')
                    #else:
                        #print(word[i], end="")

hash_display()