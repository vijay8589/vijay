# Python zip() function

x = [1, 2, 3]
y = [4, 5, 6]
zipped = zip(x, y)
print(list(zipped))



name = ["vijay", "kumar", "software engineer"]
a = [14, 3, 6]

result = zip(name, a)
print(list(result))

# Output: [('Java', 14), ('Python', 3), ('JavaScript', 6)]



number_list = [1, 2, 3]
str_list = ['one', 'two', 'three']

result = zip()

# Converting iterator to list
result_list = list(result)
print(result_list)

# Two iterables are passed
result = zip(number_list, str_list)

# Converting iterator to set
result_set = set(result)
print(result_set)