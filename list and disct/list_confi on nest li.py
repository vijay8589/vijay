# list comprehension on nested list

list1 = [[1, 2, 3], [4, 5, 6],["a", "b"]]
l1 = [ x[1] for x in list1]
print(l1)


 # list comprehension in functions

def square(x):
     return x*x
c = [square(x) for x in range(1, 11)]
print(c)

# add two lists

v = [5, 6, 7]
r = [10, 11, 12]
rv = [x + y for x in v for y in r]
print(rv)

# Assign matrix
twoDMatrix = [[10, 20, 30],
              [40, 50, 60],
              [70, 80, 90]]

# Generate transpose
trans = [[i[j] for i in twoDMatrix] for j in range(len(twoDMatrix[0]))]

print(trans)
