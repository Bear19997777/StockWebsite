import pandas as pd
from sqlalchemy import create_engine,MetaData
import sqlite3 as sq
# import mysql.connector
import pymysql
sqconn = sq.connect("/Users/zhuangjunrong/Documents/Project/stock_website/tensorflow_stock/website/database/data.db")
# engine = create_engine('postgresql://bear:12345@localhost/stockwebsite', echo=False)
# engine = create_engine('mysql://root:bear1234@localhost/autotrader', echo=False)

engine = create_engine("mysql+pymysql://root:bear1234@localhost:3306/autotrader")
# mysql://user:password@server
# engine = mysql.connector.connect(
#   host="localhost",
#   user="root",
#   password="bear1234",
#   database="autotrader"
# )
cursor = sqconn.cursor()

cursor.execute("SELECT name FROM sqlite_master WHERE type='table'")
# cursor.execute("SELECT name FROM sqlite_schema WHERE type='table' ORDER BY name;")
tables = cursor.fetchall()
# print(sqdbdf)
for table in tables:

    table_val = table[0]
    print(table_val)
    list1 = ["sqlite_sequence", "django_migrations", "django_content_type",
             "auth_permission", "auth_user", "django_session", "auth_user_user_permissions", "django_admin_log",
             "auth_group","auth_group_permissions","auth_user_groups"]
    if table_val in list1:
        continue



    # table_val = "CNN_RESULT"

    sql3data = pd.read_sql_query(f"SELECT * from {table_val}",sqconn)

    sql3data.to_sql(name=table_val, con=engine, if_exists='replace', index=False, chunksize=1000)
yy"