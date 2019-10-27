"""
Created on Sun Oct 27 16:14:54 2019
@author: 短腿伊斯科22
"""

# -*- coding: utf-8 -*-

'''
(1)如何判断两数是否同号：采用异或,若 (a^b)<0 则两者异号(符号相反时异或值小于0)
(2)如何得到一个数的相反数：~X=-X-1, 所以 -X=~X+1

两数相除不使用除法、乘法、求模运算符：
除法的一般计算就是将被除数不断减去除数，看有多少个除数，这样的循环次数太多；
假设：m/n=k...p
(1)考虑将m对半划分t次,每一份都大于n;刚好到t+1时每一份小于n
(2)这也就相当于,如果将n放大t次,每次变为原来的两倍,他还是小于m的,但是如果再放大一次那就超过m了
(3)把m中n*(2^t)也就是n>>t这一部分拿出来,剩下的部分肯定不会大于n>>t,那就顺着t再去找剩下这一部分对应的t

80 = 3*16 + 3*8 + 3*2 + 2
60 = 3*16 + 3*4
40 = 3*8  + 3*4 + 3*1 +1
20 = 3*4  + 3*2 + 2
10 = 3*2  + 3*1 + 1
'''


class Solution:
    def divide(self, dividend, divisor):
        flag = (dividend^divisor)<0
        if dividend<0:
            dividend = ~dividend + 1
        if divisor<0:
            divisor = ~divisor + 1
        
        if divisor==0:
            return None
        elif divisor>dividend:
            return 0
        else:
            result = 0
            t = 31
            while(t>=0):
                m = dividend>>t
                print(t,m)
                if m>=divisor:
                    result += 1<<t
                    dividend -= divisor<<t
                t -= 1
            
            if flag:
                result = -result
            
            if result<-(1<<31) or result>(1<<31)-1:
                return (1<<31)-1
            
            return result

print(Solution().divide(100,7))