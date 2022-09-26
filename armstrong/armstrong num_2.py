"""Check Armstrong number of n digits."""

num = 1634
# and calculated the length (number of digits)
order = len(str(num))
sum = 0

temp = num
while temp > 0:
   digit = temp % 10
   sum += digit ** order
   temp //= 10

# display the result
if num == sum:
   print(num,"is an Armstrong number")
else:
   print(num,"is not an Armstrong number")