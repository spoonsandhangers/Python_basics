def helloWorld():
    """
    Examples of ways to outpu information to the console.
    :return: none
    """
    print("Hello World")

    #Any time you perform division in Python the
    #result is a float.
    print(9/3)

    #modulo operator returns the remainder of the division.
    print(9%3)

    #floor division returns just the integer part of the division
    #with no decimal part.
    print(9//2)

    # No spaces are added when the concatenation + operator is used.
    print("Bon Jovi: " + "Jon " + "Richie " + "Alec " + "Tico ")

    #One line comments use the hash key.

def advancedOutput():
    """
    More advanced examples of outputs
    :return: none
    """
    my_name = "Eleven"

    print("Hello " + my_name)

    print(0XA5)    #prefix the hex number with 0X or 0x

    print(0B1100011)   #prefix the binary number with 0B or 0b

    """
    Python multline comments have 3 sets of speech marks at the
    beginning and the end.  These are used for documentation.
    """

helloWorld()
#advancedOutput()
