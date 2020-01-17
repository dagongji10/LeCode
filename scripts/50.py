# -*- coding: utf-8 -*-
"""
Created on Fri Jan 17 15:03:14 2020

@author: Administrator
"""

'''
题目:
    计算 pow(x, n)

分析:
    (1)用递归：f(x, n)=x*f(x, n-1)
    (2)pow(3, 10)=pow(pow(3, 5), 2),启发：将 n 除以2，只需先计算 pow(x, n/2)，然后将结果平方，减少递归的次数 
    (3)利用二进制：将 n 表示为二进制的形式，从低位到高位一步步计算

举例:pow(2, 10)
    10 的二进制表示：1010，也就是说 pow(3,10) = (0*pow(3,1)) * (1*pow(3,2)) * (0*pow(3,4)) * (1*pow(3,8))
    计算 pow(x, 2**i) 时要将结果保存下来，用来计算下一步的 pow(x, 2**(i+1))

'''

class Solution:
    def myPow(self, x, n):
        if x==1:
            return 1
        elif n<0:
            return 1.0/self.myPow(x, -n)
        elif n==0:
            return 1
        else:
            n_bin = bin(n).lstrip('0b')
            ans = 1
            p = 1
            for idx,_ in enumerate(n_bin):
                if idx==0:
                    p = x                               # 最低位直接赋值，初始化
                else:
                    p = p*p                             # 记录每一位的值
                
                if int(n_bin[len(n_bin)-1-idx])==1:     # 注意从低位往高位计算
                    ans = ans * p
            
            return ans
                
a = Solution()
print(a.myPow(3.0, -10))