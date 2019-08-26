# -*- coding: utf-8 -*-
"""
Created on Mon Aug 26 10:05:03 2019

@author: Administrator
"""

def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        num1 = 0
        index = 0
        l = l1
        while l!=None:
            num1 = num1 + l.val*(10**index)
            index += 1
            l = l.next
            
        num2 = 0
        index = 0
        l = l2
        while l!=None:
            num1 = num1 + l.val*(10**index)
            index += 1
            l = l.next
            
        _sum = num1 + num2
        head = ListNode(_sum%10)
        now = head
        _sum = _sum//10
        while _sum!=0:
            node = ListNode(_sum%10)
            now.next = node
            now = node
            _sum = _sum//10
            
        return head