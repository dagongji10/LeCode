# -*- coding: utf-8 -*-
"""
Created on Fri Nov 22 16:20:08 2019

@author: Administrator
"""

'''
二分查找的变形：将升序数组从某个节点错位
二分查找的关键在于 mid 和 target 的相对位置，这里的错位增加了相对位置判断的复杂性
将整个数组分成前后两部分，ll-lr 和 rl-rr，两部分都是升序，但是 l 部分大于 r 部分
target的位置为 p, mid 简写为 m, 二者总共有6种位置关系:
    (1)ll p m lr , rl rr >> r = m
    (2)ll m p lr , rl rr >> l = m
    (3)ll lr , rl p m rr >> r = m
    (4)ll lr , rl m p rr >> l = m
    (5)ll p lr , rl m rr >> r = m
    (6)ll m lr , rl p rr >> l = m
'''

class Solution:
    def search(self, nums, target):
        if target==nums[0]:
            return 0
        if target==nums[-1]:
            return len(nums)-1
        
        l = 0
        r = len(nums)-1
        while(l+1<r):
            m = int((l+r)/2)
            if target==nums[m]:
                return m
            elif target<nums[m] and nums[m]<nums[r]:
                r = m
            elif target>nums[r] and nums[m]<nums[r]:
                r = m
            elif target>nums[r] and nums[m]>target:
                r = m
            else:
                l = m
        
        return -1

print(Solution().search([4,1], 4))
            