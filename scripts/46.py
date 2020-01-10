# -*- coding: utf-8 -*-
"""
Created on Fri Jan 10 14:55:35 2020

@author: Administrator
"""

'''
题目:
    输出一个无重复数组的全排列
    
思路:
    插入法:
        两元素数组 >>> 往一个元素的数组插入一个数字
        三元素数组 >>> 往两个元素的数组插入一个数字
        四元素数组 >>> 往三个元素的数组插入一个数字
        ...
'''

class Solution:
    def permute(self, nums):
        if nums==[]:
            return []
        
        res = [[nums[0]]]                                   # 初始情况只包含一个元素，后续排列就是在这一个元素的基础上不断插入新的元素
        for i in range(1, len(nums)):                       # 遍历后续元素
            tmp = []
            for j in range(len(res)):                       # 遍历已存在的排列
                new_res = self.insert_num(nums[i], res[j])  # 将元素插入排列
                tmp += new_res
            res = tmp
        return res
    
    
    def insert_num(self, num, nums):
        new_nums = []
        for i in range(len(nums)+1):
            t = nums.copy()                                 # 此处必须用copy()，否则始终是作用在原始排列上，不会产生新的排列
            t.insert(i, num)
            new_nums.append(t)
        return new_nums

a = [1,2,3,4,5,6]
b = Solution()
b.permute(a)