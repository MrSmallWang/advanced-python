"""
try advanced version
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


# 通过用户输入动态实现insert
while 1:
    username = input("请输入用户名：")
    if username.upper() == "Q":
        break
    pwd = input("请输入密码：")
    mobile = input("请输入手机号：")

    # 使用with语句，并进行pymysql中的占位符进行替换
    sql = "insert into admin(username, password, mobile) values (%s, %s, %s)"
    with pymysql.connect(**db_config) as conn:
        with conn.cursor(cursor=pymysql.cursors.DictCursor) as cursor:
            # 执行相关SQL语句
            cursor.execute(sql, [username, pwd, mobile])

        # 注意这里的commit语句要加在第二个with结束之后！！
        conn.commit()