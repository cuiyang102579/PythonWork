import pymysql
import readConfig as readConfig
from common.Log import Log

localReadConfig = readConfig.ReadConfig()


class DataBase:
    _conn = None
    _cursor = None

    def __init__(self,conf,database):
        self.log =Log()
        self.host = conf['host']
        self.user = conf['user']
        self.passwd = conf['passwd']
        self.database = database

        # 连接数据库
    def connectDatabase(self):
        try:
            self._conn = pymysql.connect(self.host, self.user, self.passwd)
            self._conn.select_db(self.database)
            self._cursor = self._conn.cursor()
            self.log.info("Connect DB successfully!")
        except ConnectionError as ex:
            self.log.error(str(ex))

     # 执行sql语句   ---查询
    def execute(self, sql):
        self.connectDatabase()
        self._cursor.execute(sql)
        data = self._cursor.fetchall()
        return data


    # def executeSQL(self, sql, params):
    #     self.connectDB()
    #     # executing sql
    #     self.cursor.execute(sql, params)
    #     # executing by committing to DB
    #     self.db.commit()
    #     return self.cursor

    # def get_all(self, cursor):
    #     #     value = cursor.fetchall()
    #     #     return value
    #     #
    #     # def get_one(self, cursor):
    #     #     value = cursor.fetchone()
    #     #     return value

    # 关闭数据库
    def close(self):
        if self._conn and self._cursor:
            self._cursor.close()
            self._conn.close()
            print("Database closed!")


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
