#hirerical inheritance
class ani:
    def sound(self):
        print("animal makes sound")
class dog(ani):
    def sound(self):
        print("dog barks")
class cat(ani):
    def sound(self):
        print("cat says meao")
d=dog()
c=cat()
d.sound()
c.sound()