try:
    a=int(input("a="))
    b=int(input("b="))
    c=a/b
    print("a/b=%d"%c)
except Exception:
    print("cant divide by zero")
else:
    print("hi")
    