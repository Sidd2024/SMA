import psycopg2

#Connect to database
connection = psycopg2.connect(database="tickerdb",
                        user='postgres', password='pass123', 
                        host='127.0.0.1', port='5432'
)
  
connection.autocommit = True
cursor = connection.cursor()

#insert data into database from csv.
sql2 = '''COPY ticker(datetime,close,high,low,open,volume,instrument)
FROM 'C:\\Users\\sid\Desktop\\invsto-task\\data.csv'
DELIMITER ','
CSV HEADER;'''

cursor.execute(sql2)

#print the data inserted into database.
sql3 = '''select * from ticker;'''
cursor.execute(sql3)
for i in cursor.fetchall():
    print(i)
  
connection.commit()
connection.close()