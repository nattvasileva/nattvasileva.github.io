# -*- coding: utf-8 -*-
"""
Created on Sat Apr 30 22:56:02 2022

@author: nataliya.vasileva
"""

import math

class Triangle():
    def __init__(self,a,b,c):
        self.p=0.5*(a+b+c)
        self.a=a
        self.b=b
        self.c=c
    def area(self):
        return math.sqrt(self.p*(self.p-self.a)*(self.p-self.b)*(self.p-self.c))
    def perimeter(self):
        return self.a+self.b+self.c
    def scale(self,scale_factor):
        return Triangle(scale_factor*self.a,scale_factor*self.b,scale_factor*self.c)
    def is_valid(self):
        if (self.a+self.b>self.c) and (self.a+self.c>self.b) and (self.c+self.b>self.a):
            return True
        else:
            return False
    def is_right(self):
        if (self.a**2+self.b**2==self.c**2) or (self.a**2+self.c**2==self.b**2) or (self.c**2+self.b**2==self.a**2)  :
            return True
        else:
            return False
 #example              
t=Triangle(3, 4, 5)
print ("Area= %d" % t.area())
print ("Perimeter= %d" % t.perimeter())
print  ("Triangle is Valid: %s" % t.is_valid())
print  ("Triangle is right: %s" % t.is_right())
q=t.scale(3)
print(q.a, q.b, q.c)
print ("Area= %d" % q.area())
print ("Perimeter= %d" % q.perimeter())
print  ("Triangle is Valid: %s" % q.is_valid())
print  ("Triangle is right: %s" % q.is_right())