def linear_search(arr,n,x):
    for i in range(0,n):
        if (arr[i] == x):
            return True
        return False




arr = [10,20,30,40,50]
x = 10
n= len(arr)
if (linear_search(arr,x,n)):
    print("Element Found")
else:
    print("Element not found")
