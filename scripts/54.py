"""
Created on Wed Feb  5 15:11:12 2020
@author: 短腿伊斯科22
"""

# -*- coding: utf-8 -*-


'''
题目:
    按照顺时针螺旋，输出数组
    
思路:
    当前元素延续上一个元素的前进方向，除非这种延续会产生错误；
    如果产生错误，就要调整前进方向，调整的策略是在固定前进方向集合中轮循
    
注意:
    何时终止程序？有可能是在数组的外边上，有可能是在数组的内部

'''

class Solution:
    def spiralOrder(self, matrix):
        if matrix==[]:
            return []
        
        m = len(matrix)
        n = len(matrix[0])
        
        v = [(0,1), (1,0), (0,-1), (-1,0)]  # 前进方向集合
        
        i,j,t = 0,0,0
        res = []
        while(True):
            res.append(matrix[i][j])
            matrix[i][j] = True             # 已经输出的元素做一个记录
            
            # 一行、一列
            if m==1 and j+1==n:
                break
            if n==1 and i+1==m:
                break
            # 两行、两列
            if m==2 and i==1 and j==0:
                break
            if n==2 and i==1 and j==0:
                break
            # 三行/列以上
            if m>=3 and n>=3:
                try:
                    if matrix[i-1][j]==True and matrix[i+1][j]==True and matrix[i][j-1]==True and matrix[i][j+1]==True:
                        break
                except Exception as e:
                    pass
            
            i_t = i+v[t][0]         # 延续前一个元素的前进方向
            j_t = j+v[t][1]
            if i_t>=0 and i_t<=len(matrix)-1 and j_t>=0 and j_t<=len(matrix[0])-1 and matrix[i_t][j_t]!=True:   # 延续是可靠的
                i = i_t             # 更新元素位置
                j = j_t
            else:                   # 延续策略不可靠
                t = (t+1)%4         # 找下一个前进方向
                i = i+v[t][0]       # 更新元素位置
                j = j+v[t][1]
            
        return res
        
a = Solution()
b = [
  [1, 2, 3, 4],
  [5, 6, 7, 8],
  [9,10,11,12],
  [13,14,15,16]
]

print(a.spiralOrder(b))
