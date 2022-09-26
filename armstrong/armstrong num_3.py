"""Python Program to check Armstrong Number Using While Loop."""

number = int(input("Please Enter the Number to Check: "))

Sum = 0
Times = 0

temp = number
while temp > 0:
    Times = Times + 1
    temp = temp // 10

temp = number
while temp > 0:
    Reminder = temp % 10
    Sum = Sum + (Reminder ** Times)
    temp //= 10

if number == Sum:
    print("%d is Armstrong." % number)
else:
    print("%d is Not." % number)
