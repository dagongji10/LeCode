"""
Created on Thu Oct 17 21:58:15 2019
@author: 短腿伊斯科22
"""

# -*- coding: utf-8 -*-

'''
KMP算法：
(1)S[i]==P[j]: i++, j++
(2)S[i]!=P[j]: 寻找最大的 k,使得 P[0~(k-1)]==P[(j-k)~(j-1)],j=k
关键在于理解(2),并实现如何寻找满足要求的 k

首先理解(2):当S[i]!=P[j]时,我们要去看一下 P[0~(j-1)] 里面有没有与 P[0~(k-1)] 相等的字串,如果有那就不用再将 i 回溯了,直接将P拉过去就行
其次如何寻找满足要求的k：k 的要求是,使得j前面的字串P[0~(j-1)]最前面的k个字符和最后面的k个字符相等;这就是 next 数组的计算
                    假设next[j]=k,要计算next[j+1],需要分两种情况讨论:a. P[k]==P[j],此时next[j+1]=k+1
                                                                b. P[k]!=P[j],此时就要去找P[0~(k-1)]最大的重复串的长度,也就是next[k],判断P[next[k]]是否等于P[j]
                                                                   如果P[next[k]]==P[j],也就是说P[0~(k-1)]的首尾存在一个最长重复字串,那么P[(j-k)~(j-1)]的首尾也存在,也就是说P[0~(k-1)]的首与P[(j-k)~(j-1)]的尾相等,此时next[j+1]=next[k]+1
                                                                   如果P[next[k]]!=P[j],那就继续寻找下一个,P[next[next[k]]]
'''

class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        next_ = self.get_next(needle)
        
        i,j = 0,0
        while(i<len(haystack) and j<len(needle)):
            if haystack[i]==needle[j]:
                i += 1
                j += 1
            else:
                k = next_[j]
                if k==-1:       # 如果j==0，也就是首字符就不匹配
                    i += 1
                elif k==0:      # 如果不是首字符，但是也不存在重复
                    j = 0
                else:           # 如果不是首字符，但是存在重复
                    j = k
                    
        if j==len(needle):
            return i-j
        else:
            return -1
            
                
    def get_next(self, p):
        if p=='':
            return []
        
        k,j = -1,0
        next_ = [k]                     # 初始化
        while(j<len(p)-1):              # 根据当前位置j，计算下一位置j+1
            if k==-1 or p[k]==p[j]:     # k==-1表示回溯到首字符都没找到，说明next[j+1]=0
                k += 1
                j += 1
                next_.append(k)
            else:
                k = next_[k]
        return next_
    
s = "issippi"
p = "issip"

print(Solution().get_next(p))
print(Solution().strStr(s, p))