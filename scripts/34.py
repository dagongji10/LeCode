# -*- coding: utf-8 -*-
"""
Created on Tue Nov 26 19:55:29 2019

@author: Administrator
"""

'''
题目:
    找到升序数组中某个元素的起始/终止位置
    
思路:
    先找起始位置，再找终止位置，时间复杂度 O(logN)

收获:
    通过此题要真正掌握二分查找的思想，"思路很简单,细节是魔鬼"
'''


class Solution:
    def searchRange(self, nums, target):
        low = self.findLeft(nums, target)
        high = self.findRight(nums, target)
        return [low, high]
        
    # 二分查找的基本框架，注意几个点;以后二分查找就按照这个模板来写
    def findLeft(self, nums, target):
        low = 0                                     # 1. 左右端点的初始化
        high = len(nums)-1
        
        while(low<=high):                           # 2. 终止条件，要考虑 = 的情况
            mid = (low+high)>>1                     # 3. 中点的计算，用位操作符更省时间
            if nums[mid]<target:
                low = mid+1                         # 4. 没找到就移动一位，需要 +/- 操作
            elif nums[mid]>target:
                high = mid-1
            else:                                   # 5. 等于时怎么处理，可能要考虑多种情况
                if mid==low or nums[mid-1]!=target:
                    return mid
                else:
                    high = mid-1
        return -1
    
    def findRight(self, nums, target):
        low = 0
        high = len(nums)-1
        
        while(low<=high):
            mid = (low+high)>>1
            if nums[mid]<target:
                low = mid+1
            elif nums[mid]>target:
                high = mid-1
            else:
                if mid==high or nums[mid+1]!=target:
                    return mid
                else:
                    low = mid+1
        return -1
    

print(Solution().searchRange([2,5,5,5,6,6], 1))