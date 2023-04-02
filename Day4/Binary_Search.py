
def serach(arr,x,low,high):
    while(low<high):
        mid = low+(high-low)//2
        if arr[mid] == x:
            return True
        elif arr[mid]<x:
            low = mid+1
        else:
            high = mid-1
    return False






arr = [10,20,30,40,70,50,90]
arr.sort()
x = 30
print(serach(arr,x,0,len(arr)-1))