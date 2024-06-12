
from math import *
class Point_1:
    def __init__(self,x,y) -> None:
        self.x=x
        self.y=y
        pass
    def distance(self,other):
        return "{:.4f}".format(sqrt(pow(self.x-other.x,2)+pow(self.y-other.y,2)))
    
def Decimal(a):
    return float(a)

# if __name__ == '__main__':
#     t = int(input())
#     while t > 0:
#         arr = input().split()
#         p1 = Point(Decimal(arr[0]), Decimal(arr[1]))
#         p2 = Point(Decimal(arr[2]), Decimal(arr[3]))
#         print(p1.distance(p2))
#         t -= 1

class Rectangle:
    def __init__(self,h,w,c) -> None:
        self.h = int(h)
        self.w = int(w)
        self.c = str(c)
        pass
    
    def perimeter(self):
        return (self.h +self.w)*2
    
    def area(self):
        return self.h * self.w
    
    def color(self):
        a = self.c.lower()
        a = a.title()
        return a


class Fraction_1:
    def __init__(self,num, den) -> None:
        self.num = int(num)
        self.den = int(den)
        pass
    
    def simplify(self):
        gcd0 = gcd(self.num, self.den)
        self.num = self.num//gcd0
        self.den = self.den//gcd0
        return "{}/{}".format(self.num,self.den)
    
class Fraction_2:
    def __init__(self,num, den) -> None:
        self.num = int(num)
        self.den = int(den)
        pass
    
    def add_fraction(self,other):
        den_gcd = gcd(self.den,other.den)
        den_lcm = (self.den * other.den)// den_gcd
        self.num = self.num * (den_lcm // self.den)
        other.num = other.num * (den_lcm // other.den)
        return Fraction_2(self.num + other.num, den_lcm)
    
    def simplify(self):
        gcd0 = gcd(self.num, self.den)
        self.num = self.num//gcd0
        self.den = self.den//gcd0
        return "{}/{}".format(self.num,self.den)
    
class Point_2:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def distance(self, other):
        return ((self.x - other.x)**2 + (self.y - other.y)**2)**0.5

class Triangle_1:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c
    
    def is_valid(self):
        side_ab = self.a.distance(self.b)
        side_bc = self.b.distance(self.c)
        side_ca = self.c.distance(self.a)
        
        return max(side_ab, side_bc, side_ca)*2<(side_ab+side_bc+side_ca)
    
    def perimeter(self):
        p = self.a.distance(self.b) + self.b.distance(self.c) + self.c.distance(self.a)
        return "{:.3f}".format(p) if self.is_valid() else "INVALID"
    
a = []
t = int(input())
for x in range(t):
    # a.append([float(i) for i in input().split()])
    a += [float(i) for i in input().split()]
    
i = 0
for index in range(t):
    triagle = Triangle_1(Point_2(a[i], a[i+1]), Point_2(a[i+2], a[i+3]), Point_2(a[i+4], a[i+5]))
    print(triagle.perimeter())
    i += 6