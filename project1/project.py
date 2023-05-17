info = {}
userInfo = open("Info.txt", "w")
def l1():
    print("\n")

def disOptions():
    print("Menu")
    print("----------------------------------")
    print("""1. Look up an email address
2. Add a new name and email adress
3. Change an existing email address
4. Delete a name and email address
5. Quit the program""")

def option1():
    n = input("Enter a name")
    if(n in info.keys()):
        print("Name:", n)
        print("Email:", info[n])
        l1()
    else:
        print("The specified name was not found")
        l1()

def option2():
    n = input("Enter a name:")
    email = input("Enter email address:")
    if (n in info.keys()):
        print("That name already exists")
        l1()
    else:
        info[n]=email
        print("Name and address have been added")
        l1()
def option3():
    n = input("Enter a name:")
    if(n in info):
        email = input("Enter the new address:")
        info[n]=email
        print("Information updated")
        l1()
    else:
        questions = input("Would you like to add your info?(y/n):")
        if(question == 'y'):
             choice2()
        else:
            print("You cannot update address if you're not in database")
            l1()
def option4():
    n = input("Enter a name:")
    if(n in info):
        del(info[n])
        print("Information deleted")
        l1()
    else:
        print("The specified name was not found")
        l1()
def option5():
    userInfo.write("Name                Adress\n")
    for keys in info:
        key1 = keys
        val = info[key1]
        userInfo.write("{0}           {1:>10}            \n".format(key1, val))
    print("Information saved")

final = False

while(final == False):
    disOptions()
    l1()
    option = input("Enter your choice:")
    option = int(option)

    if(option == 1):
        option1()

    elif(option == 2):
        option2()

    elif(option == 3):
        option3()

    elif(option == 4):
        option4()

    elif(option == 5):
        option5()
        final = True

    else:
        print("Please enter a number 1-5 (options are listed above)")

userInfo.close()






















    

    
