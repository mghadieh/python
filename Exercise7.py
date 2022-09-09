def end_with_e():
    count = 0
    with open('poem.txt', 'r') as file:
        lines = file.readlines()
        for line in lines:
            words = line.split()
            for word in words:
                if word[-1] == 'e':
                    count += 1
    print('There are {} words that end with "e".'.format(count))


end_with_e()
