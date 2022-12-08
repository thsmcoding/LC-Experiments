# -*- coding: utf-8 -*-
"""
Created on Mon Nov 28 16:02:17 2022
author:HTS
"""

import unittest as ut
import solutions

class SolutionUnittestsMethods(ut.TestCase):
    
    def test_twoSum(self):
        test_obt=solutions.Solutions()
        result1=test_obt.twoSum([3,3], 6)
        self.assertEqual([0,1], result1, "FAIL! [0,1] was expected")
    
    def test_isPalindrome(self):
        test_obj=solutions.Solutions()
        result1=test_obj.isPalindrome(121)
        self.assertEqual(result1, True, "FAIL! TRUE expected")
        #result2=test_obj.isPalindrome(int(10))                 
        #self.assertEqual(result2, False, "FAIL! FALSE expected")
                       
if __name__=="__main__":
    ut.main()