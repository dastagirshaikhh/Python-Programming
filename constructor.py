class Dude:
    def __init__(self, name, occ,nw):
        self.name = name
        self.occ = occ
        self.nw = nw

    def info(self):
        print(f"{self.name} is a {self.occ} and has a networth of {self.nw}")

a = Dude("Dastagir", "Berozgar Developer", 150)
b = Dude("Saud", "Gareeb Gym wala", 500)
c = Dude("Zeeshan", "Berozgar Engineer", -20000)
a.info()
b.info()
c.info()