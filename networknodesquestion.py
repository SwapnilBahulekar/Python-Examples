import random

l=[1,2,3,4]

arr=[]
while range(len(l)):
    a=random.choice(l)
    arr.extend(a)

print(arr)
print(set(a))
print(set(l)-set(a))

