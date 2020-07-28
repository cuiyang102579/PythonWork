import pymysql


class mysqlUtils:
    def __init__(self,host,user,pwd,dbname):
        self.conn = pymysql.connect(host, user, pwd)
        try:
            self.conn.select_db(dbname)
            self.cur = self.conn.cursor()
        except Exception as e:
            print("数据库不存在")
            return False
            # print(e)

    def __del__(self):
        self.cur.close()
        self.conn.close()


    def query_db(self,sql,state='all'):
        self.cur.execute(sql)
        if state == "all":
            # 使用 fetchall() 获取查询结果
            data = self.cur.fetchall()
        else:
            data = self.cur.fetchone()
        print(data)
        return data

    def excute_db(self,sql):
        try:
            self.cur.execute(sql)
            self.conn.commit()
            print("更新成功")
        except Exception as e:
            print(e)
            self.conn.rollback()
            return False

    def insert_db(self,sql,data):
        try:
            self.cur.executemany(sql,data)
            self.conn.commit()
        except Exception as e:
            print(e)
            self.conn.rollback()
            return False

if __name__ == '__main__':
    mysql= mysqlUtils('cps-cps.mysql101011021.fat.homedo.com','write_fortest','Y,l+7L0w','ind_linker')
    # mysql.query_db("SELECT id,mobile from user_resource_receive where id in ('489854027046449152','490106184568008704')")
    # mysql.excute_db("update user_resource_receive set resource_title='资料六04'  where id= '490613911375441920'")
    # mysql.query_db("SELECT * from user_resource_receive where id=490613911375441920")
    t1=0,'SEARCH_KEYWORD','测试118','1','全站搜索关键词'
    t2=0,'SEARCH_KEYWORD','测试119','1','全站搜索关键词'
    t3=[]
    t3.append(t1)
    t3.append(t2)
    print(t3)
    sql="insert into constants(id,type,code,val,description)  values (%s,%s,%s,%s,%s)"
    mysql.insert_db(sql,t3)






