class rec:
    def __init__(self,l,b):
        self.l=l
        self.b=b
    def area(self):
        return self.l*self.b
    @classmethod
    def sq(cls,side):
        return cls(side,side)
r=rec.sq(4)
print(r.area())