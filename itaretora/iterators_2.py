"""Sample built-in iterators"""

# Iterating over a list
print("List Iteration")
l = ["vijay", "in", "hyderabad"]
for i in l:
    print(i)

# Iterating over a tuple (immutable)
print("\nTuple Iteration")
t = ("vijay", "in", "hyderabad")
for i in t:
    print(i)

# Iterating over a String
print("\nString Iteration")
s = "vijay"
for i in s:
    print(i)

# Iterating over dictionary
print("\nDictionary Iteration")
d = dict()
d['xyz'] = 123
d['abc'] = 345
for i in d:
    print("%s  %d" % (i, d[i]))
