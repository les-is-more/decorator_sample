import sqlite3

class Session:
    def __init__(self,db):
        self.db_name = db
        
    def connect(self):
        self.curr = sqlite3.connect(self.db_name).cursor()

    def query(self,qry):
        if not hasattr(self,'curr'):
            self.connect()
        return self.curr.execute(qry)

    def createTable(self,**schema):
        if not hasattr(self,'curr'):
            self.connect()
        tblName = schema.keys()[0]
        fields = ', '.join(['{} {}'.format(k,v) for k,v in account_schema.values()[0].items()])
        self.curr.execute('CREATE TABLE IF NOT EXISTS {} ({})'.format(tblName,fields))

    def createConsoleDict(self,lst):
        tempDict = OrderedDict(zip(list(string.ascii_letters.upper())[0:lst.__len__()],
                lst))
        return tempDict
