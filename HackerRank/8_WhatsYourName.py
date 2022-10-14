# Function Description
# Complete the print_full_name function in the editor below.
# print_full_name has the following parameters:
#     string first: the first name
#     string last: the last name

# Prints
#     string: 'Hello <firstname> <lastname>! You just delved into python' where <firstname> and  <lastname> are replaced with first and last.

# Input Format
# The first line contains the first name, and the second line contains the last name.

def print_full_name(first, last):
    print('Hello {} {}! You just delved into python.'.format(first, last))


if __name__ == '__main__':
    first_name = input()
    last_name = input()
    print_full_name(first_name, last_name)
