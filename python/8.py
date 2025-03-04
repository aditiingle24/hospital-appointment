#add values using var len arg
def add(*val):
    """aditi ingle from hyderabad"""
    total=sum(val)
    return total
print("sum is:",add(4,8))
print("sum is:",add(1,2,3,4))
print(add.__doc__)