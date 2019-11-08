# -*- coding: utf-8 -*-
"""
Created on Wed Nov  6 17:32:38 2019

@author: Administrator
"""

'''
题目:
    给定一个数字序列，找到该序列的所有重组序列中比它大的下一个序列
    eg. 43987 > 47389
    
解析:
    要找到一个比它大的序列，而且是刚好比它大的下一个，那就只能是选其中两个数交换位置
    选两个数交换位置要使整体变大，那要求交换时 低位数字>高位数字，因为只有增大高位数字才能达到使整体变大的效果
    所以就需要从低位开始寻找，看它是不是比它的左边大，左边就是高位，如果高位比它大那交换就没有意义了
    而且要找到最低的那个可以交换的高位，也就是最靠右边的可以交换的高位

算法:
    (1)从最右边开始寻找开始降序的数字 a[i-1],此时沿着 a[-1]~a[i] 的方向都是升序的
    (2)找到 a[i]~a[-1] 中刚好比 a[i-1] 大的数字 a[j],交换 a[i-1]/a[j] 的位置(沿着 a[-1]~a[i] 的方向还是升序的)
    (3)将 a[i]~a[-1] 翻转,也就是将升序变为倒序
'''


class Solution(object):
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        
        i,j = len(nums)-1,0
        while(i-1>=0 and nums[i]<=nums[i-1]):
            i -= 1
        
        print(i)
        j = i
        while(j<len(nums) and nums[j]>nums[i-1]):   # 这个地方一定是大于，不能等于，等于的话交换就没用了
            j += 1
        
        # 要判断一下,防止最终没找到合适的 i
        if not i==0:
            t = nums[i-1]
            nums[i-1] = nums[j-1]
            nums[j-1] = t
        
        # 交换不能开辟新的内存，必须在原始list上交换，而且不需要返回值，题目是这么规定
        j = len(nums)-1
        while(i<j):
            t = nums[i]
            nums[i] = nums[j]
            nums[j] = t
            i += 1
            j -= 1


Solution().nextPermutation([1,5,1])
        