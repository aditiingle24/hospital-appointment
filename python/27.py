a=[1,2,3]
try:
    print("2 ele= %d"%(a[1]))
    print("1 ele=%d"%(a[0]))
    print("4 ele=%d"%(a[3]))
except IndexError:
    print("an error occured")