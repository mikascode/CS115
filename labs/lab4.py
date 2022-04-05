#Name:Rashmika Batra
#Honor Statement: I pledge my honor that I have abided by the Stevens Honor System.
#Lab 4:  Due Friday, October 2, 2020 
def dotProduct(L,K):
    '''recursivley computes the dot product of two given lists (L and K) of equal length'''
    if not L or not K: 
        return 0.0
    else:
        return L[0]* K[0] + dotProduct(L[1:],K[1:])

def expand (s):
    ''' takes a string,s, and returns a list of the characters (each of which is a string of lenghth 1) in that string.''' 
    if not s:
        return []
    else:
        return [s[0]]+expand(s[1:])

def deepMember (e,L):
    '''takes in an element e and a sequence L where by "sequence" we mean a list.
        deepMember analyzes the list, and returns True is e in in L, or in any sublist of L, or sublist of a sublist, etc.
        '''
    if L==[]:
        return False  
    else:
        x=L[0]
        if isinstance(x, list):
            return deepMember(e, x) or deepMember(e, L[1:])

        else:
            if e==x:
                return True
            else:
                return deepMember(e,L[1:]) 
   
def removeAll(e,L):
    '''takes in an element e and a list L. Then, removeAll should return another list that is identical to L excpet that all elements identical to e have been removed.
        e has to be a top-level element to be removed.
    '''
    if L==[]:
        return []
    else:
        x=L[0]
        if isinstance(x, list):
            return [x]+removeAll(e,L[1:]) 
        else:
            if e==x:  
                return removeAll(e,L[1:])
            else:
                return [x]+removeAll(e,L[1:])

def myFilter(h, L):
    '''takes in a function and a list and returns all values of the list that meet that function's requierments'''
    if L==[]:
        return[]
    else:
        if (h(L[0])):
            return [L[0]]+myFilter(h,L[1:])
        else:
            return myFilter(h,L[1:])

def deepReverse(L):
    '''takes as input a list of elements where some of those elements may be lists themselves. deepReverse returns the reversal of the list where,
        additionally, any element that is a list is also deepReversed
        '''
    if L==[]:
        return []
    else:
        x=L[0]
        if isinstance(x, list):
            return  deepReverse(L[1:])+[deepReverse(x)]
        else:
            return deepReverse(L[1:])+ [x] 


        

   




