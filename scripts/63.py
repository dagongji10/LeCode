# -*- coding: utf-8 -*-

'''
@ Time  : 2021/4/2/0002 17:39
@ Author: dagongji09
@ File  : 63.py
'''

'''
题目：
一个机器人位于一个 m x n 网格的左上角 （起始点在下图中标记为“Start” ）。
机器人每次只能向下或者向右移动一步。机器人试图达到网格的右下角（在下图中标记为“Finish”）。
现在考虑网格中有障碍物。那么从左上角到右下角将会有多少条不同的路径？

分析：
此题跟上一道多了一个约束；可能随机出现的障碍物
在没有这个约束的情况下，我们是把左边、上边全部置为1，默认都是可以到达的
在有这个约束的情况下，左边、上边只能根据前一个路径得到，不能置为默认值
在判断左边、上边的路径值的时候，需要注意数组索引不能越界

'''


class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m, n = len(obstacleGrid), len(obstacleGrid[0])
        res = [[0 for i in range(n)] for j in range(m)]

        # 挨个递进
        for i in range(m):
            for j in range(n):
                # 如果有障碍物，则到达此位置的路径为0
                # 如果没有障碍物，则根据左边、上边的已知路径来求解，注意不能越界
                if obstacleGrid[i][j] == 1:
                    continue
                elif i == 0 and j == 0:
                    res[i][j] = 1
                elif i == 0:
                    res[i][j] = res[i][j - 1]
                elif j == 0:
                    res[i][j] = res[i - 1][j]
                else:
                    res[i][j] = res[i - 1][j] + res[i][j - 1]

        return res[-1][-1]