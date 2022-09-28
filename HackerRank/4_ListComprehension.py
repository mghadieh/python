#  You are given three integers and representing the dimensions of a cuboid along with an integer . Print a list of all possible coordinates given by on a 3D grid where the sum of is not equal to . Use list comprehensions rather than multiple loops.

# Example
# x = 1
# y = 1
# z = 1
# n = 2

# Output
# [[0, 0, 0], [0, 0, 1], [0, 1, 0], [1, 0, 0], [1, 1, 1]]

if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())

    print(list([i, j, k] for i in range(x+1) for j in range(y+1)
          for k in range(z+1) if i+j+k != n))
