import collections
s = "the world is a small place and all the actors are players in it is the truth"
l=s.split(' ')
for i in s:
    d=dict(zip(l,range(len(l))))
    s1=list(d)
    a=sorted(d.items())
print(a)

