#!/bin/python3

import sys
import re


def hackerrankInString(s):
    # Complete this function'
    t=re.compile(r'.*h.*a.*c.*k.*e.*r.*a.*n.*k.*')
    matches=t.findall(s)
    if matches:
        return "YES"
    else:
        return "No"
if __name__ == "__main__":
    q = int(input().strip())
    for a0 in range(q):
        s = input().strip()
        result = hackerrankInString(s)
        print(result)
