"""
Created on Sun Aug 25 13:22:48 2019
@author: 短腿伊斯科22
"""

# -*- coding: utf-8 -*-

'''
将每一个组合转换成字母在按键上的索引,具体来说如果输入是"23",那么组合就应该是['00', '01', '02', '10', '11', '12', '20','21', '22']
这看起来是不是像三进制数？想一下十进制转换成二进制是怎么做的？辗转相除,然后将余数组合就行,这里无非就是进制不是2而已
那么进制是3吗？其实进制是按键上字母的数量,可能是3,也可能是4,这样一想就简单了

先计算总共有多少种组合,然后依次计算每一种组合的索引组合,也就是通过辗转相除来计算

'''


def letterCombinations(digits: str):
    if digits=='':
        return []
    
    _map = ['abc', 'def', 'ghi', 'jkl',
            'mno', 'pqrs', 'tuv', 'wxyz']
    
    _s = [_map[int(i)-2] for i in digits]
#    out = [i for i in _s[0]]
#    
#    _c = 0
#    for i in range(1, len(_s)):
#        t = []
#        for j in range(len(out)):
#            for k in _s[i]:
#                t.append(out[j]+k)
#                _c += 1
#        out = t
#    print(out, len(out), _c)
    
    _c = 1
    for i in _s:
        _c = _c*len(i)
        
    cou = 0
    out = []
    for i in range(_c):
        idx = ''
        m = i
        for j in _s:
            idx += j[m%len(j)]
            m = int(m/len(j))
        cou += 1
        out.append(idx)
    return out
            
    
print(letterCombinations("234"))