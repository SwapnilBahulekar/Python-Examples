#!/bin/python3

import os
import sys


#
# Complete the plusMinus function below.
#
def plusMinus(arr):
    #
    # Write your code here.
    count1 = 0
    count2=0
    count3=0
    total1=0.0
    total2=0.0
    total3=0.0
    for i in arr:
        if (i > 0):
            count1 += 1
            total1 = float(count1/len(arr))
        elif (i < 0):
            count2 += 1
            total2 = float(count2/ len(arr))
        else:
            count3 += 1
            total3 = float(count3/ len(arr))
    print(total1)
    print(total2)
    print(total3)


if __name__ == '__main__':
    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)

