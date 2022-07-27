

print(10*'*'+'Password Reset'+10*'*')


print("""1. Enter 1 for Resetting Password.
    2. Enter 2 for Signout.
    """)

value = int(input("Choice from available option: "))

users = []
user1 = []
login_users = []
login_data = []
reset_data = []
count = 1
mobile_number = None
password = None
password_confirm = None
DOB = None
success = False

value = int(input("Select from the available option 1 or 2: "))
print(10*'*'+'Begin of menu password reset'+10*'*')
if (value == 1): #password reset from menu
    mobile_number = input("Please enter your username (Mobile number):  ")
    while (mobile_number != users[user][0]):
        #print(users[user][1])
        mobile_number = int(eval(input("Mobile number entered does not exist e.g. 123456789: ")))
    old_password = input("Enter your password: ")
    while (old_password != users[user][2]):
        #print(users[user][2])
        old_password = eval(input("Enter your old password correctly: "))
    new_password = input("Please upate your password: ")
    users[user][2] = new_password 
    print(10*'*'+'End of menu password reset'+10*'*')
    print("Your password has been reset successfully.")
    print('''Enter 1 to for Resetting Password: 
        Enter 2 for Signout''')
print(10*'*'+'Begin of failed attempt password reset'+10*'*')
mobile_number = input("Please enter your username (Mobile number):  ") #Failed attempt password Reset
while (mobile_number != users[user][0]):
    #print(users[user][1])
    mobile_number = int(eval(input("Mobile number entered does not exist e.g. 123456789: ")))
DOB = input("Please enter your DOB: ")
while (DOB != users[user][4]):
    #print(users[user][4])
    DOB = eval(input("Enter DOB in this format e.g. 24: "))
old_password = input("Enter your password: ")
while (old_password != users[user][2]):
    #print(users[user][2])
    old_password = eval(input("Enter your old password correctly: "))
new_password = input("Please upate your password: ")
users[user][2] = new_password
print(10*'*'+'End of failed attempt password reset'+10*'*')
print("Your password has been reset successfully.")
print("""
    1. Enter 1 to sign up
    2. Enter 2 to log in
    3. Enter 3 to log out
    """)