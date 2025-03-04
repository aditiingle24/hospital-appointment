#multilevel inheritance
class person:
    def name(self):
        print("name=ria")
class teacher(person):
    def age(self):
        print("age=45")
class expe(teacher):
    def exp(self):
        print("24")
n=expe()
n.name()
n.age()
n.exp()