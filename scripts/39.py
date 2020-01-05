# -*- coding: utf-8 -*-


'''
题目:
    给定一个无重复数字的数组candidates，和一个目标值target，找到所有加和为target的组合
    
思路:
    其实就是一个深度遍历的过程

解析:
    (1)深度遍历时要时刻记住路径，这样在你满足路径遍历终止条件时，就能将当前路径作为结果保存；
    (2)其次，需要对数组进行排序，这样可以有效防止重复；
    (3)采取将target和当前数组最小的值求差，看是不是满足终止条件，也就是刚好等于0，如果等于0那么这就是我们需要的结果，保存，然后进行下一步；
    (4)如果差值是大于0的，那么就把这个求差的数组元素存入路径内，深度更进一步；
    (5)记住，深度路径递归之后，要及时释放路径，不能一直只存不取
    
注意:
    将路径作为结果保存时，一定是copy路径，因为python是引用传递，如果直接将路径存入，后面的释放操作会影响最终的结果
'''


class Solution:
    def combinationSum(self, candidates, target):
        res = []
        p = []
        self.dfs(candidates, target, p, res)
        
        return res
    
    def dfs(self, c, t, p, res):
        c.sort()
    
        # 终止条件满足了（其实后面的for在第一次遍历就会终止）
        if t==0:
            res.append(p.copy())            # 此处一定要用copy的方法，如果直接将路径存入，那么后面释放的操作也会影响这里的值
        
        # 中止条件不满足
        for i in range(len(c)):
            dis = t-c[i]                    # 更新target
            if dis<0:                       # 根据target的正负做“剪枝”操作
                break
        
            p.append(c[i])                  # 在路径中保存满足要求的数组元素
            self.dfs(c[i:], dis, p, res)    # 递归寻找路径的下一部分，注意这时的数组是要及时更新的
            p.pop()                         # 找到之后要及时释放
            
c = [5, 2, 3, 6, 7]
t = 10

a = Solution()
b = a.combinationSum(c, t)
print(b)
