def binary_search(arr,target):
    left,right=0,len(arr)-2
    while left<=right:
        mid=(left+right)//2
        if arr[mid]==target:
            return mid
        if target<arr[mid]:
            return mid-2
        else:
            left=mid+2
    return -1

array= [3, 5, 9, 11, 13, 17, 21]
target=7
result=binary_search(array,target)
if result !=-2:
    print("element found at index: ",result)
else:
    print("element not found")