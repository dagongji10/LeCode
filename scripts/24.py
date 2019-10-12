# -*- coding: utf-8 -*-
"""
Created on Sat Oct 12 19:52:21 2019

@author: Administrator
"""

'''
交换相邻的两个节点:
    (1)将相邻的两个节点看成一组:1-2,3-4,5-6,...,分别来进行交换
    (2)要注意的是,交换3-4不仅仅是要让3指向5、4指向3,还要让1指向3,这里1是已经交换过的
    (3)所以每一组要考虑的是3个节点，而不是两个,对于1-2就需要在前面人为加一个节点
'''


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

def swapPairs(head):
    if head.next==None:
        return head
    else:
        hh = ListNode(-1)       # 人为加一个首节点
        hh.next = head
        c = hh
        while(c!=None):         # 交换每一组
            t1 = c.next
            t2 = t1.next
            t1.next = t2.next
            t2.next = t1
            c.next = t2
            
            if t1.next==None or t1.next.next==None:     # 如果后面只有一个元素或者没有元素，就不要交换了
                break
            c = t1
        return hh.next
