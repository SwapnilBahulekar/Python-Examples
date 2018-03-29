'''arr=[6,3,2,123322344,5]
n=len(arr)

for i in range(len(arr)):
    for j in range(0,n-i-1):
        if(arr[j]>arr[j+1]):
            arr[j],arr[j+1]=arr[j+1],arr[j]
print("bubblesort",arr)


for i in range(len(arr)):
    min1=i
    for j in range(i+1,len(arr)):
        if(arr[i]>arr[j]):
            min1=j
    arr[i],arr[min1]=arr[min1],arr[i]
print("selection sort",arr)

for i in range(1,len(arr)):
    key=arr[i]
    j=i-1
    while(j>=0 and key < arr[j]):
        arr[j+1]=arr[j]
        j-=1
    arr[j+1]=key
print("insertion sort",arr)

#quicksort
# !/bin/python3

import sys


def quickSort(arr):
    # Complete this function
    low = arr[0]
    pivot = arr[n - 1]
    i = low - 1
    for i in range(len(arr) - 1):
        for j in range(0, pivot - 1):
            #print("success")
            if (low <= pivot):
                arr[j], arr[i] = arr[i], arr[j]
                i += 1
                return arr
            elif (low > pivot):
                return arr
    return None


'''


def insertionsort(arr):
    for i in range(1, len(arr)):

        key = arr[i]

        # Move elements of arr[0..i-1], that are
        # greater than key, to one position ahead
        # of their current position
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
            print(arr)
        arr[j + 1] = key

    return arr


if __name__ == "__main__":
    n = 4
    arr = [6,3,23423,2,14]
    result = insertionsort(arr)
    print(result)
    #print(" ".join(map(str, result)))


