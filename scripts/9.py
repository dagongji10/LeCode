# -*- coding: utf-8 -*-
"""
Created on Thu Aug 15 14:17:42 2019

@author: Administrator
"""

def isPalindrome(x: int) -> bool:
    if x<0:
        return False                        # 不能用'false'代替
    else:
        s = '#' + '#'.join(str(x)) + '#'    # 也可以直接用字符串倒序然后判断是否相等
        center = int(len(s)/2)
        p = 1
        while(center-p>=0):
            if s[center-p]==s[center+p]:
                p += 1
            else:
                return False
        return True