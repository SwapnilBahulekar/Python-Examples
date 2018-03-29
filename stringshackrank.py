import collections

class stringop():

    def countstring(self,s,n):
        c=collections.Counter(s)
        print(c)
        s1 = ""
        temp=s1
        for key,value in c.items():
            if (value!=2):
                s1 = s1 + key
                s2 = sorted(s1)
                s3 = ''.join(s2)
                if key not in s3:
                    s3=s3+key

            elif(s3==""):
                return "empty string"


        return s3



s="aaabccddd"
n=len(s)
l1=stringop()
x=l1.countstring(s,n)
print(x)














