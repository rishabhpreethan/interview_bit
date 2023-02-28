#MEDIUM

'''     https://www.interviewbit.com/problems/move-zeroes/      '''

# Problem Description

# Given an integer array A, move all 0's to the end of it while maintaining the relative order of the non-zero elements.
# Note that you must do this in-place without making a copy of the array.

# Example Input

# Input 1:
# A = [0, 1, 0, 3, 12]

# Input 2:
# A = [0]


# Example Output
# Ouput 1:
# [1, 3, 12, 0, 0]

# Ouput 2:
# [0]


def solve(A):
    c=0
    l=[]
    for i in A:
        if i==0:
            c+=1
        else:
            l.append(i)
            
    for i in range(c):
        l.append(0)
    return l

print(solve([0,1,0,3,12]))