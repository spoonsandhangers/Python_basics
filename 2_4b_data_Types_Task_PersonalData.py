def personalData():
    """
    Asks the user for their name and age.
    Uses a try except block to cast their age to an int
    prints out their name ad age.
    :return:
    """
    user_name = input("Enter your name: ")
    user_age = input("Enter your age")

    #use a try except block when casting to an int.
    try:
        age = int(user_age)
        print("Hello", user_name, "you are", age, "years old.")
    except ValueError:  #error returned if the variable cannot be cast as it is not a number
        print("The age you have entered is not a number")


personalData()
