def display_words():
    with open('poem.txt', 'r') as file:
        lines = file.readlines()
        for line in lines:
            words = line.split()
            for word in words:
                if len(word) < 4:
                    print(word, end=' ')


display_words()
