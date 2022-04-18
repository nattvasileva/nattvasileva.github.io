# -*- coding: utf-8 -*-
"""
Created on Sat Apr 16 00:43:25 2022

@author: nataliya.vasileva
"""

import math

def my_reverse(l):
    output=[]
    i=len(l)-1
    while i>=0:
        output.append(l[i])
        i -= 1
    return output

