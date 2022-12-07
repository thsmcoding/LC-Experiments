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
        result2=test_obt.twoSum([], 0)
        self.assertEqual(None, result2, "FAIL! None was expected")
        result3=test_obt.twoSum([1], 2)
        self.assertEqual(None, result3, "FAIL! None was expected")
        result4=test_obt.twoSum([2,7,11,15],9)
        self.assertEqual([0,1], result4, "FAIL! [0,1] was expected")
        result5=test_obt.twoSum([3,2,4],6)
        self.assertEqual([1,2], result5, "FAIL! [1,2] was expected")        

if __name__=="__main__":
    ut.main()