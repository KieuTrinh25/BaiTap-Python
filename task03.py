import pandas as pd  
from mysql.connector import MySQLConnection, Error 

db_config = {
    'host': 'localhost',
    'database': 'task03',
    'user': 'root',
    'password': ''
}

file = pd.read_excel('input.xlsx', sheet_name='MAU', usecols='A:H', skiprows=10, nrows=52)
data = []
for row in file.iterrows():
    row_data = []
    for value in row[1]:
        row_data.append(value) 
    sql = "insert into students(id, masv, first_name, last_name, birthday, toan, ly, hoa) values (%s,%s,%s,%s,%s,%s,%s,%s)"
 
    val = (row_data[0],row_data[1],row_data[2],row_data[3],row_data[4],row_data[5],row_data[6],row_data[7])
    cursor = db_config.cursor()
    cursor.execute(sql, val)
    db_config.commit()
    data.append(row_data)
 



