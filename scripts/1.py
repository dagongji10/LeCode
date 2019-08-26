# -*- coding: utf-8 -*-
"""
Created on Mon Aug 26 09:59:21 2019

@author: Administrator
"""

def twoSum(nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for i,num in enumerate(nums):
            other = target - num
            left = nums[i+1:]
            if other in left:
                return i, left.index(other)+i+1
                
        return None
    
print(twoSum([2, 7, 11, 15], 9))