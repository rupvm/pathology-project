# -*- coding: utf-8 -*-
"""
Created on Mon May 27 20:54:50 2024

@author: halde
"""


def is_prime(a):
    for i in range(2,a):
        if a%i==0:
            return False
        else:
            return True
  
            
  
    
n=int(input("enter the limit"))

for i in range(n+1):
    if is_prime(i):
        print(i,"prime no")



m=[1,2,3,4,5]
print(tuple(m))
    
list1=set(["white","black","red"])
list2=set(["red","green"])

print(list1-list2)

def gcd(x,y):
    gcd=1
    
    if x%y==0:
        return y   
    for k in range(int(y/2),0,-1):
        if x%k==0 and y%k==0:
            gcd=k
            break
        
    return gcd

print("the gcd of 12 and 17",gcd(4,6))



def lcm(x,y):
    if x>y:
        z=x
    else:
        z=y     
    while True:
        if z%x==0 and z%y==0:
            lcm=z
            break
        
        z+=1
    return lcm



print("th lcm of 4 6",lcm(4,6))


s="hello this is me"
# print(" ".join("".join(sorted(i)) for i in s.split()))

l=[sorted(i) for i in s.split()]
print(l)


def fact(a):
    if a==0:
        return 1
    else:
        return a*fact(a-1)

print("the factorial is",fact(5))


def sum(a):
    if a==0:
        return 0
    else:
        return a%10+sum(a//10)
        

print("the sum is",sum(45))


        