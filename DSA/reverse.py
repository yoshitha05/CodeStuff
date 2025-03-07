arr = [int(x) for x in input().split()]
n = len(arr)

def maxnmin(arr, n):
    curr = 0
    max2 = 0
    for i in range(0, n):
        if (arr[i]>curr):
            max2 = curr
            curr = arr[i]
        elif (arr[i]>max2 and arr[i]<curr):
            max2 = arr[i]
    return curr, max2

print("Maximum and Minimum element of an Array are:", maxnmin(arr,n))
