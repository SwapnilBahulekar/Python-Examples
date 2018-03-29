string1 = 'nutanixisasoftwareonlycompan'
l=list(string1)
n = len(l)
n1 = round(n/2)
for i in range(n1):
    l[i], l[n-i-1] = l[n-i-1], l[i]
    str1=''.join(l)
print(str1)

