import psycopg2
import unittest
import datetime
import decimal

class testinput(unittest.TestCase):
    
    def test_data(data):
        
        #Get data from database
        connection = psycopg2.connect(database="tickerdb",
                        user='postgres', password='pass123', 
                        host='127.0.0.1', port='5432')
  
        connection.autocommit = True
        cursor = connection.cursor()

        cursor.execute("select * from ticker;")
        data = cursor.fetchall()
        connection.close()
        
        #Input validation:
        for d in data:
            assert type(d[0]) == datetime.datetime
            assert type(d[1]) == decimal.Decimal
            assert type(d[2]) == decimal.Decimal
            assert type(d[3]) == decimal.Decimal
            assert type(d[4]) == decimal.Decimal
            assert type(d[5]) == int
            assert type(d[6]) == str
                
if __name__ == '__main__':
    unittest.main()
        

