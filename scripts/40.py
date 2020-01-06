# -*- coding: utf-8 -*-
"""
Created on Mon Jan  6 18:27:29 2020

@author: Administrator
"""

'''
题目:
    给定一个数组candidates和一个目标数target，找出所有和为target的组合，数组中的元素只能使用一次
    
思路:
    此题和39题极为相似，只是有两个条件不同:(1)数组中的元素可以重复;(2)数组中的元素只能使用一次(组合中不能有重复的元素，但可以有相同的数字)
    首先组合中同一元素不能使用两次，那么递归的时候送入的候选数组就不能再包含当前元素了，必须从这之后的那一个开始；
    其次数组中如果有重复的元素，可能导致找到的组合重复了，要排除重复的组合就需要在循环中找到下一个和当前元素不等的元素，从它接着开始找

注意:
    要明确几个重复和不重复:(1)数组中元素可以重复
                       (2)组合中数字可以重复，但是重复的数字必须来自于数组中不同的元素，比如 candidates=[2,5,2,1,2], 那么 result 可以是[1, 2, 2]
                       (3)组合不能重复，也就是你的结果中永远只能包含不同的列表
'''


class Solution:
    def combinationSum(self, candidates, target):
        res = []
        p = []
        self.dfs(candidates, target, p, res)
        
        return res
    
    def dfs(self, c, t, p, res):
        c.sort()
    
        if t==0:
            res.append(p.copy())
        
        for i in range(len(c)):
            if i!=0 and c[i]==c[i-1]:           # 如果当前元素和上一个元素的值一样，就可以跳过这里，避免结果重复
                continue
            
            dis = t-c[i]
            if dis<0:
                break
        
            p.append(c[i])
            self.dfs(c[i+1:], dis, p, res)      # 递归传递的数组要从下一个元素开始(因为同一个元素只能用一次)，避免组合中使用同一元素
            p.pop()
            
c = [2,5,2,1,2]
t = 5

a = Solution()
b = a.combinationSum(c, t)
print(b)