# Adapted by Dominick DiMaggio for Prof. Nicolosi's CS 115 at Stevens Institute of Technology, 2020

##########################################
# Name: Rashmika Batra
# Pledge: I pledege my honor that I have abided by the Stevens honor system.
##########################################

# Import reduce from the functools package
from functools import reduce

#######################################################################################
# Task 1: Use reduce to determine if all elements in a boolean list are true
def helper(a,b):
    return a and b  

def all_true(lst):
    return reduce(helper, lst)
   
    # TODO: Implement

#######################################################################################
# Task 1.1: Use reduce to determine if AT LEAST one element in a boolean list is true
# Hint: Should be very similar to the above function
def helper2(a,b):
    return a or b  

def one_true(lst):
    return reduce(helper2, lst)  
   
    # TODO: Implement

#######################################################################################
# Task 2: Use map and reduce to return how many elements are True in a boolean list
#First use map to convert to numbers, then use reduce to add the numbers
def helper3 (a,b):
    return a or b

def use_map ():
    return list(map(helper3, lst))

def helper4 (a,b) :
    return a+b

def count_true(lst):
    return reduce(helper4, lst)
    # TODO: Implement

# This function is provided for you
# Gets a list of strings through the command line
# Input is accepted line-by-line
def getInput():

    lst = []
    txt = input()

    while(len(txt) != 0):
        lst.append(txt)
        txt = input()

    return lst

# Task 3: Get the longest string in the list using map and reduce, and print it out
# 'strings' is a list of input strings e.g. [ 'hello', 'world' ]
# Hint: The 'map' part of your program should take a string s into a length-2 list [len(s), s].

def getLongestString():
    strings = getInput()
    def helper5 (s):
        return[len(s), s]
    
    def helper6 (x,y): 
        if x[0] > y[0]:
            return x
        else:
            return y
    return reduce(helper6, list(map(helper5, strings)))[1]
