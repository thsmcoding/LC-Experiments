# -*- coding: utf-8 -*-
"""
Created on Mon Nov 28 16:02:17 2022
author:HTS
"""

import unittest as ut
import solutions

class SolutionUnittestsMethods(ut.TestCase):
    test_obj=solutions.Solutions()
    
    def test_twoSum(self):
        result1=self.test_obj.twoSum([3,3], 6)
        self.assertEqual([0,1], result1, "FAIL! [0,1] was expected")
    
    def test_isPalindrome(self):
        result1=self.test_obj.isPalindrome(121)
        self.assertEqual(result1, True, "FAIL! TRUE expected")
        #result2=test_obj.isPalindrome(int(10))                 
        #self.assertEqual(result2, False, "FAIL! FALSE expected")    
    
    def test_shorterisPalindrome(self):
        result1=self.test_obj.shorter_isPalindrome(121)
        self.assertEqual(result1, True, "FAIL! TRUE expected")
        #result2=test_obj.isPalindrome(int(10))                 
        #self.assertEqual(result2, False, "FAIL! FALSE expected")
    
    def test_longestCommonPrefix(self):
        # result1=self.test_obj.longestCommonPrefix([""])
        # self.assertEqual(result1,"", "FAIL! empty string expected")
        # result2=self.test_obj.longestCommonPrefix(["dog","racecar","car"])
        # self.assertEqual(result2,"", "FAIL! empty string expected")
        # result3=self.test_obj.longestCommonPrefix(["", ""])
        # self.assertEqual(result3,"", "FAIL! empty string expected")
        # result4=self.test_obj.longestCommonPrefix(["a"])
        # self.assertEqual(result4,"a", "FAIL! empty string expected")

        result5=self.test_obj.longestCommonPrefix(["flower","flower","flower","flower"])
        self.assertEqual(result5,"flower", "FAIL! flower expected")
  
   
   
                    
if __name__=="__main__":
    ut.main()