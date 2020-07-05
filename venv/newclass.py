class polynom(object):
    def __init__(self,x,a,b,c,d,e):
        self.x = x
        self.a = a
        self.b = b
        self.c = c
        self.d = d
        self.e = e

    def polynomshow(self):
        pol = str(self.a)+'x4'+'+'+str(self.b)+'x3'+'+'+str(self.c)+'x2'+'+'+str(self.d)+'x'+'+'+str(self.e)+'=0'
        return print(pol)

    def polynomznach(self):
        polynom = self.a*self.x**4 + self.b*self.x**3 + self.c*self.x**2 + self.d*self.x + self.e
        return polynom

    def polynomsravn(self,other):
        if self.a == other.a:
            if self.b == other.b:
                if self.c == other.c:
                    if self.d == other.d:
                        if self.e == other.e:
                            return print('равны')
        else:
            return print('не равны')

    def polynomslozh(self,other):
        newa = self.a + other.a
        newb = self.b + other.b
        newc = self.c + other.c
        newd = self.d + other.d
        newe = self.e + other.e
        pol = str(newa) + 'x4' + '+' + str(newb) + 'x3' + '+' + str(newc) + 'x2' + '+' + str(
            newd) + 'x' + '+' + str(newe) + '=0'
        return pol
    
a = polynom(1,2,3,4,5,6)
a.polynomshow()
c = a.polynomznach()
print('a = ', c)
b = polynom(1,3,4,5,6,7)
b.polynomshow()
z = a.polynomslozh(b)
print('результат сложения - ', z)
a.polynomsravn(b)