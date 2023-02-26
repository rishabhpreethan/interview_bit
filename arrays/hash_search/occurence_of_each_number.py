#MEDIUM

'''     https://www.interviewbit.com/problems/occurence-of-each-number/     '''

# Problem Description

# You are given an integer array A.
# You have to find the number of occurences of each number.
# Return an array containing only the occurences with the smallest value's occurence first.
# For example, A = [4, 3, 3], you have to return an array [2, 1], where 2 is the number of occurences for element 3, 
# and 1 is the number of occurences for element 4. But, 2 comes first because 3 is smaller than 4.


def findOccurences(A):
    d={}
    A.sort()
    for i in A:
        if i in d:
            d[i]+=1
        else:
            d[i]=1
    l=list(d.values())
    return l

print(findOccurences([4,3,3]))