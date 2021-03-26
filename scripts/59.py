# -*- coding: utf-8 -*-

'''
@ Time  : 2021/3/26/0026 16:26
@ Author: dagongji09
@ File  : 59.py
'''

'''
题目：
给你一个正整数 n ，生成一个包含 1 到 n2 所有元素，且元素按顺时针顺序螺旋排列的 n x n 正方形矩阵 matrix 。

方法：
按照 从左到右、从上到下、从右到左、从下到上 的顺序填充每一圈
'''

from typing import List


class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        res = [[0 for i in range(n)] for i in range(n)]
        t, b, l, r = 0, n - 1, 0, n - 1

        num = 1
        # 循环填充每一圈
        while (t < n / 2):
            # 从左到右
            for i in range(l, r + 1):
                res[t][i] = num
                num += 1
            # 从上到下
            for i in range(t + 1, b + 1):
                res[i][r] = num
                num += 1
            # 从右到左
            for i in range(r - 1, l - 1, -1):
                res[b][i] = num
                num += 1
            # 从下到上
            for i in range(b - 1, t, -1):
                res[i][l] = num
                num += 1

            t, b, l, r = t + 1, b - 1, l + 1, r - 1

        return res


res = Solution().generateMatrix(3)
print(res)
