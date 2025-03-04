class base1:
    def __init__(self):
        super(base1,self).__init__()
        print("base 1")
class base2:
    def __init__(self):
        super(base2,self).__init__()
        print("base 2")
class derived(base1,base2):
    def __init__(self):
        super(derived,self).__init__()
        print("derived")
D=derived()