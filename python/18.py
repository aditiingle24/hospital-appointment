#single inheritance
class person:
    def name(self):
        print("aditi")
class student(person):
    def area(self):
        print("hyd")
c=student()
c.name()
c.area()