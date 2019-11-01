# -*- coding: utf-8 -*-
"""
Created on Fri Nov  1 20:30:05 2019

@author: Administrator
"""

'''
二分查找法
'''

class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        l,r = 0,len(nums)-1
        if target<=nums[l]:
            return l
        if target==nums[r]:
            return r
        if target>nums[r]:
            return r+1
        
        while(l<r-1):
            m = int((l+r)/2)
            if target<nums[m]:
                r = m
            elif target>nums[m]:
                l = m
            else:
                return m
        
        return l+1

print(Solution().searchInsert([1,3,5,7,9], 10))
        