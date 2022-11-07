import copy as cp

def permute(l, start, end, res):
    if start==end:
        if not l in res:
            l_copy=cp.deepcopy(l)
            res.append(l_copy)
            #print(res)
    else:
        for i in range(start, end+1):
            l[start],l[i]=l[i], l[start]
            permute(l, start+1, end, res)
            l[start],l[i]=l[i], l[start]
                  
def permuteUnique(l):
    start, end= 0, len(l)-1
    result=[]
    permute(l,start, end, result)
    return result

def trackChars(i,s,dict_chars,subs_length):
    #try:
        print("STEP VALUE :",i)
        c=s[i]
        if c in dict_chars.keys():
            subs_length[i]=1            
        else:
           subs_length[i]=1 if i==0 else subs_length[i-1]+1 
        dict_chars[c]=subs_length[i]
    #except:
     #   print("Issue found.")

     
def lengthOfLongestSubstring(s):
    alphabet,subs_length, length, last_char=[-1]*257,[0]*len(s), 0, -1
    for i in range(len(s)):
        try:
            c = s[i]
            #never seen this character so far
            if alphabet[ord(s[i])] ==-1 :
                subs_length[i]=1 if i==0 else subs_length[i-1]+1
                length= max(length,subs_length[i])
                alphabet[ord(s[i])] =i
        
            else:
                length=max(subs_length[i-1], i-alphabet[ord(s[i])])
                subs_length[i]=length
                last_char=i if subs_length[i]>subs_length[i-1] else i-1
                alphabet[ord(s[i])] =i
        except:
            print("Index seems wrong ")
    print("The length of the longest substring w/o rep. characters is ", length)

    #Building a solution of the longest substring w/o repeat. chars
    print("One of the solutions is :", s[(last_char-length):last_char])
    return length

def longestSubstring(s):
    result, start, end, ascii_codes= "", "","", [-1]*257
    last_repeated, temp=0,""
    for i in range(len(s)):
        c=s[i]
        code_char=ord(c)
        if ascii_codes[code_char]==-1:
            end=s[last_repeated:i]
            start=c
        else:
            end=s[ascii_codes[code_char]+1:i+1]
            start=s[ascii_codes[code_char]:i]
            last_repeated=i
        print("index:",i,"end:", end, "start:", start)

        ascii_codes[code_char]=i
        temp=start if len(end)<=len(start) else end
        print("value of temp:", temp)
        result=result if len(temp)<=len(result) else temp
    print("Solution found: ", result)
    return result


def main():
   # print("TESTING PROGRAM 1 \n")
   # l=[1,1,2]
   # print(permuteUnique(l))


   # print("###### TESTING MY PROGRAM 2 \n")
   # l1=[1,2,3]
   # print(permuteUnique(l1))

    print("###### TESTING LONGEST LENGTH OF SUBSTRING W/O REP. CHARACTERS \n")
    s= "abcabcbb"
    print("STRING :",s)
    res=longestSubstring(s)

    print("###### TESTING LONGEST LENGTH OF SUBSTRING W/O REP. CHARACTERS \n")
    s= "pwwkew"
    print("STRING :",s)
    res=longestSubstring(s)
    
    print("###### TESTING LONGEST LENGTH OF SUBSTRING W/O REP. CHARACTERS \n")
    s= "bbbbb"
    print("STRING :",s)
    res=longestSubstring(s)

if __name__ == "__main__":
    main()
