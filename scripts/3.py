# -*- coding: utf-8 -*-
"""
Created on Mon Aug 26 10:06:49 2019

@author: Administrator
"""

def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        maxlen = 0
        _len = len(s)
        _str = []
        i,j = 0,0
        while i<_len and j<_len:
            if s[j] not in _str:
                _str.append(s[j])
                maxlen = max(maxlen, len(_str))
                j += 1
            else:
                _str.remove(s[i])
                i += 1
                
        if s=='':
            return 0
        return maxlen