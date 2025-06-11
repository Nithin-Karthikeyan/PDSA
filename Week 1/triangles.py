from math import sqrt

class Triangle():
    def __init__(self, a, b ,c):
        self.a = a
        self.b = b
        self.c = c
    
    def Is_valid(self):
        if self.a+self.b>self.c and self.a+self.c>self.b and self.c+self.b>self.a:
            return "Valid"
        return "Invalid"

    def Side_Classification(self):
        if self.Is_valid() == "Invalid":
            return "Invalid"

        if self.a == self.b == self.c:
            return "Equilateral"
        elif self.a != self.b != self.c:
            return "Scalene" 
        else:
            return "Isosceles"
    def Angle_Classification(self):
        if self.Is_valid() == "Invalid":
            return "Invalid"
        
        sides = [self.a, self.b, self.c]
        sides.sort()
        s1 = sides[0]
        s2 = sides[1]
        s3 = sides[2]


        if s1**2 + s2**2 > s3**2:
            return "Acute"
        elif s1**2 + s2**2 < s3**2:
            return "Obtuse"
        else:
            return "Right"
        
    def Area(self):
        if self.Is_valid() == "Invalid":
            return "Invalid"
    
        s = (self.a+self.b+self.c)/2
        area = sqrt(s*(s-self.a)*(s-self.b)*(s-self.c))
        return area
    
a=int(input())
b=int(input())
c=int(input())
T=Triangle(a,b,c)
print(T.Is_valid())
print(T.Side_Classification())
print(T.Angle_Classification())
print(T.Area())