#Question1
class Flower():
    def flower_attribute(self):
        print('The most Beautiful Flower')
class Lotus(Flower):
    print('Lotus is the national flower of india')
lot=Lotus()
lot.flower_attribute()

#Question2
#Output is given as following:
#print a.f() = A
#print b.()= B

#Question3
class Cop():
    def __init__(self,name,age,work,experience,designation):
        self.n=name
        self.a=age
        self.w=work
        self.e=experience
        self.d=designation
    def display(self):
        print(self.n)
        print(self.a)
        print(self.w)
        print(self.e)
        print(self.d)
    def update(self,name,age,work,experience,designation):
        self.na=name
        self.ag=age
        self.wo=work
        self.ex=experience
        self.ds=designation
        print(self.na)
        print(self.ag)
        print(self.wo)
        print(self.ex)
        print(self.ds)
class Mission(Cop):
    def add__mission__details(self):
        print('Mission Accomplished')
c=Cop('Ethan Hunt',30,'IMF Agent',20,'The best Agent of IMF')
m=Mission('Ethan Hunt',30,'IMF Agent',20,'The Best Agent of IMF')
m.display()
m.update('William Brandt',29,'IMF Analyst',20,'The second best IMF of Agent')

#Question4
class Shape():
    def __init__(self,length,breadth):
        self.l=length
        self.b=breadth
class Rectangle(Shape):
    def Area(self):
        area=(self.l)*(self.b)
        print(area)
class Square(Shape):
    def Area(self):
        AREA=(self.l)*(self.l)
        print(AREA)
s=Shape(10,6)
r=Rectangle(10,6)
r.Area()
sq=Square(4,4)
sq.Area()

