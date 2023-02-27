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
                
    def func(self,u,v):
        if u is None or v is None:
            return v or u  
        elif u!=v:
            return '1'
        return '0'    
    
    #USING ITERTOOLS module but issue with function zip_longest
    def check(self, l1,l2):
        total=len(l1)+len(l2)
        hold='0'
        l3=['0']*total
        print(l3)
        for x, y in it.zip_longest(l1, l2):
            total -=1
            l3[total]= self.func(hold, self.func(x,y))
            hold='1' if x==y==1 else '0'
        return l3
        
    # def addBinary(self, a, b):
    #    la, lb =[int(c) for c in a], [int(c) for c in b]
    #    lengtha, lengthb=len(la), len(lb)
    #    result,hold=[], 0
    #    if lengtha <lengthb:
    #        tmp=[0]*(lengthb-lengtha)
    #        tmp.extend(la)
    #        la=tmp
    #    else:
    #        tmp=[0]*(lengtha-lengthb)
    #        tmp.extend(lb)    
    #        lb=tmp           
    #    lengtha, lengthb=len(la)-1, len(lb)-1
    #    while(lengtha>-1):
    #        result.append((hold+la[lengtha]+lb[lengthb])%2)
    #        hold=(hold+la[lengtha]+lb[lengthb])//2 
    #        lengtha -=1
    #        lengthb -=1             
    #    if hold:
    #        result.append(hold)               
    #    result=[str(c) for c in result]
    #    return ''.join(result[::-1])
          
    
    def addBinary(self, a,b):
        max_length=len(a) if len(a)>len(b) else len(b)
        result, hold=[], 0
        la, lb = [int(a[u]) if u < len(a) else 0 for u in range(max_length-1,-1,-1)], [int(b[u]) if u <len(b) else 0 for u in range(max_length-1,-1,-1)]
        print(la," : ", a)
        print(lb, " : ",b)
        for (u,v) in zip(range(len(la)-1,-1, -1), range(len(lb)-1,-1,-1)):
            result.append((la[u] + lb[u]+hold)%2)
            hold=(la[u]+lb[u]+hold)//2
        if hold==1:
            tmp=[1]
            tmp.extend(result)
            result=tmp
        return ''.join([str(u) for u in result])

           

if __name__=="__main__":
    s1, s2= "11", "1"
    res=Solutions().addBinary(s1, s2)   
    print(" **************** ")     
    print(res)
