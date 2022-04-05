# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Name    :Rashmika Batra 
# Pledge  :I pledge my honor that I have abided by the Stevens Honor System.
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# Max:
#  Write a hmmm function that gets two numbers,
#   then prints the larger of the two.
#  Assumptions: Both inputs are any integers
Max = """
00 read r1
01 read r2
02 sub r3 r1 r2 
03 jgtzn r3 6
04 write r2 
05 halt 
06 write r1 
07 halt 
"""


# Power:
#  Write a hmmm function that gets two numbers,
#   then prints (No.1 ^ No.2).
#  Assumptions: No.1 is any integer, No.2 >= 0
Power = """
00 setn r10 1
01 read r1
02 read r2
03 jgtzn r2 06
04 write r10
05 halt
06 mul r10 r10 r1
07 addn r2 -1
08 jumpn 03
09 halt
"""


# Fibonacci
#  Write a hmmm function that gets one number,
#   then prints the No.1st fibonacci number.
#  Assumptions: No.1 >= 0
#  Hint: You really don't want to implement
#   recursion in hmmm, try to find an
#   iterative method to compute your goal.
#  Tests: f(2) = 1
#         f(5) = 5
#         f(9) = 34
Fibonacci = """
00 read r1
01 addn r1 -1
02 setn r2 0
03 setn r3 1
04 setn r5 0  
05 jltzn r1 14
06 jeqzn r1 12
07 add r5 r3 r2
08 copy r2 r3
09 copy r3 r5
10 addn r1 -1
11 jumpn 6
12 write r5
13 halt
14 write r2
"""


# ~~~~~ Running ~~~~~~
import hmmm
import importlib

runThis = Max  # Change to the function you want to run
doDebug = False # Change to turn debug mode on/off

# call main() from the command line to run the program again
def main(runArg = runThis, debugArg = doDebug):
    importlib.reload(hmmm)
    hmmm.main(runArg, debugArg)

if __name__ == "__main__" : 
    main()


