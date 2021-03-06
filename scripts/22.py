# -*- coding: utf-8 -*-
"""
Created on Thu Aug 29 15:53:52 2019

@author: Administrator
"""

'''
首先要清楚几个规则：
a.无论多少对括号，第一个符号肯定是"("
b.从起始位置截取任意的子字符串，"("数量肯定不小于")"
c.从起始位置截取任意的子字符串，如果"("的数量等于指定的括号对数，那么剩余的字符肯定都是")"

现在来看一下当有三对括号的情况：
(1)根据 a 可以得到第一个字符"("，接下来第二个字符有两种可能，所以前两个字符的组合就有两种可能："((", "()"
(2)对于"((", 第三个字符也有两种可能，那么由它衍生出来的三字符子串也有两种可能："(((", "(()"
   对于"()", 因为规则 b 的存在，第三个字符就只有一种可能了，那么由它衍生出来的三字符子串就是："()("
   这样一来，三字符子串总共有三种情况："(((", "(()", "()("
(3)对于"(((", 因为规则 c 的存在，右边可以直接补齐，全为")"，最终的结果就是"((()))"
   对于"(()", 第四个字符可以有两种可能，那么由它衍生出来的四字符子串就是："(()(", "(())"
   对于"()(", 第四个字符也有两种可能："()((", "()()"
   这样一来，我们最终找到一组符合要求的："((()))", 以及四组衍生子字符串："(()(", "(())", "()((", "()()"
(4)以此类推，每次添加一个字符，直到所有组合都满足要求

在根据子字符串添加下一个字符时，需要判断有几种情况，说白了就是能不能添加")"，因为如果不满足规则 c ，那么"("是肯定可以添加的
要能够添加")"，根据规则 b，子字符串中")"的数量必须小于"(", 否则就不能添加")";所以需要时刻记录子字符串中左右括号的数量
因此，考虑将子字符串和记录括号数量的数字组成一个元组，来表示每一种可能的括号组合
'''


def generateParenthesis(n):
#    nodes = [('', 0, 0)]
#    res = []
#    while nodes:
#        n = nodes.pop()
#        if n[1] == N:
#            res.append(n[0]+')'*(n[1] - n[2]))
#            continue
#
#        nodes.append((n[0]+'(', n[1]+1, n[2]))
#            
#        if n[2] < n[1]:
#            nodes.append((n[0]+')',n[1], n[2]+1))
#    
#    return res
    
    nodes = [['(', 1, 0]]
    res = []
    
    for i in range(2, 2*n+1):
        _add = []
        _del = []
        for j,t in enumerate(nodes):
            if t[1]==n:
                res.append(t[0] + ")"*(t[1] - t[2]))
                _del.append(t)
                continue
            else:
                if t[2]<t[1]:
                    c = [t[0]+")", t[1], t[2]+1]
                    _add.append(c)
                
                t[0] += "("
                t[1] += 1
        nodes += _add
        for d in _del:
            nodes.remove(d)
                
    return res

print(generateParenthesis(2))