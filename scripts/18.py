"""
Created on Sun Aug 25 16:24:23 2019
@author: 短腿伊斯科22
"""

# -*- coding: utf-8 -*-

def fourSum(nums, target):
    nums = sorted(nums)
    
    l0 = 0
    r0 = len(nums)
    while(r0-l0>2):
        if 
        a,d = nums[l0],nums[r0]
        
        l1 = l0+1
        r1 = r0-1
        while(l1<r1):
            b,c = nums[l1],nums[r1]
            _sum = a+b+c+d
            if _sum==target:
                pass
            elif _sum<target:
                pass
            elif _sum>target:
                pass
        
        