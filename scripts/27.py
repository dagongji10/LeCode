# -*- coding: utf-8 -*-
"""
Created on Mon Oct 14 20:35:01 2019

@author: Administrator
"""

'''
还是双指针法：
26题是排序数据去除相邻的重复元素,这一题没有排序,但是是去除指定元素,不同之处在于什么时候去除,也就是执行去除操作时的判断不一样而已
'''

class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        n,i,j = 0,0,0
        while(i<len(nums) and j<len(nums)):
            if nums[j]==val:                # 如果等于指定元素，就执行去除操作
                j += 1                      # 往后搜索相当于去除
            else:
                nums[i] = nums[j]
                n += 1
                i += 1
                j += 1
        return n

a = [3,3,0,1,12,3,3,7,3,4,3,5,3]
print(Solution().removeElement(a,3))