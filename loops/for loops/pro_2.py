"""find the factorial of given number using the loop."""

v = int(input("enter the number"))
r = 1
for i in range(v , 0, -1):
    r = r *i
print("factorial" , v,"is" ,r)


"""Write a program to calculate the sum of series up to n term. 
For example, if n =5 the series will become 2 + 22 + 222 + 2222 + 22222 = 24690"""

n = 5
# first number of sequence
start = 2
sum_seq = 0

# run loop n times
for i in range(0, n):
    print(start, end="+")
    sum_seq += start
    # calculate the next term
    start = start * 10 + 2
print("Sum of above series is:", sum_seq)