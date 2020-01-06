# -*- coding: utf-8 -*-

'''
题目:
    下一个数从上一个数观察计算得来,计算原则是看有几个相邻字符是相同的
    例如: f(n-1)=111221, 则 f(n)=312211，, 因为有 f(n-1) 是由3个1、2个2、1个1组成
思路:
    递归法,每次找到上一个数,遍历时记录重复数字和重复数量,然后将数量数字变成字符作为当前数字的组成部分
'''


class Solution:
    def countAndSay(self, n):
        if n==1:
            return '1'
        
        s = self.countAndSay(n-1)
        out = ''
        t = s[0]
        t_n = 0
        for i in range(len(s)):
            if s[i]==t:
                t_n += 1
            else:
                out += str(t_n)+t
                t = s[i]
                t_n = 1
                
        out += str(t_n)+t
        
        return out

print(Solution().countAndSay(10))