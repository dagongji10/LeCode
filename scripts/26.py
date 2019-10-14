# -*- coding: utf-8 -*-
"""
Created on Mon Oct 14 19:58:56 2019

@author: Administrator
"""

'''
使用双指针法,第一个指针用来记录当前元素,第二个指针用来查找下一个不同元素
'''

class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n,i,j = 1,0,1
        while(i<len(nums)-1 and j<len(nums)):
            if nums[i]==nums[j]:
                j += 1
            else:
                nums[i+1] = nums[j]
                n += 1
                i += 1
                j += 1
        return n

a = [1,1,1,2,2,3,3,3,3,4,5,9,9,99]
print(Solution().removeDuplicates(a))
            