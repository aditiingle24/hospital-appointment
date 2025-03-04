l = list(map(int, input().split()))  
key = int(input())  
def binary(l, key):
    i = 0
    j = len(l) - 1
    while i <= j:
        mid = (i + j) // 2  
        if key == l[mid]:
            return mid 
        elif key > l[mid]:
            i = mid + 1  
        else:
            j = mid - 1  
    return -1 
result = binary(l, key)
if result != -1:
    print("element found")
else:
    print("Element not found")
