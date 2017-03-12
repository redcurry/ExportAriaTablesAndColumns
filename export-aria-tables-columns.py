import pyodbc

connection = pyodbc.connect(
    'DRIVER={SQL Server};'
    'SERVER=server;'
    'DATABASE=variansystem;'
    'UID=username;'
    'PWD=password')

cursor = connection.cursor()
tables = [row.table_name for row in cursor.tables(tableType='TABLE')]

for table in tables:
    print(table)

    cursor = connection.cursor()
    columns = [row.column_name for row in cursor.columns(table)]

    for column in columns:
        print("  " + column)
