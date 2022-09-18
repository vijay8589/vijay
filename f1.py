"""Create a function"""


# demo is the function name
def demo(name, age):
    # print value
    print(name, age)

# call function
demo("Ben", 25)



"""Create a function with variable length of arguments"""


def func1(*args):
    for i in args:
        print(i)

func1(20, 40, 60)
func1(80, 100)


"""Return multiple values from a function"""


def calculation(a, b):
    addition = a + b
    subtraction = a - b

    return addition, subtraction

# get result in tuple format
res = calculation(40, 10)
print(res)



