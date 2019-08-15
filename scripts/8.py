# -*- coding: utf-8 -*-
"""
Created on Wed Aug 14 17:36:28 2019

@author: Administrator
"""

def myAtoi(s: str) -> int:
    s = s.lstrip(' ')           # 去掉首端的空格
    if len(s)==0:               # 长度为0则返回
        return 0
    
    if s[0] in '+' or s[0] in '-':                                  # 1.有符号
        if 1<len(s) and s[1] in '0123456789':                       # 1.1符号下一个为数字
            start_idx = 0
            end_idx = 1
            while(end_idx<len(s) and s[end_idx] in '0123456789'):
                end_idx += 1
            if end_idx<len(s):
                num = int(s[start_idx:end_idx])
            else:
                num = int(s[start_idx:])
        else:                                                       # 1.2符号下一个不为数字
            num = 0
    elif s[0] in '0123456789':                                      # 2.无符号
        start_idx = 0
        end_idx = 1
        while(end_idx<len(s) and s[end_idx] in '0123456789'):
            end_idx += 1
        if end_idx<len(s):
            num = int(s[start_idx:end_idx])
        else:
            num = int(s[start_idx:])
    else:
        return 0
    
    if num<-2**31:          # 溢出判断
        return -2**31
    elif num>2**31-1:
        return 2**31-1
    else:
        return num
