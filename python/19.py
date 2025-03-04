#multiple inheritance
class A:
    def __init__(self,x,y):
            self.x=x
            self.y=y
    def out(self):
            print("x=",self.x)
            print("y=",self.y)
class B:
    def __init__(self,z):
            self.z=z
    def out1(self):
            print("z=",self.z)
class C(A,B):
    def __init__(self):
            A.__init__(self,10,30)
            B.__init__(self,40)
            print("done")
D=C()
D.out()
D.out1()