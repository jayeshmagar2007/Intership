s1= int(input("Enter the marks of Subject 1 :"))
s2= int(input("Enter the marks of Subject 2 :"))
s3= int(input("Enter the marks of Subject 3 :"))
total= s1+s2+s3 
per=total/3
print("Total marks obtained :",total)
print("Percentage is :",per)
if per<=100 and per>=90:
    print("Grade : A+")
elif per>=80 and per<=89:
    print(" Grade : A")
elif per>=70 and per<=79:  
    print("Grade : B")
elif per>= 60 and per<=69:
    print("Grade :C ") 
elif per>=36 and per<=59:   
    print("Grade : D")
else:
    print("Fail")    
