"""Write a Python program that iterates the integers from 1 to 25.
For multiples of four print “Fizz” instead of the number and for the multiples of five print “Buzz”.
For numbers which are multiples of both four and five print “FizzBuzz”."""

x = 25
for i in range(0 , x):
    if i%4 == 0 and i%5 == 0: # number is multiple by both 4 and 5 print FizzBuzz
        print("FizzBuzz")
        continue

    if i%4 ==0 and i%5!= 0:
        print("Fizz")

    if i%4!= 0 and i%5 ==0:
        print("Buzz")
    else:
        print(i)