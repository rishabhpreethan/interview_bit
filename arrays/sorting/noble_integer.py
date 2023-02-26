#EASY

'''     https://www.interviewbit.com/problems/noble-integer/        '''

# Problem Description

# Given an integer array A, find if an integer p exists in the array such that the number of integers greater than p in the array equals to p.


def solve(A):
    A.sort()
    n=len(A)
    for i in range(n):
        if i<n-1 and A[i]==A[i+1]:
            continue
        if A[i]==n-1-i:
            return 1
    return -1

print(solve([3,2,1,3]))