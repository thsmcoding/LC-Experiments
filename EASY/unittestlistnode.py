# -*- coding: utf-8 -*-
"""
Created on Mon Nov 28 16:02:17 2022
author:HTS
"""

import unittest as ut
import ListNode as ln

class ListNodeUnittestMethods(ut.TestCase):
    
    def test_ListNode(self):
        inputList=[1,2,3,4,5]
        linkedList=ln.ListNode(8, ln.ListNode(10))
        print(linkedList)       
        
    def test_createList(self):
        list1, list2=[1,2,4,5,12], [1,2,3,4,5,10,14]
        result1=ln.ListNode.createList(list1)
        result2=ln.ListNode.createList(list2)
        print(result1)       
        print(result2)  


if __name__=="__main__":
    ut.main()