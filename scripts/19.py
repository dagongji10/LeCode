"""
Created on Wed Aug 28 22:16:01 2019
@author: 短腿伊斯科22
"""

# -*- coding: utf-8 -*-


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
    