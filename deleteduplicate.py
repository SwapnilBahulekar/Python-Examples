#!/bin/python3

import sys
import collections


def birthdayCakeCandles(n, ar):
    # Complete this function
    ar1=ar.count(max(ar))
    return ar1

n = int(input().strip())
ar = list(map(int, input().strip().split(' ')))
result = birthdayCakeCandles(n, ar)
print(result)
