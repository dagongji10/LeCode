# -*- coding: utf-8 -*-
"""
Created on Wed Aug 21 17:54:25 2019

@author: Administrator
"""

def longestCommonPrefix(strs) -> str:
    s0_len = len(strs[0])
    
    pre = ''
    for i in range(s0_len):
        c = strs[0][i]
        for j in range(len(strs)):
            if i>=len(strs[j]) or strs[j][i]!=c:
                return pre
        pre += c
    
    return pre

print(longestCommonPrefix([""]))