# Task description
# Write a function:

# def solution(A, B, K)

# that, given three integers A, B and K, returns the number of integers within the range [A..B] that are divisible by K, i.e.:

# { i : A ≤ i ≤ B, i mod K = 0 }

# For example, for A = 6, B = 11 and K = 2, your function should return 3, because there are three numbers divisible by 2 within the range [6..11], namely 6, 8 and 10.

# Write an efficient algorithm for the following assumptions:

# A and B are integers within the range [0..2,000,000,000];
# K is an integer within the range [1..2,000,000,000];
# A ≤ B.


# My Code
import math
def solution(A, B, K):
    answer = 0
    for i in range(A, B+1):
        if i % K == 0:
            answer = i
            break
    if A == B:
        if A % K == 0:
            return 1
        else:
            return 0
    return math.trunc(B/K - answer/K + 1)


# Result
# https://app.codility.com/demo/results/trainingFJFCVX-R8R/



# Copyright 2009–2023 by Codility Limited. All Rights Reserved. Unauthorized copying, publication or disclosure prohibited.