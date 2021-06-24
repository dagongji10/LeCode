# -*- coding: utf-8 -*-

'''
@ Time   : 2021/6/23 20:14
@ Author : dagongji09
@ File   : 66.py
'''

from typing import List

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        digits = [0] + digits
        forward = [0 for i in range(len(digits))]
        forward[-1] = 1

        for i in range(len(digits) - 1, -1, -1):
            print(i, digits, forward)
            if forward[i] == 0:
                break
            tmp = digits[i] + forward[i]
            digits[i] = tmp % 10

            if i == 0:
                break
            forward[i - 1] = tmp // 10

        if digits[0] == 0:
            digits = digits[1:]

        return digits


a = Solution()
print(a.plusOne([9]))
