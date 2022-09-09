total = 0
with open('poem.txt','r') as file:
    content = file.read()
    total = content.count('the')
print('"The" occured {} times in poem.txt.'.format(total))