##
##20fa-cs115bc
##
## Antonio R. Nicolosi 
## 20201120
##************************************************************
## *  Name  : Rashmika Batra 
## * Pledge : I pledge my honor that I have abided by the Stevens Honor System.  
##************************************************************

##Programming problems with one-dimensional arrays.
def isWithinRange(arr, min, sup):
    """
     Return True if and only if all entries in the array fall between
     the specified values, with min being permitted but sup being just
     beyond the allowable range).
     
     Sample input/outputs:
     Let arr = [3, -5,  7, -1, -8, 0, -6, -2]
     Then:
	 * isWithinRange(arr, -6, 10) -> False;
	 * isWithinRange(arr, -8, 10) -> True;
	 * isWithinRange(arr, -8, 7)  -> False;
	 */
    """
   
    for a in arr:
        if not(min<=a<sup):
            return False
    return True 
arr= [3, -5,  7, -1, -8, 0, -6, -2]
print("WITHIN RANGE") 
print(isWithinRange(arr, -6, 10))
print(isWithinRange(arr, -8, 10))
print(isWithinRange(arr, -8, 7))



def isPermutation(arr):
    """Returns True if and only if its entries, taken as a set, consist
    of all the numbers between 0 and len(arr)-1 (possibly permuted
    according to some arbitrary order).

    Sample input/outputs:
    * isPermutation([3, -5, 7, 4, -1, -8, 0, -6, -2]) --> False
    * isPermutation([3, 5, 7, 4, 1, 8, 0, 6, 2])      --> True
    * isPermutation([3, 1, 0, 3, 0])                  --> False
    * isPermutation([])                               --> True
    """
    x=0
    c=0
    
    if isWithinRange(arr,0,len(arr))==False:
        return False
    
    else:
        for j in range(0,len(arr)):
            if j not in arr:
                return False
        
        return True 
print("PERMUTATION")
print(isPermutation([3, -5, 7, 4, -1, -8, 0, -6, -2]))
print(isPermutation([3, 5, 7, 4, 1, 8, 0, 6, 2]))
print(isPermutation([3, 1, 0, 3, 0]))
print(isPermutation([]))

def isCyclic(arr):
    """
    Return true if-and-only-if the sequence arr[0], * arr[arr[0]],
    arr[arr[arr[0]]], ... reaches 0 * after traversing all entries in
    arr.

    Sample input/outputs:
    * isCyclic([3, 5, 7, 4, 1, 8, 0, 6, 2]) --> True
    * isCyclic([3, 5, 7, 4, 1, 8, 6, 0, 2]) --> False
    * isCyclic([3, 1, 0, 3, 0])             --> False
    * isCyclic([])                          --> True
    """

    curr=0
    count=0
    L=[]


    for i in range(len(arr)):
        curr=arr[curr]
        L=L+[curr]
    if  curr==0 and isPermutation(L):
            return True 
    return False

print("CYCLIC") 
print(isCyclic([3, 5, 7, 4, 1, 8, 0, 6, 2]))
print(isCyclic([3, 5, 7, 4, 1, 8, 6, 0, 2]))
print(isCyclic([3, 1, 0, 3, 0]))
print(isCyclic([]))  

def isSloppilySorted(arr, k):
    """
    Return True if-and-only-if the entries in arr are sorted sloppily 
    "up to k", that is, every entry precedes at most k smaller values
     and follows at most k larger values.

    Sample input/outputs:
    * isSloppilySorted([3, 2, 1, 0, 4, 8, 7, 6, 5], 3) --> True
    * isSloppilySorted([3, 2, 1, 0, 4, 8, 7, 6, 5], 2) --> False
    * isSloppilySorted([0, 1, 2, 3, 4, 5, 6, 7, 8], 1) --> True
    * isSloppilySorted([], 3)                          --> True
    """
    for i in range(len(arr)):
        small_count=0
        large_count=0
        for j in range(i):
            if arr[j]>arr[i]:
                large_count+=1
        for l in range(i+1,len(arr)):
            if arr[l]<arr[i]:
                small_count+=1
        if large_count>k or small_count>k:
            return False
    return True 
            
print("SLOPPY") 
print(isSloppilySorted([3, 2, 1, 0, 4, 8, 7, 6, 5], 3))
print(isSloppilySorted([3, 2, 1, 0, 4, 8, 7, 6, 5], 2))
print(isSloppilySorted([0, 1, 2, 3, 4, 5, 6, 7, 8], 1))
print(isSloppilySorted([], 3))
