import pymysql

# mysql 基础版
# 连接MySQL
conn = pymysql.connect(
    host='localhost',
    port=3306,
    user="root",
    password="",
    charset="utf8",
    db="unicom",
)
cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)

# 发送指令
cursor.execute("insert into admin(username, password, mobile) "
               "values ('wxy', 'xxx', 'wwww123')")
conn.commit()

# 关闭MySQL
cursor.close()
conn.close()