import pyodbc
from configparser import ConfigParser
from ConnectionParser import config

class DBConnector:
   
    params = dict()
    conn_info = ''
    conn = pyodbc.Connection

    def __init__(self, filename):
        self.params = config(filename)
        self.conn_info = 'Driver=SQL Server;Database=% s;Server=% s;uid=% s;pwd=% s'% (self.params [0], self.params[1], self.params [2], self.params [3 ])
        self.conn = pyodbc.connect(self.conn_info)

    def getConnection(self):
        return self.conn

    def closeConnection (self):
        self.conn.close()








#conn = pyodbc.connect(Driver="SQL Server", Server="DESKTOP-UDM7FMJ", Database="TestDB", uid="sa", pwd="123456")





