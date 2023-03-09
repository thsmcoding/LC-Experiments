#- coding: utf-8 -*-
"""
Created on Mon Nov 28 16:02:17 2022
author:HTS
"""
    

import ListNode as ln
import itertools as it

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
             
   # def longestCommonPrefix(self, strs):
    #    current_prefix, candidate="",strs[0]    
     #   i=0
      #  while(i<len(candidate)):
       #     if all(str.startswith(candidate[:i+1]) for str in strs[1:]):
        #        current_prefix=candidate[:i+1]
         #       i+=1
          #  else:
           #     break
        #return current_prefix
     
    def longestCommonPrefix(self, strs):
        current_prefix, i  ="", 0
        if len(strs)==1:
            return strs[0]
        elif any(str == "" for str in strs):
            return ""
        candidate=strs[0]
        while(all(str.startswith(candidate[:i+1]) for str in strs[1:]) and i < len(candidate)):
            current_prefix=candidate[:i+1]
            print(current_prefix)
            i+=1
        # else:
            #     raise IndexError("Non existing index in input array of strings")
        return current_prefix
    
    def auxMerge(self, list1, list2, head, result):
        if list1 is None:
            result.next=list2
            return head.next
        elif list2 is None:
            result.next=list1
            return head.next
        else:
            if list1.val <= list2.val:
                l1bis=list1
                l1bis_n=list1.next
                l1bis.next=None
                result.next=l1bis
                return self.auxMerge(l1bis_n,list2, head, result.next)
            else:
                l2bis=list2
                l2bis_n=list2.next
                l2bis.next=None
                result.next=l2bis
                return self.auxMerge(list1, l2bis_n, head, result.next)
                
    def mergeTwoLists(self, list1, list2):
        head=ln.ListNode(-1, None)
        result=head
        return self.auxMerge(list1, list2, head, result)
    
    def mergeImproved(self, list1, list2):
        if not list1 or not list2:
            return list1 or list2
        if list1.val < list2.val:
            list1.next=self.mergeImproved(list1.next, list2)
            return list1
        else:
            list2.next=self.mergeImproved(list1, list2.next)
            return list2
    
    def auxremoveElement(self, nums, val, st, end):
        if st>end:
            #end=0 if (len(nums)==0) else end
            return end+1
        if nums[st] == val:
            if nums[end] == val:
                end=end-1
            else:
                nums[st],nums[end], st, end=nums[end], nums[st], st+1, end-1
        else:
            st=st+1
        return self.auxremoveElement(nums, val, st, end)    
    
    def removeElement(self, nums, val):
        return self.auxremoveElement(nums, val, 0, len(nums)-1)
    
    def it_removeElement(self, nums, val):
        i,k=0, len(nums)-1
        while(i<=k):
            if nums[i]==val:
                if nums[k] ==val:
                    k=k-1
                else:
                    nums[i],nums[k], i, k=nums[k],nums[i], i+1, k-1
            else:
                i=i+1
        return k+1            
            
    def removeDuplicates(self, nums):
         i,length=0, len(nums)
         while(i<length-1):
             if nums[i] == nums[i+1]:
                 del(nums[i])
                 i -=1
                 length -=1
             i +=1
         return length      
        
    def searchInsert(self, nums, target):
        low, high=0,len(nums)
        while(low<high):
            mid=(high+low)//2
            if nums[mid]==target:
                return mid
            elif nums[mid]<target:
                low=mid+1
            else:      
                high=mid-1
        return low
    
    def addBinary(self, a,b):
        max_length=len(a) if len(a)>len(b) else len(b)
        result, hold=[0]*(max_length+1), 0
        index=len(result)-1        
        la=[0]*(max_length-len(a))
        lb=[0]*(max_length-len(b))
        la[(max_length-len(a)):max_length]=[int(c) for c in a]
        lb[(max_length-len(b)):max_length]=[int(c) for c in b]
        print(la, " ::: ", a)
        print(lb, " ::: ", b)
        for u in range(len(la)-1,-1, -1):
            result[index]=(la[u] + lb[u]+hold)%2
            hold=(la[u]+lb[u]+hold)//2
            index -=1
        if hold:
            result[index]=hold   
        else:
            del(result[0])
        return ''.join([str(u) for u in result])
         
    
    def merge(self, nums1,m,nums2, n):
        print("START :", nums1)
        i,j,k=m-1,n-1,m+n-1
        while(k>-1):
            if j<0:
                return
            if i<0:
                nums1[0:k+1]=nums2
                i -=1
            else:
                if (nums1[i] > nums2[j]):
                    nums1[k]= nums1[i]
                    i -=1
                else:       
                    nums1[k]=nums2[j]
                    j -=1
            k -=1

if __name__=="__main__":
    nums1,m,nums2,n=[1,2,3,0,0,0], 3, [2,5,6],3
    Solutions().merge(nums1, m, nums2, n)
    print("END :", nums1)
    print("*************************************")       
    nums1,m,nums2,n=[0], 0, [1],1
    Solutions().merge(nums1, m, nums2, n)
    print("END :", nums1)
    print("*************************************")       
    nums1,m,nums2,n=[1], 1, [],0
    Solutions().merge(nums1, m, nums2, n)
    print("END :", nums1)
    # s1, s2= "111", "111"
    # res=Solutions().addBinary(s1, s2)   
    # print(" **************** ")     
    # print(res)
    # print(" **************** ")     
    # s1, s2= "1010", "1011"
    # res=Solutions().addBinary(s1, s2) 
    # print(res)
    # print(" **************** ")     
    # print(Solutions().faster_addBinary(s1, s2))
    
    
    
    
    
    