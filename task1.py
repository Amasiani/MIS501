#from MIS501 import DOB
#from MIS501 import users
import re
import datetime

mobile_number = eval(input("Try again, Enter Phone in correct format e.g. 01234567890: "))

num = oct(int(input("enter num: ")))

print(num)

dte = input("enter date in mm/dd/yy: ")

dat1 = datetime.datetime.strptime(dte, "%m/%d/%y")
print(dat1.strftime("%m/%d/%y"))
age = datetime.datetime.today().year - dat1.year
print("Age calculated from the year of birth provided as ", dat1.year, " is ", age)

#print(datetime.date.today())

correct =True




tmy = datetime.datetime.today().year #extracting year from datetime module
print(tmy)

vall = '02/03/2020'
print(vall, sep=' ')
print(vall.split('/'))



#print(re.split(r'\s', val))


val = 'alp@123'
match = re.search('^\w.*\d$', val)

if match:
    print('found')
else:
    print('not found')






hello_data = []
login_info =[]
mobile_number = None
age = None
count = 0
success = False

#create account
print(10*'*'+'Begin create account'+10*'*')
#mobile_number = (input("Enter your Phone number: "))
#age = (input("Enter your age: "))
#lines = [mobile_number, age]
#with open("users.txt", "r+") as fline:
    #for line in lines:
        #fline.seek(0, 2)
        #fline.write(line)
        #fline.write('\n')
#fline.close()
print(10*'*'+'End create account'+10*'*')


#login script
print(10*'*'+'Begin account login'+10*'*')
while count <= 3 and not success:
    mobile_number = input("Enter your Phone number: ")
    age = input("Enter your age: ")
    login_info.append([mobile_number, age])
    for line in open('users.txt', 'r').readlines():
        login_info = line.split()
        
        if mobile_number and age:
            mobile_number == login_info[0] and age == login_info[1]
            print("Welcome ", login_info[0])
            success = True
            break

if not success:
    print("incorrect details.")
    count+=1

if count == 3:
    print("Excceded attempts try again.")
print(10*'*'+'End account login'+10*'*')



#working example
#while hello >= 1:
    #age = int(input("Enter your age: "))
    #while age != 18:
        #age = int(eval(input("Try again, Enter your age: ")))
        #if hello == 4:
            #print("Your 'age' still not correct")
        #break
    #DOB = int(input("Enter date of birth e.g. 24: "))
    #while DOB != 24:
        #DOB = int(eval(input("Try again, Enter your DOB: ")))
        #if hello == 3:
            #print("Reset your details")
        #break
    #hello_data.append([age, DOB])
    #print(hello_data)
    #if hello == 3:
        #break
    #hello-=1
    
    
#hello_data.append([age, DOB])
#print(hello_data)
'''else:
    #print(hello_data.append([age, DOB]))
    print("continue")'''




'''while True:
    try:
        DOB = input("Enter your age in this format e.g. MM/DD/YYYY: ")
    except ValueError:
        print("Unknow input.")
    else:
        print("Correct")
        break
if DOB >= 18:
    print("great")
else:
    print("oooon")






while True:
    data = int(input("Enter your mobile number: "))
    val = f'{data:011}'
    print(val)
    if val == len('hellooooooooo'):
        print("Bad format")
    else:
        break

''list1 = [1, 2, 4, 5, 7]
col = int(input("Enter num: "))
for num in list1:
    if num == col:
        print(num)
    print("not found")

name = input("Enter your name: ")
email = input("enter your email: ")

list1.append(name)
list1.append(email)
print(list1)


"""i =1

while i < 100:
    if i%3 != 0:
        print(i)
    i+=1"""

guess = 0
while (guess != 18):
    guess = eval(input("Enter a number: "))
print("That's right")


countdown = int(input("Enter a value to count down: "))
while countdown >= 0:
    print(countdown)
    countdown -=1
     
age = int(input("Enter your age: "))

if age <= 1:
    print("Oh boy you be pikin (baby)")
elif age <= 2:
    print("Little above pikin, that's an infant")
elif age <= 3:
    print("You are a toddler")
elif age <= 12:
    print("you are a child")
elif age <= 18:
    print("you are a teenager")
else:
    print("Find you are an elder")

num = int(input("Enter a number: "))

if num > 10:
    print(num, " is greater than 10")
    print(num*num*num)
elif num < 10:
    print(num, " is less than 10")
    print(num*num)

num = int(input("Enter a number: "))

if num < 100:
    print(num, " is less than 100")
    print(num, " is halved", num/2)

num = int(input("Enter a number: "))

if num > 10:
    print(num, " is greater than 10")
else:
    print(num, " is less than 10")

print("""1. Enter 1 to sign up
2. Enter 2 to log in
3. Enter 3 to log out""")

def sign_up(name="", ):
    pass

def log_in():
    pass

data = int(input("Enter an option: "))

if data == 1:
    sign_up()
elif data == 2:
    log_in()
elif data == 3:
    print("Logged out")
else: 
    print("Waiting for your input")
    



def switch(name):
    if name != 'emeka':
        value = input("Enter 'Emeka' to continue: ").lower()
        switch(value)   #recursive function
    else:
        print("Welcome")

"""while value2 == 1:
    print("Please sign in")
    break"""

index = int(input("enter an index: "))
listA = [12, 23, 10, 9, 8]
if (index >= 0 and index < 4):
    update = int(input("enter a value: "))
    listA.insert(index, update)
    print(listA)
else:
    print("invalued index")
'''
