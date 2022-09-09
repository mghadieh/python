def AMCount():
    a_count = 0
    m_count = 0
    with open('poem.txt', 'r') as file:
        content = file.read()
        for i in range(len(content)):
            if (content[i] == 'a' or content[i] == 'A'):
                a_count += 1
            elif (content[i] == 'm' or content[i] == 'M'):
                m_count += 1
    print('A or a: {}; M or m: {}'.format(a_count, m_count))

    # Another approach
    # for letter in content:
    #     if letter == 'A' or letter == 'a':
    #          a_count += 1
    #     elif (letter == 'm' or letter == 'M'):
    #         m_count += 1


AMCount()
