# -*- coding: utf-8 -*-
"""
Created on Mon Nov 28 16:02:17 2022
author:HTS
"""
class Solutions:    
    
    #Finding the sum
    def twoSum(self, nums, target):
        candidates={}
        for i in range(len(nums)):
            search=target-nums[i]
            if search in candidates.keys():
                return [candidates[search], i]
            candidates[nums[i]]=i   

    #Checking if a number is a palindrome 
    def isPalindrome(self,nbr):
        def check_list_for_palindrome(nbr, l):
            if nbr<0:
                return False
            total=len(l)
            for i in range(total//2):
                if l[i]!=l[total-1-i]:
                    return False
            return True               
        figures=[]
        while(nbr>0):
            figures.append(nbr%10)
            nbr=nbr//10                         
        return check_list_for_palindrome(nbr, figures)   
    
    #isPalindrome : shorter version    
    def shorter_isPalindrome(self,nbr):
        nbr_tostr=str(nbr)
        for i in range(len(nbr_tostr)//2):
            if not nbr_tostr[i] is nbr_tostr[len(nbr_tostr)-1-i]:
                return False
        return True
    
    def romanToInteger(self, s):
        symbols= {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000,
                  'IV':4, 'IX':9, 'XL':40, 'XC':90, 'CD':400, 'CM':900 }
        numb,i=0,0
        while (i<len(s)):
            if s[i::i+2] in symbols and len(s[i::i+2]) == 2:
                print(i)
                numb+=symbols[s[i::i+2]]
                i+=2
            else:
                numb+=symbols[s[i]]
                i+=1
        return numb 
     
        
     
        
     
        