import sys
import re


def minimumNumber(n, password):
    # Return the minimum number of characters to make the password strong
    count = 0

    if (len(password) >= 6):
        flag = -1
    if not (re.search(r'[a-z]', password)):
        flag = -1
        count += 1
        #print("in[a-z]")
    if not (re.search(r'[A-Z]', password)):
        flag=-1
        count+=1
        #print("in [A-Z]")

    if not (re.search(r'[0-9]', password)):
        flag = -1
        count += 1
        #print("in[0-9]")

    if not (re.search(r"[-!@#$%^&*()+]", password)):
        flag = -1
        count += 1
        #print("in[#]")

    else:
        flag = 0

    if (count >=4 and flag == 0):
        return "strong password"
    else:
        return max(count, 6 - n)


if __name__ == "__main__":
    n = int(input().strip())
    password = input().strip()
    answer = minimumNumber(n, password)
    print(answer)
