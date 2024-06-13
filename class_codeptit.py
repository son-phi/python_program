
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
        side_ab = self.a.distance(self.b)
        side_bc = self.b.distance(self.c)
        side_ca = self.c.distance(self.a)
        p = side_ab + side_bc + side_ca 
        s = sqrt(p*(p - 2*side_ab)*(p - 2*side_bc)*(p - 2*side_ca))/4
        return "{:.2f}".format(s) if self.is_valid() else "INVALID"
    
    
class complex_number:
    def __init__(self,real,imag) -> None:
        self.real = int(real)
        self.imag = int(imag)
        self.a = "{} + {}i".format(self.real,self.imag)
        pass
    
    def add(self,other):
        return complex_number(self.real + other.real, self.imag + other.imag )
    
    def mul(self,other):
        return complex_number(self.real * other.real - self.imag * other.imag, self.real * other.imag + self.imag * other.real)   


class Student:
    def __init__(self,name,birthdate,grade) -> None:
        self.name = str(name)
        self.birthdate = str(birthdate)
        self.grade = grade
        self.sum_grade = float(grade[0]) +float(grade[1]) + float(grade[2])
        if len(self.birthdate) < 10:
            if self.birthdate[2] != "/": self.birthdate = "0"+ birthdate
            if self.birthdate[5] != "/": self.birthdate = birthdate[:3] +"0"+birthdate[3:]
        pass
    
    def print(self):
        print("{} {} {:.1f}".format(self.name,self.birthdate,self.sum_grade))


class RainfallStation:
    def __init__(self,id, name, duration, rainfall_amount ) -> None:
        self.id = id
        self.name = name
        self.duration = round(duration/60,10)
        self.average_hourly_rainfall = round(rainfall_amount/ self.duration,2)
        pass
    
    
    
dict_station = {}
t = int(input())

for x in range(t):
    name = input()
    start = input()
    end = input()
    amt = int(input())
    duration = 60 - int(start[-2:]) + int(end[-2:]) + int(end[:2]) - int(start[:2]) -1
    id = "T0{}".format(len(dict_station)+1) 
    if name not in dict_station.keys() :
        dict_station[name] = [ id , name, duration, amt]
    else:
        dict_station[name][2] += duration
        dict_station[name][3] += amt

# print(dict_station)
for st in dict_station.values() :
    s = RainfallStation(st[0],st[1],st[2],st[3])
    print( "{} {} {:.2f}".format(s.id, s.name,s.average_hourly_rainfall))
    # print(st[2],st[3])

