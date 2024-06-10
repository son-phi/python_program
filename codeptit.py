# CODEPTIT
from math import *

lst_number = "0123456789"
result =[]
def my_function(st):
    i = 0
    while i <  len(st):
        x=""
        if st[i] in lst_number:
            x+=st[i]
            while i < len(st) - 1 and st[i+1] in lst_number:
                i+=1
                x+=st[i]  
        i+=1
        if x!="":
            result.append(int(x)) 
    return result

s = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
def doi_co_so_10_sang_m(cs10,m):
    a=""
    while cs10//m !=0:
        a = str(s[cs10%m]) +a
        cs10//=m
    return s[cs10]+ a

def doi_co_so_n_sang_10(n,cs2):
    cs10= 0
    i = 0
    while i < len(cs2):
        cs10 *=int(s[n]) 
        cs10 +=int(cs2[i])
        i+=1
    return cs10

def is_prime(n):
    i=2
    if n<2 : return False
    while i <= isqrt(n):
        if n%i== 0:
            return False
        i+=1
    return n>=1

def GCD(x,y):
    while y:
        x,y = y,x%y
    return abs(x)

t = int(input())
while t!=0:
    print(GCD(15 ,3))
    
    t-=1



