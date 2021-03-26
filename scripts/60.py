# -*- coding: utf-8 -*-

'''
@ Time  : 2021/3/26/0026 16:42
@ Author: dagongji09
@ File  : 60.py
'''

'''
题目：
给出集合 [1,2,3,...,n]，其所有元素共有 n! 种排列。按大小顺序列出所有排列情况，并一一标记，当 n = 3 时, 所有排列如下：
"123"
"132"
"213"
"231"
"312"
"321"
给定 n 和 k，返回第 k 个排列。


思考：
（1）n 个数字，每个数字作为第一位开头的有 (n-1)! 种情况，k/(n-1)! 就能判断第一位取哪个数字，假设取的是 t
（2）将 t 从上面的 n 个数字中去除，问题变为：剩下的 (n-1) 个数的排列中，取第 k%(n-1)! 个
'''


class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        import math

        d = [1, 2, 6, 24, 120, 720, 5040, 40320, 362880]
        nums = [i + 1 for i in range(n)]

        res = ''
        while (n > 0):
            # 判断取哪个数字
            t = nums[math.ceil(k / d[n - 2]) - 1]
            res += str(t)

            # 更新状态
            k = k % d[n - 2]
            nums.remove(t)
            n = len(nums)
        return res


Solution().getPermutation(3, 6)

