import json

import pymysql

conn = pymysql.connect('cps-cps.mysql101011021.fat.homedo.com','write_fortest','Y,l+7L0w')
conn.select_db('ind_linker')
cur=conn.cursor()
cur.execute("SELECT id,mobile from user_resource_receive where id in ('489854027046449152','490106184568008704')")
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
    result['mobile']=row[1]
    jsonData.append(result)
    jsondatar=json.dumps(jsonData, ensure_ascii=False)
    # print(jsondatar[1:len(jsondatar) - 1])
    # print(jsondatar)
print('sql执行成功')
