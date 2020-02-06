"""
Created on Wed Feb  5 21:41:21 2020
@author: 短腿伊斯科22
"""

# -*- coding: utf-8 -*-

'''
题目:
    融合区间
    
关键:
    先对二维区间列表进行排序，sorted 的使用

'''

class Solution:
    def merge(self, intervals):
        if intervals==[]:
            return []
        
        # 给二维列表排序：start为主关键字，end为次关键字
        intervals = sorted(intervals, key=(lambda x:[x[0], x[1]]))
        
        res = [intervals[0]]                # 保存结果
        for i in range(1, len(intervals)):  # 一次遍历
            t0 = res[-1]                    # 取融合区间的最后一个区间
            t1 = intervals[i]               # 取待融合区间
            if t1[0]<=t0[1]:                # 如果有交集
                if t1[1]<=t0[1]:            # 判断是否为完全包含关系
                    continue
                else:                       # 不是完全包含
                    t = [t0[0], t1[1]]
                    res[-1] = t             # 更新最后一个区间
            else:
                res.append(t1)              # 如果没有交集，就直接添加
        
        return res
                
a = Solution()
b = [[10,13],[1,4],[4,5],[8,9],[12,14]]
a.merge(b)