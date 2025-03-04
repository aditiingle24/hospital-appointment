class rec:
    def __init__(self,l,b):
        self.l=l
        self.b=b
    def area(self):
        return self.l*self.b
    @classmethod
    def sq(cls,l,b):
        return cls(l,b)
r=rec.sq(2,5)
print(r.area())