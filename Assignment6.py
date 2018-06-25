#Question1
Int=[]
for i in range (0,10):
    Int.append(int(input("Enter the integer")))
print(Int)

#Question2
while True:
    print("Infinite")

#Question3
a=[]
b=[]
for i in range (0,4):
    number=int(input("Enter the number"))
    a.append(number)
print (a)
for i in a:
    b.append(i**2)
print(b)

#Question4
list=[4,1,'a', 2.23, 'f', 3.45]
intlist=[x for x in list if isinstance(x,int)] #if x is an instance of integer then print it in list intlist
print(intlist)
flist=[x for x in list if isinstance(x,float)]#if x is an instance of float then print it in list flist
print(flist)
strlist=[x for x in list if isinstance(x,str)]#if x is an instance of string then print it in list strlist
print(strlist)

#Question5
Even=[]
Odd=[]
for i in range(1,101):
    if(i%2==0):
        Even.append(i)
    else:
        Odd.append(i)
print(Even)
print(Odd)

#Question6
for i in range(1,5):
    for j in range(1,i+1):
        print("*", end="")
    print()


#Question7
list = {'Abhishek':16,'Piyush':19, 'Tarun':20,'Mohit':22}
search_age = input("Provide age: ")
search_age = int(search_age)
#Here we define another empty dictionary, to store the results in a more permanent way.
listofAge = {}
#We use double variable iteration, so we get both the name and age on each run of the loop
for name, age in list.items():
# We use double variable iteration, so we get both the name and age on each run of the loop
    if age == search_age:
        age = str(age)
        results = name + " " +age
        print (results)

 # Here we create a second variable that uses the value of the age for the current person in the list.
 # For example if "Piyush" is "19", age2 = 19, integer value which we can use in addition.
        age2 = int(age)
        listofAge[name] = listofAge.get(name,0)+age2
print (listofAge)

#Question8
l=[]
for i in range(0,5):
    num=int(input("Enter the number"))
    l.append(num)
print(l)
l2=[]
a=int(input("enter the value to be deleted"))
if a in l:
    print(a)
    x=l.index(a)
    x=l.remove(a)
print(l)

