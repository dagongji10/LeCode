"""
Created on Sun Jan 12 18:52:29 2020
@author: 短腿伊斯科22
"""

# -*- coding: utf-8 -*-

'''
题目:
    字母异位词分组
    
思路:
    将字符串分解成元组，利用字典的键各异的特点，将分组结果存储在字典的值里面
'''

class Solution:
    def groupAnagrams(self, strs):
        res = {}
        for s in strs:
            s_set = tuple(sorted(list(s)))          # 这里需要将字符串变成列表，而不是集合（因为集合会自动去掉字符串中相同的字母）
            if s_set in res:
                res[s_set].append(s)
            else:
                res[s_set] = [s]
        
        return list(res.values())

a = Solution()
b = ["eat", "tea", "tan", "ate", "nat", "bat"]
a.groupAnagrams(b)
        