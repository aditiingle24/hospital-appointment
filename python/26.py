from abc import ABC, abstractmethod
class polygon(ABC):
    def noofside(self):
        pass
class tri(polygon):
    def noofside(self):
        print("3 sides")
class pen(polygon):
    def noofside(self):
        print("5 sides")
class hex(polygon):
    def noofside(self):
        print("6 sides")
class quad(polygon):
    def noofside(self):
        print("4 sides")
r=tri()
r.noofside()
k=pen()
k.noofside()
r=hex()
r.noofside()
k=quad()
k.noofside()