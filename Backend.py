
# Imports:
import pymysql
from Constants import HOST, USER, PASSWORD, DBNAME


class DB:
    '''
    A class to make connection between the DB that is located on the cloud, and the project.
    '''
    def __init__(self):
        '''
        Make basic connections.
        '''
        self.conn = pymysql.connect(host=HOST, user=USER, passwd=PASSWORD, connect_timeout=10)
        self.create_db()
        self.conn = pymysql.connect(host=HOST, user=USER, passwd=PASSWORD, connect_timeout=10, db=DBNAME)
        self.cursor = self.conn.cursor()
        self.create_table()

    def create_db(self):
        '''
        A function to create the db if is not exists.
        :return: None.
        '''
        try:
            with self.conn.cursor() as cur:
                # Creating db as per requirement
                cur.execute('create database ControlUp;')
        except:
            print("DB 'ControlUp' exists")

    def create_table(self):
        '''
        A function to create a table if is not exists.
        :return: None.
        '''
        try:
            # Creating table as per requirement
            sql ='''CREATE TABLE CONTROLUP(
               DATA_STAMP TIMESTAMP NOT NULL,
               PRODUCT_URL CHAR(200) NOT NULL,
               HIGHEST_PRICE FLOAT NOT NULL,
               LOWEST_PRICE FLOAT NOT NULL,
               AVG_PRICE FLOAT NOT NULL
            )'''
            self.cursor.execute(sql)
        except:
            print("Table 'CONTROLUP' exists")

    def add_entry(self, ts, url, h_price, l_price, avg_price):
        '''
        A function to add an entry to the db.
        :param ts: timestamp.
        :param url: an url.
        :param h_price: the highest price.
        :param l_price: the lowest price.
        :param avg_price: the average price.
        :return: None.
        '''

        # Preparing SQL query to INSERT a record into the database.
        sql = "INSERT INTO CONTROLUP VALUES (%s, %s, %s, %s, %s)"
        values = ts, url, h_price, l_price, avg_price
        try:
            # Executing the SQL command
            self.cursor.execute(sql, values)

            # Commit your changes in the database
            self.conn.commit()
            print("Data inserted")
        except Exception as e:
            # Rolling back in case of error
            self.conn.rollback()
            print(e)

    def get_all_data(self):
        '''
        A function to get all data from db.
        :return: all data in database.
        '''
        # Retrieving all rows in table
        sql = '''SELECT * from CONTROLUP'''

        # Executing the query
        self.cursor.execute(sql)
        # Fetching all rows from the table
        result = self.cursor.fetchall()
        return result

    def close_session(self):
        '''
        A function to close the connection with the db.
        :return: None.
        '''
        # Closing the connection
        self.conn.close()






