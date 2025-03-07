arr = [int(x) for x in input().split()]
i = 0
mid = len(arr)//2
while i<mid:
    arr[i],arr[len(arr)-i-1]=arr[len(arr)-i-1], arr[i]
    i+=1
print(arr)
