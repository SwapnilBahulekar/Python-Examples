import sys


def miniMaxSum(arr):
    # Complete this function

    minsum1=0
    maxsum1=0
    n=len(arr)-1
    for i in range(len(arr)-2):
        minsum1=minsum1+arr[:i]
        maxsum1=maxsum1+arr[i:]
        print(minsum1,maxsum1)



arr = [1,2,3,4,5]
miniMaxSum(arr)
