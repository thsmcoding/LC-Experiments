# -*- coding: utf-8 -*-
"""
Created on Mon Nov 28 16:02:17 2022
author:HTS
"""
class ListNode:    
    
    def __init__(self, val=0, next=None):
        self.val=val
        self.next=next
    
    def __str__(self):
        pt_self=self
        s=""
        if pt_self is None:
            s+="X"
        while(pt_self is not None):
            s+= str(pt_self.val)
            if not (pt_self.next is None):
                s+="->"
            pt_self=pt_self.next
        return s
        
    def createList(l):
        head=ListNode(-1)
        result=head
        for i in l:
            result.next=ListNode(i, None)
            result=result.next
        return head.next
        
  