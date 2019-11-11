#console printing
from collections import OrderedDict 

class ConsolePrinter:
    def __init__(self, session):
        pass

    def navBar():
        pass

    def options():
        pass

    def printConsoleOptions(self,**kwds):
        i,tempText = 1, ''
        for k, v in kwds.items():
            tempText += '{} {}. {:20}'.format('\t' * 1, k, v)
            if i % 2 == 0 or i == kwds.__len__():
                print(tempText)
                tempText = ''
            i += 1

    def navBar(self):
        self.modSpecs['modTitle']
        print("{} [{}] {}".format('=' * 20,self.modSpecs['modTitle'].upper(), '=' * 20))
        self.longtextPrint(self.game_desc,60)
        self.printConsoleOptions(**self.createConsoleDict(Session.__consoleMainOptions))

    def longtextPrint(self,t,l): 
        for i in range(int(t.__len__() / l) + 1):
            print("{}".format(t[i * l: min((i + 1) * l,t.__len__())]))
    
    def __call__(self):
        self.navBar()

