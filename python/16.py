#area of square
class rec:
    def __init__(self,l,b):
        self.l=l
        self.b=b
    def area(self):
        return self.l*self.b
    @classmethod
    def sq(cls,side):
        return cls(side,side)
s=rec.sq(4)
print("area is:",s.area())