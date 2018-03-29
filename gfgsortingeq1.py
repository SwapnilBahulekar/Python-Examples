import collections
class operations():
    def find(self, arr, l, r, key):

        while (l <= r):
            mid = round(l + (r - l) / 2)

            if (arr[mid] == key):
                return mid
            elif (arr[mid]<key):
                l = mid + 1
            elif (arr[mid] > key):
                r = mid - 1
        return -1

    def insert(self,arr,n,key,pos):
        arr.insert(pos,key)
        return arr

    def delete(self,arr,n,pos):
       arr1=[]
       for i in range(n):
           if i is not pos:
               arr1.append(arr[i])

       return arr1


    def partition(self,arr,low,n):
        print("in partition")
        i = low - 1
        pivot=arr[n-1]

        for j in range(low,n-1):
            if(arr[j]<=pivot):
                i = i + 1
                arr[i],arr[j]=arr[i],arr[j]

        arr[i+1],arr[n-1]=arr[n-1],arr[i+1]
        return i+1

    def quicksort(self,arr,low,n):
        print("in quicksort")
        if low<n-1:
            print("in")
            l1=operations()
            pi=l1.partition(arr,low,n)
            l1.quicksort(arr,low,pi-1)
            l1.quicksort(arr,pi+1,n)




    def removeduplicates(self,arr,n):
        c=collections.Counter(arr)
        duplicates=[i for i in c if c[i]>1 ]
        for i in range(n):
            while i in duplicates:
                pos=i
                a1=l1.delete(arr,n,pos)
                if i not in duplicates:
                    return c



arr = [6,2,3,7,9,6,6]
n = len(arr)
key = 2
pos=3
l1 = operations()

low=0
#l1.quicksort(arr,low,n)


x = l1.find(arr, 0, len(arr)-1, key)
#y= l1.insert(arr,n,2,pos)
#z=l1.delete(arr,n,2)
z=l1.removeduplicates(arr,n)
print(z)
