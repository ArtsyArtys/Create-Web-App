from psycopg2 import sql, connect
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT


def connectdb(database, dbname, user_name, password = ''):
    if database == "PostgreSQL":
        con = connect(
        user = user_name, host='',
        password = password)
        print(con)
        con.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
        cur = con.cursor()

        cur.execute("CREATE DATABASE " + dbname + r";")

# connectdb("PostgreSQL", 'rawr', 'randy', '')
