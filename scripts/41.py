# -*- coding: utf-8 -*-
"""
Created on Mon Jan  6 20:04:22 2020

@author: Administrator
"""

'''
题目:
    找到一组未排序的数组中没有出现的最小的正整数
    
思路:
    因为要判断元素是否在数组中，如果用list来判断那么时间复杂度肯定超过O(n)，考虑将list变成集合set再去判断

'''

class Solution:
    def firstMissingPositive(self, nums):
        if nums==[]:
            return 1
        
        res = 1
        nums_set = set(nums)                # 偷懒的操作
        for i in range(len(nums_set)):
            i_next = i+1
            if i_next in nums_set:          # 判断最小正整数是否出现，list时间复杂度是O(n)，set时间复杂度是O(1)
                res += 1
            else:
                return res
            
        return res
    
a = Solution()
b = []
c = a.firstMissingPositive(b)
print(c)