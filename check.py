import pymysql

connection = pymysql.connect(
    host='localhost',
    user='root',
    password='',
    database='user'
)

try:
    with connection.cursor() as cursor:
        cursor.execute("SELECT VERSION()")
        version = cursor.fetchone()
        print("Database version:", version)
finally:
    connection.close()
