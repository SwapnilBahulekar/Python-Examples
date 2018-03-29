import re
import collections


class Ipaddr():
    def validip(self,s):

        l=[]
        for i in range(len(s)-1):
            l=s.split('.')
            if len(l)==4:
                l1=map(int,l)
                if(l[0]!=0):
                    return False
                    if(max(l1)<256):
                        return True
                else:
                    return False
            else:
                return False

        return False


s="0.0.0.0"
l1=Ipaddr()
x=l1.validip(s)
if(x==True):
    print("valid ip")
else:
    print("not a valid ip")
