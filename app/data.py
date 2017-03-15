import pymysql
from flask import flash
config = {
    'host': '127.0.0.1',
    'port': 3306,
    'user': 'root',
    'password': 'passwd',
    'db': 'messages',
    'charset': 'utf8mb4',
    'cursorclass': pymysql.cursors.DictCursor,
}
def Post(content):
    connection = pymysql.connect(**config)
    c = connection.cursor()
    if content!=" " and content and content!='null':
        sql="insert into message values('"+content+"')"
        c.execute(sql)
        connection.commit()
        connection.close()
        return True
    else:
        connection.close()
        return False



def getPost():
    connection = pymysql.connect(**config)
    c = connection.cursor()
    sql = "select content from message"
    c.execute(sql)
    results =c.fetchall()
    connection.close()
    return results
