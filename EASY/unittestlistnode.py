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
        

if __name__=="__main__":
    ut.main()