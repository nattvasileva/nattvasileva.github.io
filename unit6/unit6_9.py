# -*- coding: utf-8 -*-
"""
Created on Sat Apr 23 20:08:50 2022

@author: nataliya.vasileva
"""

import math

def is_prime(n):
    output=[]
    i=1
    while i<=n:
        if (n%i==0):
            output.append(i)
            i += 1
        else:i += 1
    if len(output)==1:
        return "False"
    elif len(output)>2:
        return "False"
    else: return "True"