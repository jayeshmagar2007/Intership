num1 = int(input("Enter the first number :"))
num2 = int(input("Enter the second number :"))
num3 = int (input("Enter the third number :"))
if num1 > num2 and num1 >num3:
    print(f"{num1} number is greater than {num2} and {num3}")
elif num2 >num3 and num2 > num1:
    print(f"{num2} number is greater than {num1} and {num3} ")
else :
    print(f"{num3} number is greater than {num1} and {num2}")        