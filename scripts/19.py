"""
Created on Wed Aug 28 22:16:01 2019
@author: 短腿伊斯科22
"""

# -*- coding: utf-8 -*-

'''
两个知识点
（1）python链表的实现
链表数据结构原理同C++，实现的时候不再使用指针，直接定义节点类，next是其中一个属性
构造实例时，先实例化节点对象，然后逐个将其连接起来，只需知道头结点就可遍历整个链表
（2）倒数第n个数的实现
从尾到头遍历可以使用双指针，还是用左右指针来代表：l，r
双指针都是从左边开始往右走，只是r先行一步，当它从1走到n时，l开始和r一样同步右行；直到r走到末尾时，l也就刚好位于倒数第n个数的位置
分析：
假设数组长度是S，倒数第n个数就是顺数第S-n个数
r指针将整段路程分成两部分：前一部分长度为n，后一段就是S-n，r走了S-n那么l就刚好找到倒数第n个数
'''

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

def removeNthFromEnd(head: ListNode, n: int) -> ListNode:
    _count = 1
    l = head
    r = head
    while(_count != n):
        r = r.next
        _count += 1
    
    if r.next==None:
        head = head.next
    else:
        r = r.next
        while(r.next != None):
            l = l.next
            r = r.next

        l.next = l.next.next
    
    h = head
    print(h.val)
    while(h.next is not None):
        print(h.next.val)
        h = h.next
    
a = ListNode(1)
b = ListNode(2)
c = ListNode(3)
d = ListNode(4)
e = ListNode(5)
a.next = b
b.next = c
c.next = d
d.next = e

removeNthFromEnd(a, 1)
    