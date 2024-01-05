"""
查询数据库、占位符替换代码逻辑
"""
import pymysql

db_config = {
    "host": "127.0.0.1",
    "port": 3306,
    "user": "root",
    "password": "",
    "charset": "utf8",
    "db": "unicom",
}

sql = "select * from admin"
# with 连接数据库
with pymysql.connect(**db_config) as conn:
    with conn.cursor(cursor=pymysql.cursors.DictCursor) as cursor:
        cursor.execute(sql)
        data_list_all = cursor.fetchall()
        print(data_list_all)
        data_list_size = cursor.fetchmany(1)
        print(data_list_size)