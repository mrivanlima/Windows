import pyodbc
import readconfig

from ConnectionParser import config


#create connection


params = config('sqlserver_conf.ini')

conn_info = 'DRIVER = {SQL Server}; DATABASE =% s; SERVER =% s; UID =% s; PWD =% s'% (params [0], params [1], params [2], params [3 ])

print (conn_info)

conn = pyodbc.connect(Driver="SQL Server", Server="DESKTOP-UDM7FMJ", Database="TestDB", uid="sa", pwd="123456")



cur = conn.cursor()



cur.execute("select * from TestTable")
rows = cur.fetchall()

if rows:
    print(*rows,sep="\n")
conn.close()


#conn1 = pyodbc.connect(Driver="SQL Server", Server="WS-406SK13", Database="Basics", Trusted_Connection = "Yes") 
#conn = pyodbc.connect(Driver="SQL Server", Server="DESKTOP-UDM7FMJ", Database="TestDB", uid="sa", pwd="123456")

#cursor = conn.cursor()

#cursor.execute("select * from TestTable")
#rows = cursor.fetchall()

#if rows:
#    print(*rows,sep="\n")
#conn.close()




