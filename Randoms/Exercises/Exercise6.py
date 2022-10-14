def count_this_these():
    word_check = ['this', 'these']
    count = 0
    with open('poem.txt', 'r') as file:
        lines = file.readlines()
        for line in lines:
            words = line.split()
            for word in words:
                if 'this' == word.lower() or 'these' == word.lower():
                    count += 1
    print('"This" and "These" occured {} times.'.format(count))


count_this_these()
