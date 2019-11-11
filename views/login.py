#!/usr/local/bin/python3

# note there should a Main View class()
# we will not create the View base class, as we need more details
# on what information should be stardardized or abstracted from each
# views

class View:
    @property
    def modTitle(self):
        return self.title

    @modTitle.setter
    def modTitle(self,modTitle):
        self.modTitle = modTitle

### is it better to just create a JSON document listing
### all the objects and their properties, plus the actions
### and validators available for that

class Login:
    def __init__(self,name):
        self.name = name

    @property
    def uid(self):
        return "UID value is: {} ".format(self._uid)

    @uid.setter
    def uid(self, uval):
         self._uid = uval
         return self._uid

a = Login(name='Lester')
a.uid = 23453
print(a.uid)
