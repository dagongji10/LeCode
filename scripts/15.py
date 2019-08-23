# -*- coding: utf-8 -*-
"""
Created on Wed Aug 21 20:09:30 2019

@author: Administrator
"""

'''
2sum:
如果是两数之和呢？例如找到两数之和为0？
(1)暴力求解就是找到所有两数组和,判断二者之和是否为0,该方法时间复杂度为O(n2)
(2)好一点的方法,先将数组进行排序,排序时间复杂度为O(n*logn),然后指定首尾两个指针往中间走,一遍下来就能找到所有的组合,成为"双指针法"
该方法之所以有效,依赖于指针行进的规则:二者之和小于0则表示要需要增大其中一个,那就然左指针往右走(增大)；否则让右指针往左走(减小),最终的时间复杂度为O(n*log(n))
(3)还有一种方法,"哈希值表",先遍历一遍数组,遍历时查看元素需要的搭档是否在数组中,时间复杂度为O(n)
这种方法有一个问题,python在判断一个元素是否在列表中时时间复杂度是O(n)不是O(1),所以做这个判断时可以将数组复制一份到集合内,集合的判断是O(1)

3sum:
(1)"双指针法":还是对数组进行排序,然后先固定第一个数,运用双指针去找剩下的两个数,双指针本身的时间复杂度是O(n),加上遍历的时间复杂度就是O(n2)
在2sum问题中双指针的时间复杂度是O(n*logn),因为要排序;3sum问题中最终的时间复杂度为O(n2)
(2))"哈希值表":2sum问题是遍历一个数,这里可以先遍历找两个数,然后判断第三个数是不是在数组里面,这样的时间复杂度就是O(n2)

优化:
(1)相邻元素如果相等,需要去重(需要考虑三个位置的数值)；
(2)如果最小值大于0就可以直接终止搜索
'''

def threeSum(nums):
    nums = sorted(nums)
    
    g = []
    for i in range(len(nums)):
        a = nums[i]
        if a>0:
            break
        if i>0 and a==nums[i-1]:
            continue
        
#        for j in range(i+1, len(nums)):
#            b = nums[j]
#            if -(a+b)<b:
#                break
#            if -(a+b) in nums[j+1:] and [a, b, -(a+b)] not in g:
#                g.append([a, b, -(a+b)])
        
        l = i+1
        r = len(nums)-1
        while(l<r):
            _sum = a+nums[l]+nums[r]
            if _sum==0:
                g.append([a, nums[l], nums[r]])
                while(l<r and nums[l]==nums[l+1]):
                    l += 1
                while(l<r and nums[r]==nums[r-1]):
                    r -= 1
                l += 1
                r -= 1
            elif _sum<0:
                l += 1
            elif _sum>0:
                r -= 1
    return g
        
    
print(threeSum([0, 0,0]))
    

