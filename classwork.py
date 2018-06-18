#Question1
a=int(input("Enter the year"))

if(a%4 == 0):
    print("The year is a leap year")
    print(a)
else:
    print("the year is not a leap year")

#Question2

a=int(input("Enter the length"))
b=int(input("Enter the breadth"))

if(a==b):
    print("This is a square")
else:
    print("This is a rectangle")

#Question3
a=int(input("Enter the age of a"))
b=int(input("Enter the age of b"))
c=int(input("Enter the age of c"))

if(a<b):
    if(a<c):
        print("a is the youngest")
        print(a)
    elif(b<c):
        print("b is the youngest")
        print(b)
    else:
        print("c is youngest")



    if(a>c):
        if(a>b):
         print("a is the eldest")
         print(a)
    elif(b>c):
        print("b is the eldest")
    else:
        print("c is the eldest")
        print(c)


#Question4
a=int(input("Enter your points"))
if(a>=1 and a<=50):
    print("Sorry! No prize won this time")
elif(a>50 and a<=150):
     print("Congratulations! You won a Wooden Dog")
elif(a>150 and a<=180):
        print("Congratulations! You won a Book")
elif(a>180 and a<=200):
        print("Congratulations! You won Chocolates")
else:
    print("Sorry no prize")


#Question5
a=int(input("Enter the quantity of the goods"))
e=a*100
if(e>1000):
    b=e*0.1
    c=e-b
    print("Discount given is")
    print(b)
    print("Cost after discount is")
    print(c)
else:
    print("Sorry no discount given")







