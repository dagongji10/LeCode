"""
Created on Mon Aug 26 21:44:09 2019
@author: 短腿伊斯科22
"""

# -*- coding: utf-8 -*-

def fourSum(nums, target):
    if len(nums)<4:
        return []
    
    idxs = {}
    ans = []
    for i in range(len(nums)-1):
        a = nums[i]
        for j in range(i+1, len(nums)):
            b = nums[j]
            _sum = a+b
            _diff = target-_sum
            
            if _diff in idxs:
                for t in idxs[_diff]:
                    m,n = t
                    if m!=i and m!=j and n!=i and n!=j:
                        tem = sorted([a, b, nums[m], nums[n]])
                        ans.append(tem)
            
            if _sum in idxs:
                idxs[_sum].append([i, j])
            else:
                idxs[_sum] = []
                idxs[_sum].append([i, j])
            
    ans = [list(t) for t in set(tuple(_) for _ in ans)]
    return ans
            
print(fourSum([-491,-487,-445,-436,-435,-429,-398,-385,-378,-370,-367,-353,-344,-325,-284,-279,-269,-262,-189,-182,-164,-152,-123,-118,-110,-64,-55,-48,-45,9,14,17,47,54,64,64,70,94,114,144,161,171,188,194,205,241,271,284,312,341,363,376,407,410,413,441,442,455,476,492], -1529))