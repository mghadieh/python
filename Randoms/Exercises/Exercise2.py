def count_lines_without_T():
    count = 0
    with open('poem.txt', 'r') as file:
        lines = file.readline()
        for line in lines:
            if (line[0].upper() != 'T'):
                count += 1
    print("Number of lines that don't start with a 'T' or a 't' is {}".format(count))


count_lines_without_T()
