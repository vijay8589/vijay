# use of lambda functions
double = lambda x: x * 2

print(double(5))


# Program to filter out only the even items from a list
my_list = [1, 5, 4, 6, 8, 11, 3, 12]

new_list = list(filter(lambda x: (x%2 == 0) , my_list)) #using the fileter function

print(new_list)


#program to double each item in a list using map()

my_list = [1, 5, 4, 6, 8, 11, 3, 12]

new_list = list(map(lambda x: x * 2 , my_list)) # use the map function

print(new_list)





"""Specified number: 27.2 Expected Answer:
The double number of 27.2 = 54.4"""


def double_number(n):
    return lambda x: x * n # use the lambda function


result = double_number(2)
print("The double number of 27.2 =", result(27.2))