# -*- coding: utf-8 -*-
"""
Created on Mon Aug 26 10:07:47 2019

@author: Administrator
"""

def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        
        if len(nums1)==0:
            nums1 = nums2
        else:
            i,j = 0,0
            while i<len(nums1) or j<len(nums2):
                if i==len(nums1):
                    nums1.append(nums2[j])
                    i += 1
                    j += 1
                elif j==len(nums2):
                    break
                else:
                    if nums1[i]<nums2[j]:
                        i = min(i+1, len(nums1))
                    else:
                        nums1.insert(i, nums2[j])
                        i += 1
                        j += 1
        
        _len = len(nums1)
        if _len%2==0:
            return (nums1[int(_len/2-1)]+nums1[int(_len/2)])/2
        else:
            return nums1[_len//2]