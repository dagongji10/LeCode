# -*- coding: utf-8 -*-
"""
Created on Wed Aug 21 20:09:30 2019

@author: Administrator
"""

'''
2sum:
如果是两数之和呢？例如找到两数之和为0？
暴力求解就是找到所有两数组和,判断二者之和是否为0,这是最蠢的方法
好一点的方法,先将

遍历每一个元素,遍历时看它的相反数是不是在数组里面,在的话把这两个元素从数组里拿掉,继续遍历
这种称为哈希思想,本来它应该是最快的,时间复杂度为O(n),但是python里面"判断一个元素是否在列表中"时间复杂度是O(n)不是O(1),所以实现出来最坏的时间复杂度还是O(n2)
要用哈希的话,不能用"判断元素在列表中",而要将列表变成集合,然后判断"元素在集合中",后者的时间复杂度是O(1)


3sum:
受到"2sum"问题的启发,可以先遍历找两个数,然后判断第三个数是不是在数组里面,这样的时间复杂度就是O(n2)
我们再来优化一下：比如让数组先排个序,从小到大,然后让a<b<c,a在先固定,b在其右边往右走,看c是否存在于数组中,当-(a+b)<b时就可以结束这一组,让a往右走一个;直到a>=0结束

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
    

