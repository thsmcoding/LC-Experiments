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

def main():
    print("TESTING PROGRAM 1 \n")
    l=[1,1,2]
    print(permuteUnique(l))


    print("###### TESTING MY PROGRAM 2 \n")
    l1=[1,2,3]
    print(permuteUnique(l1))
    


if __name__ == "__main__":
    main()
