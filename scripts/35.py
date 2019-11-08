# -*- coding: utf-8 -*-
"""
Created on Fri Nov  1 20:30:05 2019

@author: Administrator
"""

'''
二分查找法：
(1)要注意在开始时首尾两端的处理
(2)要注意在终点处(l+1=r)的处理
'''

class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        l,r = 0,len(nums)-1
        if target<=nums[l]:			# 首尾两端的处理
            return l
        if target==nums[r]:
            return r
        if target>nums[r]:
            return r+1
        
        while(l<r-1):				# 循环结束的条件
            m = int((l+r)/2)
            if target<nums[m]:
                r = m
            elif target>nums[m]:
                l = m
            else:
                return m
        
        return l+1					# 终点位置处的处理

print(Solution().searchInsert([1,3,5,7,9], 10))
        