from database import DatabaseManager
from users import User

db = DatabaseManager()
db.create_tables()

user = User()

print('Hello and welcome to Programming Buddies!')
not_logged_in = True
while not_logged_in:
    login = input("""Would you like to
        [1] Login
        [2] Create an account
    """)
    if login == '1':
        login_pass = user.login()
        if login_pass:
            print(f"Hi {user.name}, you have successfully logged in. Welcome!")
            not_logged_in = False
        elif login_pass == 'wrong password':
            print("Please relogin either with your new password or with your current password")
        else:
            print("Your email is not in our system. Please create an account instead")

    elif login == '2':
        not_logged_in = user.create_account()

    else:
        print("Wrong input. Please only enter in 1 or 2")



