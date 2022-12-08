# -*- coding: utf-8 -*-
"""
Created on Mon Nov 28 16:02:17 2022
"""
class Solution:    
    def twoSum(self, nums, target):
        candidates={}
        for i in range(len(nums)):
            search=target-nums[i]
            if search in candidates.keys():
                return [candidates[search], i]
            candidates[nums[i]]=i   

    def longestCommonPrefix(self, str):
        return str       
        
        
def main():
    nums=[3,3]
    target=6
    res=Solution.twoSum(Solution, nums, target)
    print(res)   

if __name__=='__main__':
    main()