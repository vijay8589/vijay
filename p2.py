"""Even Number Pyramid Pattern
10

10 8

10 8 6

10 8 6 4

10 8 6 4 2"""


rows = 5

LastEvenNumber = 2 * rows

evenNumber = LastEvenNumber

for i in range(1, rows+1):

    evenNumber = LastEvenNumber

    for j in range(i):

        print(evenNumber, end=" ")

        evenNumber -= 2

    print("\r")
