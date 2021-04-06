# -*- coding: utf-8 -*-

'''
@ Time  : 2021/4/2/0002 17:34
@ Author: dagongji09
@ File  : 62.py
'''


'''
题目：
一个机器人位于一个 m x n 网格的左上角 （起始点在下图中标记为 “Start” ）。
机器人每次只能向下或者向右移动一步。机器人试图达到网格的右下角（在下图中标记为 “Finish” ）。
问总共有多少条不同的路径？

分析：
类似于上楼梯，上楼梯是一维的，这个是二维的，但是解决方案是一样的，挨个递进就行
'''

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        a = [[1 for i in range(n)] for j in range(m)]

        # 挨个递进
        for i in range(1, m):
            for j in range(1, n):
                a[i][j] = a[i - 1][j] + a[i][j - 1]

        return a[-1][-1]