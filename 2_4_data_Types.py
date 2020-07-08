def dataTypeExamples():
    my_string = '"Any mix of letters, numbers 2345 or symbols surrounded by speech marks"'
    my_int = 23
    my_float = 22.4234562
    my_boolean = True

    print("This is a string:", my_string)
    print("This is an int:", my_int, "a whole number")
    print("This is a float:", my_float, "A number with a decimal part")
    print("This is a boolean value:", my_boolean, ",this can be True or False only")

    print("Any time you perform division in Python the result is a float")
    print("Even if you divide two integers and there is no remainder")
    print("For example 10 divided by 2 =", 10/2)
    print("")
    print("A float can be rounded to a certain number of decimal places")
    print("For example when dealing with money")
    print("The float 22.4234562 rounded to 2 decimal places is:")
    print("\t*",round(my_float,2))

    print("In python variables do not have to be declared as a specific type")
    print("They can also change type by being assigned to another value")

    my_int = '"This is a string"'
    print("my_int now has a string assigned to it:", my_int)
    print("")
    my_string = 4321
    print("my_string now has an int asigned to it:", my_string)

def dataTypeCasts():
    print("When a user inputs information, it is always assigned as a string")
    print("It is even a string if the user inputs a numerical value")
    print("If you want to use the user input in a calculation you have to first")
    print("Change the data type to an int or a float")
    print("This is done using a cast either: int() or float()")

    user_age = input("what year were you born?")
    current_year = input("What year is it now?")
    year = int(current_year)
    age = int(user_age)
    print("")
    print("Your age is:", year-age)
    print("")
    print("Both these values were cast to an int before the calculation was performed")
    print("using int(value/variable here)")
    print("")
    print("You can also cast to other data types")
    print("using str(), float(), bool()")
    print("bool() will return True for anything other than "" or 0")

def castExceptions():
    print("if you try to cast a value to an int or a float")
    print("but it is not a numerical value")
    print("A ValueError exception will be thrown")
    print("You can use a try catch block to catch any exception thrown and report the error")

    try:
        user_age = int(input("Enter your age:"))
        print("Your age is:", user_age)
    except ValueError:
        print("A value error has occurred")
        print("The value you entered was not a number")





dataTypeExamples()
#dataTypeCasts()
#castExceptions()
