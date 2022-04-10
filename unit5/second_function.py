 # -*- coding: utf-8 -*-
"""
Created on Sun Apr  3 23:19:33 2022

@author: nataliya.vasileva
"""
import math

def solve_quadratic (a,b,c):
    if (b**2-4*a*c)>0:
        x=(-b+math.sqrt(b**2-4*a*c))/(2*a)
        y=(-b-math.sqrt(b**2-4*a*c))/(2*a)
        return (x,y)
    elif b**2-4*a*c==0:
        z=(-b)/(2*a)
        return z
    else:
        return 'None'
   