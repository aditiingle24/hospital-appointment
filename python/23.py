#hybrid inheritance
class ani:
    def speaks(self):
        print("animal speaks")
class dog(ani):
    def barks(self):
        print("dog barks")
class cat(ani):
    def meao(ani):
        print("cat meoa")
class puppy(dog,cat):
    def play(self):
        print("puppy plays")
p=puppy()
p.speaks()
p.barks()
p.meao()
p.play()