import re
import datetime

print("""1. Enter 1 to sign up
2. Enter 2 to log in
3. Enter 3 to log out""")

value = int(input("Choice from available option: "))

users = []
login = []
count = 1
mobile_number = ""
password = ""
password_confirm = ""
DOB = ""
success = False



if value == 1:
    num_users  = int(input("Enter number of users: ")) #Multiple users option
    print("Please sign up")
    for user in range(0, num_users, 1): #looping throught num_users
        username = input("Enter your name:  ")
        mobile_number = input("Enter your mobile number e.g. 01234567890: ")
        valid_mobile_number = re.compile(r"(?:\d)?\d{11}")
        while valid_mobile_number.search(mobile_number) is None:
            mobile_number = eval(input("Try again, Enter your mobile number in the correct format e.g 01111111111: "))
        password = input("Enter password in the format xyz@123: ")
        valid_password = re.compile(r"([A-Za-z0-9]+[.@#\$])*[0-9]") #Reference from Python3.10 Doc Chapter 6(6.2.5). Regular expression (Compile user input with re module()).
        while valid_password.search(password) is None:
            password = eval(input("Try again, Enter password in the correct format e.g. axy@234: "))
        password_confirm = input("Enter password confirmation: ")
        #valid_password = re.compile(r"([A-Za-z0-9]+[.@#\$])*[0-9]")
        while valid_password.search(password_confirm) is None:
            if password_confirm != password:
                password_confirm = eval(input("Password confirmation not matching password, try again: "))
        DOB = input("Enter date of birth e.g MM/DD/YYYY: ")
        valid_DOB = re.compile(r"^\d{1,2}/\d{1,2}/\d{4}$") #Reference from Python3.10 Doc Chapter 6(6.2.5). Regular expression (Compile user input with re module()).
        while valid_DOB.search(DOB) is None:
            DOB = eval(input("Try again, Enter your DOB in the correct format e.g. MM/DD/YYYY: "))
        year_BOD = datetime.datetime.strptime(DOB, "%m/%d/%Y") #converting string type date to datetime object. Reference from python3.10 Doc Chapter 8, Datetime string converted to datetime
        date_str = year_BOD.strftime('%m/%d/%y') # formating datetime object to string format.
        age = datetime.datetime.today().year - year_BOD.year #Extacting year from datetime object and calculating the age from user input by subtracted from current year
        if age <= 18: #Enforcing age limit
            print("Sorry you cannot use this application age limit is 18years.")
        else:
            users.append([username, mobile_number, password, password_confirm, DOB, age])
        #print(users) #list of registered users 
        users_copy = users[:] # deep copy of users list to make it available to the login script
        print("Your have successfully signed up.")
        print("""
            1. Enter 1 to sign up
            2. Enter 2 to log in
            3. Enter 3 to log out
            """)
    print(10*'*'+'Beginning of Login Script'+10*'*') #Beginning of Application Login script.
    options = int(input("To login select 2 or 3 to exit the application: ")) #setting options
    if options == 2:
        print("Enter your Phone and Password to Login.")
        while count <=3 and not success: #initializing Login attempt counter
            #print(login_data) #Login users deep copy
            mobile_number = input("Enter your mobile number e.g. 09876543210: ")
            password = input("Enter your password e.g xyz@123: ")
            #login.append([mobile_number, password]) #login user details
            print(users_copy)
            for user in users: #Looping through users(list) and creating a sub_list (user list) from users list
                if mobile_number and password in user: #checking mobile_number and password in user list
                    if mobile_number == user[1] and password == user[2]: #comparing items in user list with user input
                        #print(user) #logged in user
                        print('You have successfully logged in\nWelcome %s'%(user[0].capitalize()))
                        success = True
                        print(10*'*'+'End of Application Login script'+10*'*') #End of Application Login script.
                        print("1. Enter 1 for Resetting your password\n2. Enter 2 to signout")
                        print(10*'*'+'Beginning of menu Password Reset'+10*'*') #Password Reset from menu 
                        select_value = int(input("Select from the available option 1 or 2: "))
                        if select_value == 1:
                            print("Reset you Password from Menu.")
                            print(users_copy) #Registered users deep copy
                            mobile_number = input("Please enter your username (Mobile number) e.g. 01234567890:  ")
                            if mobile_number != user[1]:
                                print("Entered mobile number does not exit!!!")
                                mobile_number = eval(input("Enter your mobile number in correct format e.g 01234567890: "))
                            old_password = input("Enter your password: ")
                            if old_password != user[2]:
                                print(user[2])
                                old_password = eval(input("Entered password not matching!!!"))
                            new_password = input("Please upate your password: ")
                            user[2] = new_password #setting new password to old password in the users list
                            print("Your password has been updated successfully.", user[2])
                            continue
                        else:
                            print("You logged out of the application.")
                            break
        if not success:
            print("Incorrect credential try again")
            count+=1
        if count == 3:
            print("Reached attempt limit")
            print(10*'*'+'Beginning of failed attempt password reset'+10*'*') #Failed attempt password Reset
            for user in users:
                mobile_number = input("Please enter your username (Mobile number):  ")
                valid_mobile_number = re.compile(r"(?:\d)?\d{11}")
                if valid_mobile_number.search(mobile_number) is None:
                    mobile_number = eval(input("Mobile number entered does not exist e.g. 01234567890: "))
                DOB = input("Enter date of birth e.g MM/DD/YYYY: ")
                valid_DOB = re.compile(r"^\d{1,2}/\d{1,2}/\d{4}$") #Reference from Python3.10 Doc Chapter 6(6.2.5). Regular expression (Compile user input with re module())
                if valid_DOB.search(DOB) is None:
                    DOB = eval(input("Try again, Enter your Date Of Birth in correct format e.g. MM/DD/YYYY: "))
                if mobile_number and DOB in user:
                    if mobile_number == user[1] and DOB == user[4]:
                        new_password = input("Please upate your password: ")
                        user[2] = new_password
                        print("Your password has been reset successfully.", user)
                    else:
                        print("No match found")
                        break      
                    print(10*'*'+'End of failed attempt password reset'+10*'*')
                    print('''1. Enter 1 to sign up
                        2. Enter 2 to log in
                        3. Enter 3 to log out
                        ''')  
            #print(10*'*'+'End of failed login attempt'+10*'*') #End of failed login attempt
    else:
        print("You have logged out of the application, thanks")
elif value ==2:
    print("Exit the application and select 2 to Signup")
else:
    print("You have logged out of the application")
