# list comprehension

var = [x for x in range(1, 11)]
print(var)

# print 1 to 10 even numbers

a = [x for x in range(1, 11) if x%2 == 0]
print(a)

b = [x if x>2 else x+1 for x in range(1, 11)]
print(b)


num = [1, 2, 3, 4, 5]
v = 10 * num
print(v)

num1 = [x * 10 for x in num]
print(num1)


# change the case of words or alphabet

words = ["helli", "i", "vijay"]
w1= [ x.upper() for x in words]
print(w1)





