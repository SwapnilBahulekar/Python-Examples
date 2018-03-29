#!/bin/python3

import sys


def solve(a0, a1, a2, b0, b1, b2):
    arr=[]
    brr=[]
    arr.append(a0)
    arr.append(a1)
    arr.append(a2)
    brr.append(b0)
    brr.append(b1)
    brr.append(b2)
    s=""
    for i in range(len(arr)):
        if arr[i]>brr[i]:
            s=s+"1"

        elif brr[i]>arr[i]:

            s=s+"1"



    return s



a0, a1, a2 = input().strip().split(' ')
a0, a1, a2 = [int(a0), int(a1), int(a2)]
b0, b1, b2 = input().strip().split(' ')
b0, b1, b2 = [int(b0), int(b1), int(b2)]
result = solve(a0, a1, a2, b0, b1, b2)
print(" ".join(map(str, result)))


