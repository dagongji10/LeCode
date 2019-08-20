# -*- coding: utf-8 -*-
"""
Created on Mon Aug 19 19:20:31 2019

@author: Administrator
"""

'''
1、LeetCode的正则表达式匹配逻辑跟RE不同，样例的第一个RE就能匹配上；这里我们先按照RE的逻辑来实现
2、通配符 . 要占用一个位置，也就是说它所代表的那个字符至少要出现一次，否则匹配失败（没有匹配）；
   所以它解决的是字符种类的问题，我不知道这个位置是什么那就用 . 来替代
3、通配符 * 要跟在它前面的字符连起来看，它可以不占用位置，但会尽最大努力占一个位置；如果它前面没有字符（它位于第一位），就会报错；
   所以它解决的是一个字符重复次数的问题，你可以重复0次，也可以是任意次
   
p.charAt(j) == s.charAt(i) : dp[i][j] = dp[i-1][j-1]
p.charAt(j) == '.' : dp[i][j] = dp[i-1][j-1];
p.charAt(j) == '*': here are two sub conditions:
    - if p.charAt(j-1) != s.charAt(i) : dp[i][j] = dp[i][j-2]
    - if p.charAt(j-1) == s.charAt(i) or p.charAt(i-1) == '.':
            dp[i][j] = dp[i-1][j]       // in this case, a* counts as multiple a
            dp[i][j] = dp[i][j-1]       // in this case, a* counts as single a
            dp[i][j] = dp[i][j-2]       // in this case, a* counts as empty
'''

def isMatch(s: str, p: str) -> bool:
    s_len = len(s)
    p_len = len(p)
    dp = [[False] * (p_len + 1) for _ in range(s_len + 1)]

    dp[0][0] = True
    for i in range(p_len):
        if p[i] == "*" and dp[0][i - 1]:
            dp[0][i + 1] = True

    for i in range(s_len):
        for j in range(p_len):
            if p[j] == s[i] or p[j] == ".":                 # 1. p[j]不为 * 同时还能匹配上
                dp[i + 1][j + 1] = dp[i][j]
            elif p[j] == "*":                               # 2. p[j]为 * 的情况
                if p[j - 1] != s[i]:                        # 2.1 *前面的字符不出现，状态码同p[j-2]一致
                    dp[i + 1][j + 1] = dp[i + 1][j - 1]
                if p[j-1] == s[i] or p[j-1] == ".":         # 2.2 *前面的字符出现
                    dp[i+1][j+1] = (dp[i][j+1] or dp[i+1][j] or dp[i+1][j-1])

    return dp[-1][-1]
