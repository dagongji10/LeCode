"""
Created on Sat Aug 31 13:05:04 2019
@author: 短腿伊斯科22
"""

# -*- coding: utf-8 -*-

'''
从两个实例入手:"[(){}]"   "(([){]})"
使用栈的思想来解决是最好的：我们将"([{"视为正，将")]}"视为负，栈里面只会存入正号，用来跟提取到的符号作比较
具体来说，如果是正的就存入栈，如果是负的我们将它与栈顶相比较，如果匹配上了就将栈顶释放，接着寻找下一个
为什么有效呢？
（1）正负符号的匹配保证题目的条件一：左括号必须用相同类型的右括号闭合
（2）栈的先进后出的性质保证题目的条件二：左括号必须以正确的顺序闭合

'''

def isValid(s: str) -> bool:
    idx = {"(":")", "{":"}", "[":"]"}
    
    if len(s)%2!=0:
        return False
    
    _stack = []
    for i in range(len(s)):
        if s[i] in idx.keys():
            _stack.append(s[i])
        elif len(_stack)>0:
            t = _stack[-1]
            if s[i]!= idx[t]:
                return False
            else:
                _stack.pop()
        else:
            return False
                
    if len(_stack)!=0:
        return False
        
    return True

print(isValid("{({})[]}"))