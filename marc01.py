class Drobe(object):
    def __init__(self, numup, numdown):
        self.chis = numup
        self.znam = numdown

    def drobeshow(self):
        drobeshow = str(self.chis) + '/' + str(self.znam)
        return drobeshow

    def plus(self, otherdrobe):
        pluschis = self.chis*otherdrobe.znam + otherdrobe.chis*self.znam
        plusznam = self.znam*otherdrobe.znam
        a = 1
        while a <= plusznam:
            if (pluschis % a == 0) and (plusznam % a == 0):
                pluschis = int(pluschis / a)
                plusznam = int(plusznam / a)
            a += 1
        plusres = str(pluschis) + '/' + str(plusznam)
        return plusres


a = Drobe(1, 2)
b = Drobe(1, 4)
c = a.plus(b)
print(a.drobeshow(), b.drobeshow())
print(c)
