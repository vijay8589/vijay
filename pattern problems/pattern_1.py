"""1: Simple Number Triangle Pattern
Pattern:
1
2 2
3 3 3
4 4 4 4
5 5 5 5 5"""

rows = 6
for i in range(rows):
    for j in range(i):
        print(i, end=" ")
    print(" ")

""" Inverted Pyramid of Numbers
Pattern:
1 1 1 1 1 
2 2 2 2 
3 3 3 
4 4 
5"""

rows = 5

b = 0

for i in range(rows, 0, -1):

    b += 1

    for j in range(1, i + 1):
        print(b, end=" ")

    print("\r")

""" Half Pyramid Pattern of Numbers
1 
1 2 
1 2 3 
1 2 3 4 
1 2 3 4 5"""

rows = 5

for row in range(1, rows + 1):

    for column in range(1, row + 1):
        print(column, end=" ")

    print(" ")