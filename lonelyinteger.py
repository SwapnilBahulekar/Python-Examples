
import collections
class integer1():
    def lonelyint(self,arr,n):
        arr1=[]
        c=collections.Counter(arr)
        print(c)
        for key,value in c.items():
            if(value<2):
               arr1.append(key)
        return arr1


arr=[1,1,2,2,2,3]
n=5
l1=integer1()
x=l1.lonelyint(arr,n)
print(x)

