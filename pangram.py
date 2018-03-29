# Enter your code here. Read input from STDIN. Print output to STDOUT\
import collections

def contains(s,s1):
    s2=s.replace(" ","")
    c=collections.Counter(s2)
    c1=len(c)
    if c1==26:
        return True
    else:
        return False


s = "We promptly judged antique ivory buckles for the prize"
s1 = "abcdefghijklmnopqrst"
l0 = list(s)
l1 = list(s1)
x=contains(s,s1)
if x == True:
    print("pangram")
else:
    print("not pangram")
