# -*- coding: utf-8 -*-
"""
Created on Wed Jan  8 20:24:05 2020

@author: Administrator
"""

'''
思路:
    双指针法
    
分析:
    (1)对于每一个柱子，我们都单独计算它的积水量，例如: i 的积水量取决于左边最高柱子、右边最高柱子中较低的那一个，如果 i 高于二者中的较低柱子那么积水量为0，否则积水量就是较低柱子减去 i 的高度
    (2)利用双指针法记录两边最高的柱子，从两边往中间走，具体计算方式见代码
    
复杂度:
    时间复杂度O(n),空间复杂度O(1)
'''

class Solution:
    def trap(self, height):
        s = 0
        left, right = 0, len(height)-1
        left_max, right_max = 0, 0
        
        while(left<right):
            if height[left]<=height[right]:         # 我们永远只关注较低的那一边，因为较低的那边才能积水
                if height[left]>=left_max:          # 柱子高于最高点，那么积水为0，只需更新最高值
                    left_max = height[left]
                else:                               # 柱子低于最高点，就会有积水
                    # left_max 是 left 处左边最高柱子，并且 left_max 肯定小于右边最高柱子
                    # 因为 left_max 是在 height[left]<=height[right] 的前提下更新的
                    # 所以 left 的积水量就取决于 left_max
                    s += left_max-height[left]
                left += 1
                
            else:
                if height[right]>=right_max:
                    right_max = height[right]
                else:
                    s += right_max-height[right]
                right -= 1
        
        return s
                
                
a = [1,0,5,1,2,0,4]
b = Solution().trap(a)
print(b)