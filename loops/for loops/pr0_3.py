"""The Fibonacci sequence is a sequence of numbers that starts with 1, followed
by 1 again. Every next number is the sum of the two previous numbers. I.e., the sequence
starts with 1, 1, 2, 3, 5, 8, 13, 21,... Write a program that calculates and prints the Fibonacci
sequence until the numbers get higher than 1000."""

num1 = 0
num2 = 1
print(1, end=" ")
while True:
    num3 = num1 + num2
    if num3 > 1000:
        break
    print(num3, end=" ")
    num1 = num2
    num2 = num3