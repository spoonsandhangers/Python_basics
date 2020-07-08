def conversation():
    """
    Asks the user to input their name and hair colour
    gives the user a nickname by concatenating the first 3 letters
    of their name with 'gsy'
    :return:
    """
    #store the name that the user inputs in the variable user_name
    user_name = input("What is your name?: ")

    #output hello and their name using the variable user_name
    print("Hello", user_name)

    #Ask the user what colour their hair is mentioning their name.
    user_hair = input("What colour is your hair "+ user_name+ "? ")

    #Give the user a nickname using the first three letters of their name followed by
    #gsy.
    print("Your nickname is", user_name[0:2]+"gsy")

def mixedRainbow():
    """
    Asks the user to input the colours of the rainbow one at a time.
    makes every other one uppercase, changes all the letter e's with a's
    print them out.
    :return:
    """

    #Ask a user to input the colours of the rainbow one at a time.
    #change them to lower then upper alternately.
    rainbow1 = input("Enter the 1st colour of the rainbow: ").lower()
    rainbow2 = input("Enter the 2nd colour of the rainbow: ").upper()
    rainbow3 = input("Enter the 3rd colour of the rainbow: ").lower()
    rainbow4 = input("Enter the 4th colour of the rainbow: ").upper()
    rainbow5 = input("Enter the 5th colour of the rainbow: ").lower()
    rainbow6 = input("Enter the 6th colour of the rainbow: ").upper()
    rainbow7 = input("Enter the 7th colour of the rainbow: ").lower()

    #alternative method
    # rainbow1.lower()
    # rainbow2.upper()
    # rainbow3.lower()
    # rainbow4.upper()
    # rainbow5.lower()
    # rainbow6.upper()
    # rainbow7.lower()

    #replace the 'e' with an 'a' in all colours
    rainbow1 = rainbow1.replace('e','a')
    rainbow2 = rainbow2.replace('E','A')
    rainbow3 = rainbow3.replace('e','a')
    rainbow4 = rainbow4.replace('E','A')
    rainbow5 = rainbow5.replace('e','a')
    rainbow6 = rainbow6.replace('E','A')
    rainbow7 = rainbow7.replace('e','a')

    #print the colours out with their new weird names.
    print("The colours of the rainbow might be: ")
    print(rainbow1)
    print(rainbow2)
    print(rainbow3)
    print(rainbow4)
    print(rainbow5)
    print(rainbow6)
    print(rainbow7)





#conversation()
mixedRainbow()
