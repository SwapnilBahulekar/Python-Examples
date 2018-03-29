#!/bin/python3

import sys


def bigSorting(arr):
    # Complete this function
    for i in range(len(arr)):
        for j in range(len(arr) - i - 1):
            if (arr[j] >arr[j + 1]):
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

    return arr

if __name__ == "__main__":
    n = 5
    arr = [6,312232123,1,3,10,3,5]
    arr_i = 0
    for arr_i in range(n):
        arr_t = str(input().strip())
        arr.append(arr_t)
    result = bigSorting(arr)
    print(result)
    print("\n".join(map(str, result)))


