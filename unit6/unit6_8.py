# -*- coding: utf-8 -*-
"""
Created on Thu Apr 21 15:22:13 2022

@author: nataliya.vasileva
"""

import math

n=1
while n<1001:
        if n%15==0:
            n=n+1
            print ("FizzBuzz")
        elif n%5==0:
            n=n+1
            print ("Buzz")
        elif n%3==0:
            n=n+1
            print ("Fizz")
        else:
            print (n)
            n=n+1

