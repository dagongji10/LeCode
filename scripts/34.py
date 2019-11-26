# -*- coding: utf-8 -*-
"""
Created on Tue Nov 26 19:55:29 2019

@author: Administrator
"""

class Solution:
    def searchRange(self, nums, target):
        l,r = 0,len(nums)-1
        print(l, r)
        
        if l==r:
            if nums[l]==target:
                return l,l
            else:
                return -1,-1
        
        if l+1==r:
            if nums[l]==target and nums[r]!=target:
                return l,l
            elif nums[l]==target and nums[r]==target:
                return l,r
            elif nums[l]!=target and nums[r]!=target:
                return -1,-1
            elif nums[l]!=target and nums[r]==target:
                return r,r
            
        m = int((l+r)/2)
        
        
        if nums[l]==target and nums[r]==target:
            pass
        elif nums[l]==target and nums[r]!=target:
            if nums[m]==target:
                r = m+self.searchRange(nums[m:r], target)[1]
            else:
                r = l+self.searchRange(nums[l:m], target)[1]
        elif nums[l]!=target and nums[r]==target:
            if nums[m]==target:
                l = l+self.searchRange(nums[l:m], target)[0]
            else:
                l = m+self.searchRange(nums[m:r], target)[0]
        elif nums[l]!=target and nums[r]!=target:
            if nums[m]<target:
                l,r = self.searchRange(nums[m:r],target)
                l += m
                r += m
            elif nums[m]>target:
                l,r = self.searchRange(nums[l:m],target)
                l += l
                r += l
            else:
                l = l+self.searchRange(nums[l:m], target)[0]
                r = m+self.searchRange(nums[m:r], target)[1]
        
        
        return l,r

print(Solution().searchRange([5,7,7,8,8,10], 10))