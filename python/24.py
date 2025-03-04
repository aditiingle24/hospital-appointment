#method overriding
class bird:
    def intro(self):
        print("there are so many birds")
    def flight(self):
        print("some can fly and some cannot")
class sparrow(bird):
    def flight(self):
        print("sparrow can fly")
class ostrich(bird):
    def flight(self):
        print("ostrich cannot fly")
b=bird()
b.intro()
b.flight()
s=sparrow()
s.intro()
s.flight()
o=ostrich()
o.intro()
o.flight()