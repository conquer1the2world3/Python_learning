import pymysql

username = '张三'
passwd = '123456'

try:
    print("Attempting to connect to database...")
    cnn = pymysql.connect(
        host='localhost',
        user='zfsjlll',
        password='yyt010324',
        database='test',
        charset='utf8',
        autocommit=True
    )
    print("Database connection successful!")
    print(cnn.get_server_info())

    # sql = 'select * from person'
    # with cnn.cursor() as cur:
    #     print("Executing SQL query:", sql)
    #     cur.execute(sql)
    #     result = cur.fetchall()
    #     print("Query results:", result)
    
    # sql = 'insert into person (username, passwd) values (%s, %s)' 
    # with cnn.cursor() as cur:
    #     print("Executing SQL query:", sql)
    #     cur.execute(sql, (username, passwd))
    #     print("Insert operation successful!")

    # sql = 'update person set username = %s where passwd = %s'
    # with cnn.cursor() as cur:
    #     print("Executing SQL query:", sql)
    #     cur.execute(sql, (username, passwd))
    #     print("Update operation successful!")
    # sql = 'delete from person where username = %s'
    # with cnn.cursor() as cur:
    #     print("Executing SQL query:", sql)
    #     cur.execute(sql, (username))
    #     print("Delete operation successful!")

    cnn.begin()
    sql1 = 'insert into person (username, passwd) values (%s, %s)'
    sql2 = 'update person set username = %s where passwd = %s'
    sql3 = 'delete from person where username = %s'
    with cnn.cursor() as cur:
        cur.execute(sql1, (username, passwd))
        cur.execute(sql2, ('李四', passwd))
        cur.execute(sql3, (username))
        print("Transaction successful!")
    cnn.commit()
except pymysql.Error as err:
    print(f"Database error: {err}")
except Exception as e:
    cnn.rollback()
    print(f"An error occurred: {e}")
finally:
    cur.close()
    if 'cnn' in locals():
        cnn.close()
        print("Database connection closed.")



