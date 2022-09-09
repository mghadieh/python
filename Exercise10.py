def JTOI():
    lst = []
    with open('poem_Exercise_10.txt', 'r') as file:
        content = file.read()
        lst = list(content)
        # print(lst)
        for i in range(len(lst)):
            print('before change', lst[i])
            if lst[i] == 'j':
                lst[i] = 'i'
            elif lst[i] == 'J':
                lst[i] = 'I'
            print('after change', lst[i])
    print(lst)
    with open('poem_Exercise_10.txt', 'w') as file:
        content = ''.join(lst)
        print(content)
        file.write(''.join(lst))


JTOI()
# this can be verified by comparing the last word in line 22 with the original poem.txt "Shijin" -> "Shiiin"
