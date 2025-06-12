def calculator(num1,num2,op):
    if op =='+':
        print("Addition is :",num1+num2)
    elif op =='-':
        print("subtraction is :",num1-num2)
    elif op =='*':
        print("Multiplication is :",num1*num2)
    elif op =='/':
        print("Division is :",num1/num2)
# num1= int(input("Enter the first number :"))
# num2 = int(input("Enter the second number :"))
op= input("Enter the operator :")
calculator(10,20,op)        
