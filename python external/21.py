a=[1,2,3]
try:
    print("second ele=%d"%(a[1]))
    print("4=%d"%(a[3]))
except IndexError:
    print("error occured")