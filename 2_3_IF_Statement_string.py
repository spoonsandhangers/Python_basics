def stringCases():
   user_name = input("Enter your user name: ") # ask for users name.
   comp_name = "bobby"

    # true if string contains the substring
   if "ob" in user_name:
       print("Correct in")
   else:
       print("nope in")

    # true if string does not contain the substring
   if "ob" not in user_name:
       print("Correct not in")
   else:
       print("nope not in")

    #true if the variable contains a matching string.
   if user_name == "Bobby":
       print("Correct user name")
   else:
       print("Access denied")

    # true if the user_name starts with the substring
   if user_name.startswith("Bob"):
       print("Correct, it starts with the substring")
   else:
       print("nope it doesn't start with the substring")

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
    #A conditional statement always follows an IF.
   # Where the word IF is SELECTION is being used.



stringCases()
