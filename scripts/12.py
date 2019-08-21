# -*- coding: utf-8 -*-
"""
Created on Wed Aug 21 09:44:18 2019

@author: Administrator
"""

def intToRoman(num: int) -> str:
    region = [1000, 900, 500, 400, 
              100, 90, 50, 40, 
              10, 9, 5, 4, 1]
    roman = ['M', 'CM', 'D', 'CD',
             'C', 'XC', 'L', 'XL',
             'X', 'IX', 'V', 'IV', 'I']
    n = num
    r = ''
    while(n>0):
        for i in region:
            if n>=i:
                d = i
                break
        
        k = int(n/d)
        n = n%d
        r += roman[region.index(d)]*k
    return r
    
print(intToRoman(1994))