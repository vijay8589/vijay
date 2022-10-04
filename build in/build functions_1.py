"""Python abs() function"""

print(abs(-100))
print(abs(1023))
print(abs(123.25))
print(abs(-2033.66))


"""Get absolute value of numbers of a list."""

nums = [12,30,-33,-22,77,-100]
print("Original list:")
print(nums)
print("\nAbsolute values of the above numbers:")
print([abs(x) for x in nums])


""" all values true"""


num = [23, 45, 10, 30]
print(all(num)) #True

# all values false
num = [0, False]
print(all(num)) #False

# one false value
num = [1, 3, 4, 0]
print(all(num)) #False

# one true value
num = [0, False, 5]
print(all(num)) #False

# empty iterable
num = []
print(all(num)) #True


"""any() function"""

str = "vijay is good boy"
print(any(str))

# 0 is False
# '0' is True
str = '000'
print(any(str))

str = ''
print(any(str))