import math

class Triangle:
    def __init__(self,a,b,c):
        self.a=a
        self.b=b
        self.c=c
        print("Created!")
    def area(self):
        s=(self.a+self.b+self.c)/2
        return math.sqrt(s*(s-self.a)*(s-self.b)*(s-self.c))
Triangle=Triangle(3,4,5)
print(Triangle.area())
