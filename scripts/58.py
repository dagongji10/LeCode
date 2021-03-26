# -*- coding: utf-8 -*-

'''
@ Time  : 2021/3/26/0026 15:56
@ Author: dagongji09
@ File  : 58.py
'''
'''
题目：
给你一个字符串 s，由若干单词组成，单词之间用空格隔开。返回字符串中最后一个单词的长度。如果不存在最后一个单词，请返回 0 。
'''


class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        return len(s.strip().split(' ')[-1])
