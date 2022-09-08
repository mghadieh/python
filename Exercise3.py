count = 0
with open('poem.txt', 'r') as file:
    lines = file.readlines()
    for line in lines:
        words = line.split()
        count += len(words)
print('Total number of words in poem.txt is {}'.format(count))
