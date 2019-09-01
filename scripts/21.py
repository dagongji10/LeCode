"""
Created on Sat Aug 31 15:26:59 2019
@author: 短腿伊斯科22
"""

# -*- coding: utf-8 -*-


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

def mergeTwoLists(l1: ListNode, l2: ListNode) -> ListNode:
    head = ListNode(1)
    h = head
    pre1 = l1
    pre2 = l2
    
    while(True):
        if pre1==None:
            h.next = pre2
            break
        elif pre2==None:
            h.next = pre1
            break
        else:
            if pre1.val<pre2.val:
                h.next = pre1
                
                h = pre1
                
            else:
                h.next = pre2
                h = pre2
                pre2 = pre2.next
    
    return head.next

def listPrint(l:ListNode):
    h = l
    while(h!=None):
        print(h.val)
        h = h.next

a = ListNode(1)
b = ListNode(3)
c = ListNode(5)
d = ListNode(7)
a.next = b
b.next = c
c.next = d

m = ListNode(2)
n = ListNode(5)
t = ListNode(10)
m.next = n
n.next = t

hh = mergeTwoLists(a, m)
listPrint(hh)