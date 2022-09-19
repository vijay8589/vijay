"""Create an inner function to calculate the addition """


# outer function
def outer_fun(a, b):
    square = a ** 2

    # inner function
    def addition(a, b):
        return a + b
    add = addition(a, b)

    return add + 5

result = outer_fun(5, 10)
print(result)




"""Create a recursive function"""


def addition(num):
    if num:

        return num + addition(num - 1)
    else:
        return 0

res = addition(10)
print(res)