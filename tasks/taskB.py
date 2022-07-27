

print(10*'*'+'Application Login'+10*'*')

print("""1. Enter 1 to sign up
2. Enter 2 to log in
3. Enter 3 to log out""")

value = int(input("Choice from available option: "))

users = []
user1 = []
login_users = []
login_data = []
reset_data = []
count = 1
mobile_number = ""
password = ""
password_confirm = ""
DOB = ""
success = False
 
print("Please log in.")
print(10*'*'+'Begin of Login Script'+10*'*')
while count <=3 and not success:
    mobile_number = input("Enter your mobile number e.g. 123456789: ")
    password = input("Enter your password: ")
    user1.append([mobile_number, password])
    for user in range(0, len(users), 1): #Looping throught users(list) 
        if user != user1: #comparing items in the list with user input
            if mobile_number and password: #Mobile number verification
                mobile_number = users[user][0]
                password = login_data[user][1]
                print('You have successfully sign up\nWelcome %s'%(users[user][0]))
                success = True
                print(10*'*'+'End of Application Login script'+10*'*')
            print("1. Enter 1 for Resetting your password\n2. Enter 2 to signout")
if not success:
    print("Incorrect credential try aagin")
    count+=1
if count == 3:
    print("Reached attempt limit")
    print("Reset password ") #add failed attempt password reset script here