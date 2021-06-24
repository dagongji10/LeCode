# -*- coding: utf-8 -*-

'''
@ Time   : 2021/6/23 20:40
@ Author : dagongji09
@ File   : 67.py
'''


class Solution:
    def addBinary(self, a: str, b: str) -> str:
        a = [0] + [int(t) for t in list(a)]
        b = [0] + [int(t) for t in list(b)]
        c = [0 for i in range(len(a))]

        for i in range(len(a) - 1, 0, -1):
            tmp = a[i] + b[i] + c[i]
            a[i] = tmp % 2
            c[i - 1] = tmp // 2

        return ''.join([str(t) for t in a])

p = Solution()
p.addBinary('1011', '11')