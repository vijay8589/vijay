"""Write a Program in Python to Find the Smallest and the Largest List Elements on Inputs Provided by the User"""

# creating an empty list
res_list = []

num = int(input("How many elements in list:"))

for x in range(num):
    numbers = int(input('Enter number '))
    res_list.append(numbers)

print("Maximum element in the list is :", max(res_list))
print("Minimum element in the list is :", min(res_list))




"""add two lists in one list. Example: [[1, 2, 3], [4, 5], [6, 7, 8]]

Output: [1, 2, 3, 4, 5, 6, 7, 8]"""

List1 = [[1, 2, 3], ['x', 'y', 'z'], ['A', 'B', 'C']]
print("The original list is : " + str(List1))

# empty list
flat_list = []

for x in List1:
    flat_list = flat_list + x






# updated flat list
print("Flat list" + str(flat_list))



