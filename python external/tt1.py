l = list(map(int, input().split()))  
key = int(input())  
n = len(l)
for i in range(n):
    if key == l[i]:
        print("present")
        break
    else:
        print("not found")
