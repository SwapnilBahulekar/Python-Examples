#!/bin/python3

import sys


def solve(grades):
    # Complete this function
    for i in range(len(grades)):
        grade1 = []
        if (grades[i] >= 38):
            if (grades[i] % 5 >=3):
                grades[i] += (5 - (grades[i] % 5))

    return grades





n = 4
grades = [73,67,38,33]
grade1 = []
grades_i = 0
'''for grades_i in range(n):
    grades_t = int(input().strip())
    grades.append(grades_t)'''
result = solve(grades)
print(result)
print("\n".join(map(str, result)))
