def binary(a, k, i, j):
    if i <= j:
        mid = (i + j) / 2  
        if k == a[mid]:
            return mid  
        elif a[mid] > k:
            return binary(a, k, i, mid - 1)  
        else:
            return binary(a, k, mid + 1, j)  
    return -1  
a = list(map(int, input().split()))  
k = int(input())  

a.sort()

i = 0
j = len(a) - 1

result = binary(a, k, i, j)

print(result)
