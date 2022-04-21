# -*- coding: utf-8 -*-
"""
Created on Sat Apr 16 15:46:21 2022

@author: nataliya.vasileva
"""

import math

def big_fibonacci(n):
    i=1
    m=1
    s=0
    while n>=len(str(i)):
        if n==len(str(i)):
            return i
        else:
            s=i+m
            m=i
            i=s
            
        
        
        
        

