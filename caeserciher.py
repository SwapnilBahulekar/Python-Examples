#!/bin/python3

import sys

import re
def caesarCipher(s, k):

    s2=""
    for i in s:
        if i.isalpha():
            n='a' if i.islower() else 'A'
            s2+=chr(ord(n)+((ord(i)-ord(n)+k) % 26))
        else:
            s2=s2+i

    return s2



# Complete this function


if __name__ == "__main__":
    n = int(input().strip())
    s = input().strip()
    k = int(input().strip())
    result = caesarCipher(s, k)
    print(result)
