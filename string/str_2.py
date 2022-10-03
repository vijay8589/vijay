"""Remove the ith character from the string using the native method"""

test_str = "vijaya raju"

# Removing char at pos 3
new_str = ""

for i in range(len(test_str)):
    if i != 2:
        new_str = new_str + test_str[i]

# Printing string after removal
print("The string after removal of i'th character : " + new_str)


""" Python code to demonstrate string length"""
# using for loop

# Returns length of string
def findLen(str):
    counter = 0
    for i in str:
        counter += 1
    return counter


str = "vijay"
print(findLen(str))