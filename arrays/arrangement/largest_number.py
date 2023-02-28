#MEDIUM

'''     https://www.interviewbit.com/problems/largest-number/       '''

# Problem Description

# Given a list of non-negative integers, arrange them such that they form the largest number.
# Note: The result may be very large, so you need to return a string instead of an integer.

# Example Input
# A = [3, 30, 34, 5, 9]

# Example Output
# 9534330


from functools import cmp_to_key

def largestNumber(A):
    l=len(A)
    A=list(A)
    s=''
    for i in range(l):
        A[i]=str(A[i])

    def isgreater(n1,n2):
        if n1+n2>n2+n1:
            return -1
        else:
            return 1

    A=sorted(A,key=cmp_to_key(isgreater))
    for i in A:
        s+=i
    return int(s)

print(largestNumber([3,30,34,5,9]))