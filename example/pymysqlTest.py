import json

import pymysql

conn = pymysql.connect('cps-cps.mysql101011021.fat.homedo.com','write_fortest','Y,l+7L0w')
conn.select_db('saas_application')
cur=conn.cursor()
# cur.execute("SELECT id,mobile from user_resource_receive where id in ('489854027046449152','490106184568008704')")
cur.execute("SELECT id,repo_name from repository_application where id in (1001,1002,1003,1004,1005,1006,1007);" )
# while 1:
#     res=cur.fetchone()
#     if res is None:
#         #表示已经取完结果集
#         break
#     print (res)
data = cur.fetchall()
cur.close()
# conn.commit()
conn.close()
print(data)
jsonData = []
for row in data :
    result = {}
    result['id']=row[0]
    result['repo_name']=row[1]
    jsonData.append(result)
    jsondatar=json.dumps(jsonData, ensure_ascii=False)
    # print(jsondatar[1:len(jsondatar) - 1])
    # print(jsondatar)
print('##################')
print(type(jsonData))
print(jsonData)
print(type(jsondatar))
print(jsondatar[0])
print('sql执行成功')

class DataBase:
    _conn = None
    _cursor=None
    def __init__(self,conf,database):
        self.host = conf['host']
        self.user = conf['user']
        self.passwd = conf['passwd']
        self.database = database

    #连接数据库
    def connectDatabase(self):
        self._conn= pymysql.connect(self.host,self.user,self.passwd )
        self._conn.select_db(self.database)
        self._cursor = self._conn.cursor()

    # 关闭数据库
    def close(self):
        if self._conn and self._cursor:
            self._cursor.close()
            self._conn.close()
            print("Database closed!")

    # 执行sql语句   ---查询
    def execute(self,sql):
        self.connectDatabase()
        self._cursor.execute(sql)
        data= self._cursor.fetchall()
        return data


if __name__ == '__main__':
    sql="SELECT id,repo_name from repository_application where id in (1001,1002,1003,1004,1005,1006,1007);"
    con={"host":"cps-cps.mysql101011021.fat.homedo.com","user":"write_fortest","passwd":"Y,l+7L0w"}
    data = DataBase(con,"saas_application")
    # data.connectDatabase()
    print("%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%")
    res=data.execute(sql)
    data.close()
    print(res)
    print("%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%")

