# -*- coding: utf-8 -*-
"""
Created on Mon Nov 28 16:02:17 2022
author:HTS
"""

import unittest as ut
import solutions as sol

class SolutionUnittestsMethods(ut.TestCase):
    test_obt=sol.Solutions()
    
    def test_twoSum(self):
        result1=self.test_obt.twoSum([3,3], 6)
        self.assertEqual([0,1], result1, "FAIL! [0,1] was expected")
        result2=self.test_obt.twoSum([], 0)
        self.assertEqual(None, result2, "FAIL! None was expected")
        result3=self.test_obt.twoSum([1], 2)
        self.assertEqual(None, result3, "FAIL! None was expected")
        result4=self.test_obt.twoSum([2,7,11,15],9)
        self.assertEqual([0,1], result4, "FAIL! [0,1] was expected")
        result5=self.test_obt.twoSum([3,2,4],6)
        self.assertEqual([1,2], result5, "FAIL! [1,2] was expected")        

    def test_shorter_IsPalindrome(self):
        result1=self.test_obt.shorter_isPalindrome(121)
        self.assertEqual(result1, True,"FAIL! True expected" )
        result2=self.test_obt.shorter_isPalindrome(10)
        self.assertEqual(result2, False,"FAIL! False expected" )
        
    def test_addBinary(self):
        result1=self.test_obt.addBinary("11", "1")
        self.assertEqual(result1, "100", "FAIL! 11 and 1 should return 100")
        result2=self.test_obt.addBinary("1010", "1011")
        self.assertEqual(result2, "10101", "FAIL! 1010 and 1011 should return 10101")
        
    def test_addToArrayForm(self):
        result1=self.test_obt.addToArrayForm([1,2,0,0], k = 34)
        self.assertEqual(result1, [1,2,3,4], "FAIL! Should return [1,2,3,4] ")
        result2=self.test_obt.addToArrayForm([2,7,4], k = 181)
        self.assertEqual(result2, [4,5,5], "FAIL! Should return [4,5,5] ")
        result3=self.test_obt.addToArrayForm([2,1,5], k = 806)
        self.assertEqual(result3, [1,0,2,1], "FAIL! Should return [1,0,2,1] ")

                         
if __name__=="__main__":
    ut.main()