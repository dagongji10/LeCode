"""
Created on Sun Jan 12 14:39:14 2020
@author: 短腿伊斯科22
"""

# -*- coding: utf-8 -*-

'''
题目:
    将矩阵顺时针旋转90度

分析:
    (1)首先，顺时针旋转90度以后，元素的索引值是怎么变化的？
    假设以矩阵中心((n-1)/2, (n-1)/2)为坐标原点，旋转前元素的位置为 (x,y)，那么旋转之后的坐标应该是
        (x, y) >> (y, n-1-x)
    (2)如何在原始矩阵上交换元素的值？
    考虑按照一层层的方式交换，从最外层逐步向最里层发展，每次旋转时可以同时交换四条边上的对应元素（根据上面的公式可以推导出这四个元素的位置）
    假设现在旋转的是第 i 层，那么需要旋转的元素就是第 i 行的 (i ~ n-1-i) 元素，用一个for循环就可以解决

'''


class Solution:
    def rotate(self, matrix):
        size = len(matrix)
        
        if size<=1:
            return matrix
        
        # 以层的形式旋转,i=0为最外层
        for i in range(int(size/2.0)):
            for j  in range(i, size-1-i):                   # 要注意这里第 i 层元素的范围，并不是直接到第 i 行的末尾
                tmp = matrix[j][size-1-i]
                matrix[j][size-1-i] = matrix[i][j]          # (i, j)           > (j, size-1-i)
                matrix[i][j] = tmp
                
                tmp = matrix[size-1-i][size-1-j]
                matrix[size-1-i][size-1-j] = matrix[i][j]   # (j, size-1-i)    > (size-1-i, size-1-j)
                matrix[i][j] = tmp
                
                tmp = matrix[size-1-j][i]
                matrix[size-1-j][i] = matrix[i][j]          # (size-1-i, n-1-j)> (size-1-j, i)
                matrix[i][j] = tmp                          # (size-1-j, i)    > (i, j)
                    

a = [[5,1,9,11],
     [2,4,8,10],
     [13,3,6,7],
     [15,14,12,16]]
b = Solution()
b.rotate(a)
print(a)