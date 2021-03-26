# -*- coding: utf-8 -*-

'''
@ Time  : 2021/3/26/0026 14:30
@ Author: dagongji09
@ File  : 57.py
'''

'''
题目：
    插入区间
    给你一个 无重叠的、按照区间起始端点排序的区间列表，在列表中插入一个新的区间，你需要确保列表中的区间仍然有序且不重叠（如果有必要的话，可以合并区间）。

思考：
（1）要完成插入的操作，就要考虑区间之间的关系，无非两种：有交集，无交集
（2）判断区间之间的关系，是一个 N对1 的操作，也就是要把 intervals 中的N个区间跟 newInterval 去做比较
（3）一般情况是：intervals 左边的 p1 个区间跟 newInterval 无交集，右边的 p2 个区间跟 newInterval 也无交集，只有中间的 p 个区间跟 newInterval 有交集
（4）对于有交集的情况，我们将 newInterval 的位置固定，但是更新它的范围，直到有交集的区间搜索完

关键点：
这里遍历的是 intervals，所以不宜对它的元素再去改动；newInterval 的位置是固定的，所以可以对它的值做修改
所以，要明确动与不动的状态，这里就是让 newInterval 动起来
'''

from typing import List


class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        res = []
        p = 0

        # intervals 中的区间在 newInterval 的左边，且无交集
        while (p < len(intervals) and intervals[p][1] < newInterval[0]):
            p += 1
        res += intervals[:p]

        # intervals 中的区间与 newInterval 有交集
        while (p < len(intervals) and intervals[p][0] <= newInterval[1]):
            newInterval[0] = min(newInterval[0], intervals[p][0])
            newInterval[1] = max(newInterval[1], intervals[p][1])
            p += 1
        res.append(newInterval)

        # intervals 中的区间在 newInterval 的右边，且无交集
        res += intervals[p:]

        return res
