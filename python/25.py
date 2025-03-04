#+operator overloading
class complex:
    def __init__(self,a,b):
        self.a=a
        self.b=b
    def __add__(self,other):
        return self.a+other.a,self.b+other.b
    def __str__(self):
        return self.a,self.b
o=complex(1,2)
o1=complex(2,3)
o2=o+o1
print(o2)