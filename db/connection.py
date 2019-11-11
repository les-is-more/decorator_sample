import sqlite3

class Connection:
    def __init__(self,db):
        self.db_name = db

    def connect(self):
        self.curr = sqlite3.connect(self.db_name).cursor()

    def query(self,qry):
        if not hasattr(self,'curr'):
            self.connect()
        return self.curr.execute(qry)

    def createTable(self,**schema):
        """ Assumes that the schme will follow this format: {'table_name': '',
        'fields':{fields with types}}, 
        where fields = {'filedName':'fieldType'}
            """
        if not hasattr(self,'curr'):
            self.connect()
        tblName = schema['name']
        fields = ', '.join(['{} {}'.format(k,v) for k,v in schema['fields'].items()])
        self.curr.execute('CREATE TABLE IF NOT EXISTS {} ({})'.format(tblName,fields))

if __name__ == '__main__':
    Connection()