if __name__ == '__main__':
    N = int(input())
    result = []
    strng = ''

    for i in range(N):
        inp = input()
        lst = inp.split()
        if lst[0].lower() == 'insert':
            result.insert(int(lst[1]), int(lst[2]))
        elif lst[0].lower() == 'print':
            print(result)
        elif lst[0].lower() == 'append':
            result.append(int(lst[1]))
        elif lst[0].lower() == 'remove':
            result.remove(int(lst[1]))
        elif lst[0].lower() == 'sort':
            result.sort()
        elif lst[0].lower() == 'pop':
            if len(lst) > 1:
                result.pop(int(lst[1]))
            else:
                result.pop()
        elif lst[0].lower() == 'reverse':
            result.reverse()


# Test case
# # 12
# # insert 0 5
# # insert 1 10
# # insert 0 6
# # print
# # remove 6
# # append 9
# # append 1
# # sort
# # print
# # pop
# # reverse
# # print
