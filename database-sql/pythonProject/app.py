import sys
from dbhelper import DbHelper
class Flipkart:
    def __init__(self):
        # connect to the database
        self.db = DbHelper()
        self.menu()

    def menu(self):
        user_input = input("""
        1. enter 1 to register
        2. enter 2 to login
        3. anything else to leave
        """)

        if user_input == '1':
            self.register()
        elif user_input == '2':
            self.login()
        else:
            sys.exit(1000)
    def register(self):
        name = input("Exter your name")
        email = input("Exter your email")
        password = input("Exter your password")
        response = self.db.register(name , email , password)

        if response:
            print('registration complected')
        else:
            print('failed')
        self.menu()
    def login(self ):
        email = input("enter email")
        password = input("enter password")
        self.db.search(email , password)




Obj = Flipkart()

