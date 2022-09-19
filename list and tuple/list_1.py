# append method

list1 = ["apple", "banana", "cherry", "durian"]
print(list1)
list1.append("orange")
print(list1)

# extend

list2 = ["apple", "banana", "cherry", "durian"]
print(list2)
list2.extend(["raspberry", "strawberry", "blueberry"])
print(list2)

# insert

list3 = ["apple", "banana", "cherry", "durian"]
print(list3)
list3.insert(2, "orange")
print(list3)

# remove

list4 = ["apple", "banana", "cherry", "banana", "durian"]
print(list4)
list4.remove("banana")
print(list4)

# pop

list5 = ["apple", "banana", "cherry", "durian"]
print(list5)
print(list5.pop())  # empty pop removes the last element of the list
print(list5)
print(list5.pop(0))
print(list5)


# delete

list6 = ["apple", "banana", "cherry", "banana", "durian"]
del list6[3]
print(list6)


# index

list7= ["apple", "banana", "cherry", "banana", "durian"]
print(list7.index('banana'))


# count

list8 = ["apple", "banana", "cherry", "banana", "durian"]
print(list8.count("banana"))


# sort

list9 = ["apple", "strawberry", "banana", "raspberry", "cherry", "banana", "durian", "blueberry"]
list9.sort()
print(list9)
num1 = [314 , 315, 642, 246, 129, 999]
num1.sort()
print(num1)



# reverse sort

list10 = ["apple", "strawberry", "banana", "raspberry", "cherry", "banana", "durian", "blueberry"]
list10.sort(reverse=True)
print(list10)