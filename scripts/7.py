# -*- coding: utf-8 -*-
"""
Created on Wed Aug 14 16:55:13 2019

@author: Administrator
"""

def reverse(x: int) -> int:
    if x<0:
        x = -x
        c = '-'
    else:
        c = ''
    
    str_x = str(x)
    reverse_x = c + str_x[::-1]
    int_reverse_x = int(reverse_x)
    
    if int_reverse_x<-2**31 or int_reverse_x>2**31-1:   # 32位有符号整型的范围[-2^31, 2^31-1]
        return 0
    
    return int_reverse_x

print(2**31-1)
print(reverse(1563847412))