# -*- coding: utf-8 -*-
"""
Created on Mon Nov 28 16:02:17 2022
"""
class Solution:
    result=[0]*2
    candidates={} 
    
    def twoSum(self, nums, target):
        for i in range(len(nums)):
            search=target-nums[i]
            if search in self.candidates.keys():
                self.result[0], self.result[1]=i,self.candidates[search]
                break
            self.candidates[nums[i]]=i
        return self.result    
        
def main():
    nums=[3,3]
    target=6
    res=Solution.twoSum(Solution(),nums, target)
    print(res)   

if '__name__'=='__main__':
    Solution.main()