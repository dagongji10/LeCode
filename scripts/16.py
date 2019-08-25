"""
Created on Sun Aug 25 12:17:50 2019
@author: 短腿伊斯科22
"""

# -*- coding: utf-8 -*-

'''
这道题的解法同 3sum 相类似,还是使用"双指针法",只是在判断时条件为三数和与目标值的差
(1)如果 3sum-target<0：左指针往右走,找到不同的值(去重);与之前的最小距离比较,判断是否找到当前最小距离
(2)如果 3sum-target>0：右指针往左走,找到不同的值(去重);与之前的最小距离比较,判断是否找到当前最小距离
(3)如果 3sum-target=0：结束,返回target
'''


def threeSumClosest(nums, target) -> int:
    nums = sorted(nums)
    
    _sum = nums[0]+nums[1]+nums[2]
    for i,a in enumerate(nums):
        if i>0 and a==nums[i-1]:
            continue
        
        l = i+1
        r = len(nums)-1
        while(l<r):
            b = nums[l]
            c = nums[r]
            
            dis = a+b+c-target
            if dis<0:
                while(l<r and nums[l+1]==b):
                    l +=1
                l += 1
            elif dis==0:
                return target
            elif dis>0:
                while(l<r and nums[r-1]==c):
                    r -= 1
                r -= 1
                
            if abs(dis)<abs(_sum-target):
                _sum = a+b+c
                
    return _sum

print(threeSumClosest([1,1,1,0], 100))
                