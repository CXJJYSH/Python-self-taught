class Hexagon:
    def __init__(self,s1,s2,s3,s4,s5,s6):
        self.s1=s1
        self.s2=s2
        self.s3=s3
        self.s4=s4
        self.s5=s5
        self.s6=s6
        print("Created!")
    def calculate_perimeter(self):
        return self.s1+self.s2+self.s3+self.s4+self.s5+self.s6
Hexagon=Hexagon(1,2,3,4,5,6)
print(Hexagon.calculate_perimeter())
