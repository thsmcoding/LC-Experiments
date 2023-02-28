# -*- coding: utf-8 -*-
"""
Created on Mon Nov 28 16:02:17 2022
author:HTS
"""


class Solutions:    
    
    #Finding the sum in an array of numbers
    def twoSum(self, nums, target):
        candidates={}
        for i in range(len(nums)):
            search=target-nums[i]
            if search in candidates.keys():
                return [candidates[search], i]
            candidates[nums[i]]=i   
    
    #isPalindrome : shorter version    
    def shorter_isPalindrome(self,nbr):
        nbr_tostr=str(nbr)
        return nbr_tostr[::] == nbr_tostr[::-1]
    
    #return the binary sum of two strings as a binary string
    def addBinary(self, a, b):
        sum_10=int(a,2)+int(b,2)
        return str(bin(sum_10)).lstrip('-0b')