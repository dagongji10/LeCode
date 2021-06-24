# -*- coding: utf-8 -*-

'''
@ Time   : 2021/6/24 20:04
@ Author : dagongji09
@ File   : 68.py
'''

from typing import List


class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        index = 0
        line, result = [], []

        # 遍历每一个单词，判断它是不是能够被纳入当前行
        while index < len(words):
            word = words[index]

            # 如果当前行为空，那么加入当前单词后当前行长度就是单词长度
            # 如果当前行不为空，那么加入当前单词后当前行长度就需要加上单词长度，并加一个空格
            # 加入当前单词后，当前行长度不超过 maxWidth，就表示可以纳入
            if len(word) + len(' '.join(line)) + (1 if len(line) > 0 else 0) <= maxWidth:
                line.append(word)
                index += 1
            else:
                # 总共需要填补的空格数
                total_space = maxWidth - len(''.join(line))

                if len(line) == 1:
                    # 只有一个单词则左对齐
                    result.append(line[0] + ' ' * total_space)
                else:
                    # 空格均匀分布，且优先填补左边
                    a = total_space // (len(line) - 1)
                    b = total_space % (len(line) - 1)
                    spaces = [a + 1 for i in range(b)] + [a for i in range(len(line) - 1 - b)] + [0]
                    line_space = [line[i] + ' ' * spaces[i] for i in range(len(line))]
                    result.append(''.join(line_space))

                # 重置行队列
                line = []

        # 最后一行的处理
        if len(line) > 0:
            result.append(' '.join(line))
            result[-1] = result[-1] + ' ' * (maxWidth - len(result[-1]))

        return result


a = Solution()
print(a.fullJustify(["Listen", "to", "many,", "speak", "to", "a", "few."], 6))
