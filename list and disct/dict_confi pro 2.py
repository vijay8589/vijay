"""We can iterate over two iterables in a dictionary comprehension."""
words = ['data', 'science', 'machine', 'learning']
values = [5, 3, 1, 8]
dict_a = {i : j for i, j in zip(words, values)}
print(dict_a)
var = {'data': 5, 'science': 3, 'machine': 1, 'learning': 8}



"""The keys of a dictionary must be immutable so tuples can be used as keys. 
Dictionary comprehensions allow for generating keys of tuples by implemented nested loops."""

a = [1,2,3,4]
b = [5,6,7]
dct = {(i,j):i*j for i in a for j in b}
print(dct)

v = {(1, 5): 5,
       (1, 6): 6,
       (1, 7): 7,
       (2, 5): 10,
       (2, 6): 12,
       (2, 7): 14,
       (3, 5): 15,
       (3, 6): 18,
       (3, 7): 21,
       (4, 5): 20,
       (4, 6): 24,
       (4, 7): 28}
