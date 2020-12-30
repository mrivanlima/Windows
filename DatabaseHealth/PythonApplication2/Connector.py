import pyodbc
from configparser import ConfigParser
from ConnectionParser import config

class DBConnector:
   
    params = dict()
    conn_info = ''

    def __init__(self, filename):
        self.params = config(filename)
        self.conn_info = 'Driver=SQL Server;Database=% s;Server=% s;uid=% s;pwd=% s'% (self.params [0], self.params[1], self.params [2], self.params [3 ])

    def getConnection(self):
        return pyodbc.connect(self.conn_info)









#conn = pyodbc.connect(Driver="SQL Server", Server="DESKTOP-UDM7FMJ", Database="TestDB", uid="sa", pwd="123456")





