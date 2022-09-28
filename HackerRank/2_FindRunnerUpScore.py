# Given the participants' score sheet for your University Sports Day, you are required to find the runner-up score. You are given scores. Store them in a list and find the score of the runner-up.

# Example

# input :
# 5
# 2 3 6 6 5

# Output: 5

if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())

    lst = list(arr)
    lst.sort()
    # by creating a dict using the list items as keys, all duplicates are removed.
    lst = list(dict.fromkeys(lst))

    print(lst[-2])
