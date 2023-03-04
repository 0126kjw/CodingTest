# 문제 내용

# An array A consisting of N different integers is given. The array contains integers in the range [1..(N + 1)], which means that exactly one element is missing.

# Your goal is to find that missing element.

# Write a function:

# def solution(A)

# that, given an array A, returns the value of the missing element.

# For example, given array A such that:

#   A[0] = 2
#   A[1] = 3
#   A[2] = 1
#   A[3] = 5
# the function should return 4, as it is the missing element.

# Write an efficient algorithm for the following assumptions:

# N is an integer within the range [0..100,000];
# the elements of A are all distinct;
# each element of array A is an integer within the range [1..(N + 1)].


# 나의 풀이
def solution(A):
    if len(A) == 0:
        return 1
    else:
        num = sorted(A)
        for i in range(len(A)):
            if num[i] != i+1:
                return i+1
        return i+2
    
# 결과
# https://app.codility.com/demo/results/training7Z7N7U-DMR/


# Copyright 2009–2023 by Codility Limited. All Rights Reserved. Unauthorized copying, publication or disclosure prohibited.