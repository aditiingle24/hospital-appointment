#multiple inheritance using super
class base1:
    def __init__(self):
        super(base1,self).__init__()
        print("base 1 class")
class base2:
    def __init__(self):
        super(base2,self).__init__()
        print("base 2 class")
class derived(base1,base2):
    def __init__(self):
        super(derived,self).__init__()
        print("derived clsas")
D=derived()