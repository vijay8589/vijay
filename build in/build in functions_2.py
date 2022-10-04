"""bin() function"""

x = 10
print("Original number: ",x)
y = bin(x)
print("Binary string:")
print (y)
x = -10
print("\nOriginal number: ",x)
y = bin(x)
print("Binary string:")
print (y)



"""bool() function"""

val = True
print("val = ", bool(val))
val = False 
print("val = ", bool(val))
val = 5
print("val = ", bool(val))
val = 0
print("val = ", bool(val))
val = bool()
print("val = ", bool(val))
