# -*- coding: utf-8 -*-
"""
Created on Mon Nov 28 16:02:17 2022
author:HTS
"""
class Solutions:    
    
    #twoSum: searching a target sum in an integer array
    def twoSum(self, nums, target):
        candidates={}
        for i in range(len(nums)):
            search=target-nums[i]
            if search in candidates.keys():
                return [candidates[search], i]
            candidates[nums[i]]=i   
    
    #shorter_isPalindrome: checking if a string is a palindrome    
    def shorter_isPalindrome(self,nbr):
        nbr_tostr=str(nbr)
        return nbr_tostr[::] == nbr_tostr[::-1]
    
    #addBinary: return the binary sum of two strings as a binary string
    def addBinary(self, a, b):
        sum_10=int(a,2)+int(b,2)
        return str(bin(sum_10)).lstrip('-0b')