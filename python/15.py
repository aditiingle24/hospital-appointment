#area of rec
class rec:
    def __init__(self,l,b):
        self.l=l
        self.b=b
    def area(self):
        return self.l*self.b
    @classmethod
    def sq(cls,l,b):
        return cls(l,b)
s=rec.sq(2,4)
print("area:",s.area())