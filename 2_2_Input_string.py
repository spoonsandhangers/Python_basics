def inputExamples():
    """
    Example of user input
    :return: string user_name
    """

    user_name = input("Enter your name in upper case: ") #Input is always stored as a String.

    #my_name = input() # Prompt is optional.

    return user_name

def stringExamples():
    """
    Examples of String handling in Python
    :return: none
    """

    the_name = "ERIC IDLE"

    print("Lower case: ", the_name.lower())
    print("Upper case: ", the_name.upper())
    print("Prints the 3rd character: ", the_name[2])
    print("Prints the length of the string: ",len(the_name))
    print("Prints a substring: ", the_name[0:3]) #Prints the first 2 letters of the string.
    print("Prints the index of the first occurrence of the character: ", the_name.index('I'))
    print("Replaces one string with another: ", the_name.replace("ERIC","you are"))

    another_name = "         Graham Chapman      "
    print("name before the whitespace is removed: ", another_name)
    print("Strips leading and trailing whitespace: ", another_name.strip())

stringExamples()
