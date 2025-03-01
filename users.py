from database import DatabaseManager


class User:
    def __init__(self):
        self.db = DatabaseManager()
        self.email_list = ('gmail.com', 'yahoo.com', 'me.com', 'mac.com', 'outlook.com')
        self.name = ''
        self.email = ''
        self.password = ''
        #add other key variables that we want to look for? (risk appetite, bookmarked sticks etc?)

    def create_account(self):
        print("Hi! We're hapy that you're creating an account with us. Please fill in the following information please.")
        self.name = input("Name: ")
        self.email = input("Email: ")
        self.password = input("Password: ")
        if self.db.add_user(name=self.name, password=self.password, email=self.email):
            print("Your account has been successfully created!")
            return False
        else:
            print("You already have an account with us, please login instead")
            return True

    def login(self):
        email = input("Email: ")
        password = input("Password: ")
        if self.db.email_check(email) == 0:
            return False
        else:
            if self.check_password(email, password):
                self.name = self.db.get_name(email)
                self.email = email
                self.password = password
                return True
            else:
                print('You have entered the wrong password :(')
                change_password_question = input("If you would like to change your password, type 1. Otherwise any other character will lead you back to the login page: ")
                if change_password_question == '1':
                    new_password = "What would you like your new password to be: "
                    self.db.change_password(email, new_password)
                    print("You have successfully changed your password! Please login again with your new password thanks")
                    return 'wrong password'

    def check_password(self, email, password):
        database_password = self.db.get_password(email)
        if password == database_password:
            return True
        else:
            return False
