
from math import *
class Point():
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

class Rectangle():
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

arr = input().split() 
if int(arr[0]) > 0 and int(arr[1]) > 0: 
    r = Rectangle(int(arr[0]), int(arr[1]), arr[2]) 
    print("{} {} {}".format(r.perimeter(), r.area(), r.color())) 
else: 
    print("INVALID")
