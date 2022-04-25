# -*- coding: utf-8 -*-
"""
Created on Sun Apr 24 00:47:30 2022

@author: nataliya.vasileva
"""

import math

def primes_below(n):
    output=[]
    k=2
    i=0
    while i<n:
        if (i%k!=0):
            output.append(i)
            k += 1
        else:i += 1
        output.append(i)
    return output