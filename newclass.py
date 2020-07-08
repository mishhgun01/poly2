

class Polynom(object):


    def __init__(self,*args):
        self.listofargs = list([*args])


    def showSelf(self):
        sum = ''
        string = ''
        length = len(self.listofargs)
        i = 0
        while i <= (length - 2):
            if self.listofargs[i + 1] >= 0:
                    string = str(self.listofargs[i]) + 'x' + str(length - i - 1) + '+'
                    sum = sum + string
            elif self.listofargs[i + 1] <= 0:
                    string = str(self.listofargs[i]) + 'x' + str(length - i - 1)
                    sum = sum + string
            i += 1
        sum = sum[:-1]
        symb = self.listofargs[length-1]
        if symb > 0:
            symb = '+' + str(symb)
        else:
            symb = str(symb)
        sum = sum  + symb
        return print(sum)


    def getValue(self,x):
        sum = 0
        j = 0
        length = len(self.listofargs)
        for i in self.listofargs:
            while j <= length - 1:
                k = i * x**(length - j - 1)
                sum = sum + k
                j += 1
                break
        return print(sum)


    def getSum(self,other):
        i = 0
        j = 0
        newlist = []
        while i <= len(self.listofargs) - 1:
            while j <= len(other.listofargs) - 1:
                k = self.listofargs[i] + other.listofargs[j]
                newlist.append(k)
                j += 1
                break
            i += 1
        sum = ''
        string = ''
        length = len(newlist)
        i = 0
        while i <= (length - 2):
            if newlist[i + 1] >= 0:
                string = str(newlist[i]) + 'x' + str(length - i - 1) + '+'
                sum = sum + string
            elif newlist[i + 1] <= 0:
                string = str(newlist[i]) + 'x' + str(length - i - 1)
                sum = sum + string
            i += 1
        sum = sum[:-1]
        symb = newlist[length - 1]
        if symb > 0:
            symb = '+' + str(symb)
        else:
            symb = str(symb)
        sum = sum + symb
        return print(sum)


    def getSub(self, other):
        i = 0
        j = 0
        newlist = []
        while i <= len(self.listofargs) - 1:
            while j <= len(other.listofargs) - 1:
                k = self.listofargs[i] - other.listofargs[j]
                newlist.append(k)
                j += 1
                break
            i += 1
        sum = ''
        string = ''
        length = len(newlist)
        i = 0
        while i <= (length - 2):
            if newlist[i + 1] >= 0:
                string = str(newlist[i]) + 'x' + str(length - i - 1) + '+'
                sum = sum + string
            elif newlist[i + 1] <= 0:
                string = str(newlist[i]) + 'x' + str(length - i - 1)
                sum = sum + string
            i += 1
        sum = sum[:-1]
        symb = newlist[length - 1]
        if symb > 0:
            symb = '+' + str(symb)
        else:
            symb = str(symb)
        sum = sum + symb
        return print(sum)


    # def getMult(self,other):
    #     sum = 0
    #     i = 0
    #     j = 0
    #     newlist = []
    #     while i <= len(self.listofargs) - 1:
    #         while j <= len(other.listofargs) - 1:
    #             k = self.listofargs[i] * other.listofargs[j]
    #             sum = sum + k
    #             j += 1
    #             newlist.append(sum)
    #         i += 1
    #         j = 0
    #         sum = 0
    #     return print(newlist)