"""
Created on Sun Jan 12 10:43:51 2020
@author: 短腿伊斯科22
"""

# -*- coding: utf-8 -*-


'''
题目:
    任意数组的全排列（元素可能重复，但排列不能重复）

思路:
    利用深度优先遍历来解决问题，要注意重复元素带来的排列重复问题
    
重点:
    (1)深度优先遍历的回溯实现（还没理解透彻，记住公式，5步）
    (2)重复元素的处理方式:排序，剪枝（剪枝条件）
'''


class Solution:
    def permute(self, nums):
        nums.sort()
        
        if nums==[]:
            return []
        
        size = len(nums)
        depth = 0                                                   # 根节点深度为0
        used = [False for _ in range(size)]                         # 节点状态列表
        res = []                                                    # 初始化
        path = []                                                   # 初始化
        self.dfs(nums, size, depth, path, used, res)
        
        return res
    
    # 重点：深度优先遍历的回溯方法实现
    def dfs(self, nums, size, depth, path, used, res):
        if size==depth:
            res.append(path.copy())
            return
        
        for i in range(size):
            if i>0 and nums[i-1]==nums[i] and not used[i-1]:        # 防止重复出现（剪枝）
                continue
                
            if not used[i]:
                path.append(nums[i])                                # 更新路径
                used[i] = True                                      # 更新节点状态
                self.dfs(nums, size, depth+1, path, used, res)      # 递归
                path.pop()                                          # 回溯1：路径回溯
                used[i] = False                                     # 回溯2：节点状态回溯
    
a = [1,2,1,3]
b = Solution()
c = b.permute(a)
print(c)