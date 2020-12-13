#import sqlite library
import sqlite3

# re module provides support 
# for regular expressions 
import re 

# this 
with sqlite3.connect("user.db") as db:
    cursor = db.cursor()

    cursor.execute('''CREATE TABLE IF NOT EXISTS user(userID INTEGER PRIMARY KEY, username VARCHAR(20) NOT NULL,
    firstname VARCHAR(20) NOT NULL, lastname VARCHAR(20) NOT NULL, password VARCHAR(20) NOT NULL);''')

    cursor.execute("""INSERT INTO user (username, firsrname,lastname,password)VALUE("test_user", "murtala", "adamu", "password", "email", "course") """) 
    db.commit()

    #Check Database to see if the user exist or not. if user does not exist, user details are save into the database
    
    # def define a function for new user
    def newUser():

        found = 0
        while found == 0:
            username = input ("please enter a username")

        with sqlite3.connect("user.db") as db:
            cursor = db.cursor()
        findUser = ("SELECT * FROM user WHERE username = ?")
        cursor.execute (findUser, [(username)])

        if cursor.fetchall():
            print("that useranme is already exist, please try again!")
        else:
            found = 1
    
        firstName = input("please enter first name:")
        lastName = input("please enter last name:")
        password = input("please enter a Password:")
        password1 = input("please re-enter Password again:")
        email = input("please your email:")

        # Make a regular expression
        # for validating an Email
        regex = '^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$'

        # Define a function for
        # for validating an Email
        def check(email):

            # pass the regualar expression
            # and the string in search() method
            if (re.search(regex, email)):
                print("Valid Email")

            else:
                print("Invalid Email")

        course = input("please your course:")

    
        while password != password1:
            print("Sorry your password do not match, please try again!")
            password = input("please enter a Password:")
            password1 = input("please re-enter Password again:")
        insertDate = '''INSECT INTO user(username, firsrname,lastname,password)VALUE(?,?,?,?)'''
        cursor.execute(insertDate,[(username),(firstName),(lastName),(password), (email),(course)])
        db.commit()

    newUser()

    
cursor.execute("SELECT * FROM user;")
print(cursor.fetchall())