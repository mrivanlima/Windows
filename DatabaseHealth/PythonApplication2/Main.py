import readconfig
from ConnectionParser import config
from Connector import DBConnector


connector = DBConnector('sqlserver_conf.ini')
conn = connector.getConnection()


cur = conn.cursor()
cur.execute("select * from TestTable")
rows = cur.fetchall()

if rows:
    print(*rows,sep="\n")
conn.close()






