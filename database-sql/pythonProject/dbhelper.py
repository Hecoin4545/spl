import sys

import mysql.connector

# how to connect to the sql database

class DbHelper:
    def __init__(self):
        try:
            self.conn = mysql.connector.connect(host='localhost' , user='root' , password='' , database='campusx-sq')
            self.mycursor = self.conn.cursor()
        except:
            print('some eror occured')
            sys.exit(0)
        else:
            print('connected to the database')

    def register(self , name , email , password):
        try:
            self.mycursor.execute("""
            INSERT INTO `users` (`id` , `name` , `email` , `password`)  VALUES (NULL , '{}','{}','{}');
            """.format(name , email , password))
            self.conn.commit()
        except:
            return -1
        else:
            return 1

    def search(self,email,password):
        self.mycursor.execute("""
        SELECT * FROM users WHERE email LIKE '{}' AND password LIKE '{}'
        """.format(email , password))

        data = self.mycursor.fetchall()
        print(data)



