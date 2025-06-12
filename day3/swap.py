a = int(input("Enter the value of a : "))
b = int(input("Enter the value of b : "))
print(f"Value of a before swap   {a}")
print(f"Value of a before swap {b}")
temp = a
a = b
b = temp
print("Value after swap a:",a)
print ("Value afterswap b:",b)