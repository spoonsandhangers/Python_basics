"""
A collection of string functions that return true or false.
These can be used as conditions in a selection statement.(IF)
"""
def stringCases():
   user_name = input("Enter your user name: ") # ask for users name.
   comp_name = "Bobby"

    # true if string contains the substring
   if "ob" in user_name:
       print("Correct in")
   else:
       print("nope in")

    # true if string does not contain the substring
   if "ob" not in user_name:
       print("Correct, the substring is not in user_name")
   else:
       print("nope, the substring is in user_name")

    #true if the variable contains a matching string. Case sensitive.

   if user_name == "admin":
       print("Welcome back admin")
   elif user_name == "Bobby":   #elif used to test more than one condition. In this structure only one is True.
       print("Correct user name")
   else:
       print("Access denied")

    # true if the user_name starts with the substring
   if user_name.startswith("Bob"):
       print("Correct, it starts with the substring")
   else:
       print("nope, it doesn't start with the substring")

  # true if the user_name ends with the substring
   if user_name.endswith("by"):
       print("Correct, it ends with the substring")
   else:
       print("nope it doesn't end with the substring")

    # true if the user_name is all whitespace and is at least one character.
   if user_name.isspace():
       print("Correct, this is just space")
   else:
       print("nope it's not space")

    # true if the user_name is uppercase
   if user_name.isupper():
       print("Correct, this is uppercase")
   else:
       print("Nope, this is not uppercase")

    # true if the user_name is lowercase
   if user_name.islower():
       print("Correct, this is lowercase")
   else:
       print("nope, this is not lowercase")

     # true if the user_name is numeric
   if user_name.isnumeric():
       print("Correct, this is numeric")
   else:
       print("nope, this is not numeric")

    #All conditional statements must equate to true or false.
    #A conditional statement always follows an IF or ELIF.
    # Where the word IF is used, SELECTION is being used.
    # In Python whitespace matters!  All code that is inside the
   # IF statement must be indented using the tab key.
   # Pay attention to code indentation!



stringCases()
