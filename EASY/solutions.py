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
        return f"{sum_10:b}"
        #str(bin(sum_10)).lstrip('-0b') ----> missed case where result has a leading zero
    
    #addToArrayForm: adding numbers in array-form
    def addToArrayForm(self, num, k):
        tostr=int(''.join([str(c) for c in num]))+k
        return list(map(lambda x: int(x), str(tostr)))
    
    #plusOne:Increment an integer in its array from
    def plusOne(self, digits):
        result= int(''.join([str(c) for c in digits]))+1
        return list(map(lambda x: int(x), [u for u in str(result)]))
        
        
        