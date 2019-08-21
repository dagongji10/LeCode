# -*- coding: utf-8 -*-
"""
Created on Wed Aug 21 10:19:19 2019

@author: Administrator
"""

def romanToInt(s: str) -> int:
    roman = ['I', 'V', 'X', 'L', 'C', 'D', 'M']
    int_n = [1, 5, 10, 50, 100, 500, 1000]
    
    n = 0
    for i,c in enumerate(s):
        idx = roman.index(c)
        
        if i==len(s)-1:
            n += int_n[idx]
        elif roman.index(c)>=roman.index(s[i+1]):
            n += int_n[idx]
        else:
            n -= int_n[idx]
    
    return n
            
print(romanToInt('III'))
            