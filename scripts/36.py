# -*- coding: utf-8 -*-
"""
Created on Wed Nov 27 10:34:23 2019

@author: Administrator
"""

'''
题目:
    判断数独是否有效:行/列/单元格没有重复数字
思路:
    遍历每一个数字，对每一个数字做三次定位分别对应行、列、单元格，判断数字是否在其中出现过
注意:
    每一个行、列、单元格都是一个集合；
    行、列、单元格要根据数字的位置有所变动，但是总数是9；
    
    
知识点:
    list判断一个元素是否在列表中，需要循环遍历，时间复杂度 O(N)
    set()也就是集合，它判断元素在集合内是根据哈希表来的，时间复杂度 O(1)
    {}也就是字典，它跟集合是一样的，都是哈希表
'''

class Solution:
    def isValidSudoku(self, board):
        rows = [set() for i in range(9)]    # 创建空集合必须使用 set()
        cols = [set() for i in range(9)]
        cell = [set() for i in range(9)]
        
        for i in range(9):
            for j in range(9):
                cell_n = (i//3)*3+j//3
                elem = board[i, j]
                
                if elem=='.':
                    continue
                else:
                    if elem in rows[i] or elem in cols[j] or elem in cell[cell_n]:
                        return False
                    else:
                        rows[i].add(elem)
                        cols[j].add(elem)
                        cell[cell_n].add(elem)
                        
        return True