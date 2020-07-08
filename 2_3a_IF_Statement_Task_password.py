"""
3 solutions to the password task.
password() uses a string flag to show if your username is
correct.
password2() uses a boolean flag to show if your username is
correct.
password3() uses a nested loop.
"""

def password():
    """
    Asks the user for a username and password
    compares these to the stored username and password.
    Displays a message to inform the user if their username or password
    are incorrect and whether they have access.
    Uses a string flag.
    :return: none
    """
    username = "morty"
    password = "letmein"

    name_input = input("Enter your user name: ")
    password_input = input("Enter your password: ")

    flag_name = "correct"

    if name_input == username:
        print("Your user name is correct")
    else:
        print("Your user name is incorrect")
        flag_name = "incorrect"

    if password_input == password and flag_name == "correct":
        print("your password is correct")
        print("Access granted")
    elif flag_name == "incorrect":
        print("Access denied")
    else:
        print("your password is incorrect!")
        print("Access denied")

def password2():
    """
     Asks the user for a username and password
    compares these to the stored username and password.
    Displays a message to inform the user if their username or password
    are incorrect and whether they have access
    uses a Boolean flag
    :return: none
    """
    username = "morty"
    password = "letmein"

    name_input = input("Enter your user name: ")
    password_input = input("Enter your password: ")

    flag_name = True

    if name_input == username:
        print("Your user name is correct")
    else:
        print("Your user name is incorrect")
        flag_name = False

    if password_input == password and flag_name == True:
        print("your password is correct")
        print("Access granted")
    elif flag_name == False:
        print("Access denied")
    else:
        print("your password is incorrect!")
        print("Access denied")

def password3():
    """
     Asks the user for a username and password
    compares these to the stored username and password.
    Displays a message to inform the user if their username or password
    are incorrect and whether they have access
    Uses a nested loop
    :return: none
    """
    username = "morty"
    password = "letmein"

    name_input = input("Enter your user name: ")
    password_input = input("Enter your password: ")

    if name_input == username:
        print("Your user name is correct")
        if password_input == password:
            print("Your password is correct")
            print("Access granted")
        else:
            print("Your password is incorrect")
            print("Access denied")
    else:
        print("Your username is incorrect")
        print("Access denied")


#password()
#password2()
password3()

