# -*- coding: utf-8 -*-
"""
Created on Wed Aug 14 15:42:33 2019

@author: Administrator
"""

'''
Z字型输出关键在于找到每个字符归属于哪一行，也就是它的索引与 0~numRows 的对应关系
可以看到，2*numRows-2 其实就是一个周期（先下后上），一个周期内行号先递增再递减，转折点在 numRows-1 行

算法：
对于第 i 个字符，先对 2*numRows-2 取余，余数小于 numRows 说明位于往下走的状态；不小于 numRows 说明位于往上走的状态
往下走的时候，余数是多少就将该字符存入对应的余数行；往上走的时候，要存入 （2*numRows-2）-余数 行

时间复杂度：O(n)
'''

def convert(s: str, numRows: int) -> str:
    if numRows==1:                  # 如果是1行那直接输出就好
        return s
    
    out = {}                        # 创建dict存储每一行的内容
    for i in range(numRows):
        out[i]=''
    
    period = 2*numRows-2            # 计算周期
    for i in range(len(s)):         # 遍历字符串的字符
        series_num = i%period       # 计算余数
        if series_num<numRows:      # 余数小于行数，说明往下走
            out[series_num] += s[i]
        else:                       # 余数不小于行数，说明往上走
            out[period-series_num] += s[i]
    
    result = ''                     # 将每一行的内容合并起立
    for i in range(numRows):
        result += out[i]
    return result

print(convert("LEETCODEISHIRING", 3))