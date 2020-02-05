"""
Created on Wed Feb  5 21:19:54 2020
@author: 短腿伊斯科22
"""

# -*- coding: utf-8 -*-

'''
题目:
    给定一组非负整数，每个元素的值代表该位置能跳到的最大距离，判断是否能从初始起点跳到最后
    
注意:
    (1)并不是一定要跳到最大距离的位置，可以在最大距离位置之前选择再调整最大距离
    (2)

思路:
    遍历数组，每遍历一个元素就更新此时可以达到的最大位置；
    如果元素所在位置超出了之前元素能达到的最大距离，那肯定不能跳到数组最后，直接结束

'''

class Solution:
    def canJump(self, nums):
        k = 0                       # 保存最大能达到的位置
        for i in range(len(nums)):  # 遍历
            if i>k:                 # 最大距离在 i 之前，也就是 i 都到不了
                return False
            
            k = max(k, i+nums[i])   # 更新最大距离：之前的最大距离和当前位置能到的距离作比较，取较大者
        
        return True

a = Solution()
b = [3,2,1,0,4]
print(a.canJump(b))