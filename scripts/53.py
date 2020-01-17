# -*- coding: utf-8 -*-
"""
Created on Fri Jan 17 17:16:57 2020

@author: Administrator
"""

'''
题目:
    最大子序列的和

分析:
    (1)遍历每一个元素，第一层遍历时将元素看成子序列的起点，然后遍历剩下的部分，找到那个能使子序列和最大的终点；
    (2)进一步的，我们发现：如果前面的当前元素之前元素的和小于0，那么起点还不如直接设在当前元素，所以可以设置一个缓存，专门存储之前序列的和，用来确定当前元素所属的起点
    (3)假设数组 d 缓存了每个元素之前相邻的序列和，那么就可以根据这个和的正负性来判断要不要将当前元素作为序列的起点
    
核心:
    d[i] = d[i-1]>=0 ? d[i-1]+nums[i] : nums[i]
'''

class Solution:
    def maxSubArray(self, nums):
        d = [1-2<<31 for i in range(len(nums))] # 缓存当前元素之前最大相邻子序列和
        max_ = -1                               # 存储最大子序列和的结果
        for i in range(len(nums)):              # 遍历
            if i==0:                            # 序列的头部
                d[i] = nums[i]
                max_ = d[i]
                continue
            
            if d[i-1]>0:        
                d[i] = d[i-1]+nums[i]           # 相邻子序列的和如果大于0，那就从之前的元素开始
            else:
                d[i] = nums[i]                  # 相邻子序列的和如果不大于0，还不如直接从当前元素开始
                
            if max_<d[i]:                       # 判断是否是最大子序列和
                max_ = d[i]
                
        return max_
            
a = Solution()
a.maxSubArray([-2])