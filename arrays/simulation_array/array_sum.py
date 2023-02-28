#MEDIUM

'''     https://www.interviewbit.com/problems/array-sum/        '''

# Problem Description

# You are given two numbers represented as integer arrays A and B, where each digit is an element.
# You have to return an array which representing the sum of the two given numbers.
# The last element denotes the least significant bit, and the first element denotes the most significant bit.

# Input Format
# The first argument is an integer array A. The second argument is an integer array B.

# Output Format
# Return an array denoting the sum of the two numbers.

# Example Input

# Input 1:
# A = [1, 2, 3]
# B = [2, 5, 5]

# Input 2:
# A = [9, 9, 1]
# B = [1, 2, 1]

# Example Output

# Output 1:
# [3, 7, 8]

# Output 2:
# [1, 1, 1, 2]

# Example Explanation

# Explanation 1:
# Simply, add all the digits in their place.

# Explanation 2:
# 991 + 121 = 1112
# Note that the resultant array size might be larger.


def addArrays(A,B):
    s1,s2,l='','',[]
    for i in A:
        s1+=str(i)
    for i in B:
        s2+=str(i)
    n1=int(s1)
    n2=int(s2)
    s=n1+n2
    for i in str(s):
        l.append(i)
    return l

print(addArrays([1,2,3],[2,5,5]))