#!/bin/python3

import sys


def funnyString(s):
    # Complete this function
    s1 = s[::-1]
    for i in range(1,len(s)):
        n = abs(ord(s[i]) - ord(s[i - 1]))
        print(n)
        n1 = abs(ord(s1[i]) - ord(s1[i - 1]))
        print(n1)
        if (n!=n1):
            return "not funny"

    else:
        return "Not funny"


q = int(input().strip())
for a0 in range(q):
    s = input().strip()
    result = funnyString(s)
    print(result)
