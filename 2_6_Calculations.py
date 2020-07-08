import math

def calculateInPython():
    """
    Demonstrates basic calculations in Python and prints out the results
    :return: none
    """
    print("Data types used for calculations are int and float")
    print("variables do not need to be declared before use")
    print("Add = +")
    print("subtract = -")
    print("multiply = *")
    print("divide = /")
    #remainder of a division
    print("modulus = %")
    #The integer part of division, no decimal part even if there is a remainder.
    print("floor or integer division = //")

    int_1 = 24
    int_2 = 12

    print("int 1 =", int_1)
    print("int_2 =", int_2)

    print("int_1 + int_2 =", int_1 + int_2) #adds the 2 integers
    print("int_1 - int_2 =", int_1 - int_2) #subtracts 2 integers
    print("int_1 x int_2 =", int_1 * int_2) #multiplies 2 integers
    print("int_1 / int_2 =", int_1 / int_2) #divides 2 integers
    print("int_1 % int_2 =", int_1 % int_2) #remainder of the division
    print("int_1 // int_2 =", int_1 // int_2) #integer part of the division

    print("Any time you perform division in Python the result")
    print("is a float.  Even if there is no remainder")
    print("This is why the result of 24 divided by 12 is 2.0 not 2")
    print("int_1 / int_2 =", int_1 / int_2) #divides 2 integers

    print("Variables are often used to count up or down")
    print("In computer science we call this increment and decrement")

    count = 0


    print("The variable count is initialised with the value 0")
    print("count = 0")
    print("To increment the varaible count we can:")
    print("count = count + 1")
    print("count += count")
    count += 1
    print("Count now equals:", count)
    print("")
    print("To round a float to a certain number of decimal places")
    print("Use the round() function")
    print("round(float,number of places)")
    my_float = 7.34186903
    print("A float variable equals:",my_float)
    print("using round(my_float,2) rounds it to 2 decimal places:", round(my_float,2))
    print("")


def usingMathLibrary():
    """
    Demonstrates how to import the math library and how to use pi
    :return: none
    """
    print("To use PI in your code, you must import the math library")
    print("At the very top of your code on line one insert the following")
    print("Import statement: import math")
    print("You can now use PI in calculations by typing math.pi")
    print("This is the value of PI rounded to 4 decimal places")
    print("By typing round(math.pi,4):",round(math.pi,4))


#calculateInPython()
usingMathLibrary()
