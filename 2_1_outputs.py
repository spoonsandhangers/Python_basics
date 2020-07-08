def basic_outs():
    print("Hello World!") #String output

    #Python adds a line break after each print statement.
    #To prevent this you can add end=''.
    print("all", end ='')
    print("on", end ='')
    print("one", end ='')
    print("line") # I want this one to produce a line break at the end.

    #To add a line break in the middle of a print statement add \n
    print(" on \n seperate \n lines")

    #To add tabs to a line add \t
    print("All \t tabbed \t out")

    #Declare a variable for a String, no need to tell Python that
    #it is a String, unlike other languages.
    aName = "Homer"  # variable declaration
    print(aName)    #use the variable in a print statement.

    #Use the + symbol to concatenate strings together.
    #In python this does not add a space, so you need to add one if needed.
    print("Hello " + aName) # Concatenation

    #You can perform calculations in a print statement
    print(4*2)  # Prints the answer to 4 multiplied by 2

def out_extension():
    # You can tell Python what to seperate strings with.
    print('','User','Marge','documents','letters',sep='/') #to build a file path

    print('harry','Potter','Hogwarts','Gryffindor',sep=',') #creates a comma seperated record.

    print('All','On','Seperate','Lines',sep='\n') #Will each word on a different line.

    print('All','tabbed','out',sep='\t') #adds a tab after every element

    #We can mix these up to create a bulleted list
    print('The houses in Hogwarts are:', end='\n\t* ')
    print('Gryffindor','Hufflepuff','Slytherin','Ravenclaw',sep='\n\t* ')

    #Print f is a function that allows you to format your print statements.
    first_name = "Marty"
    sur_name = "McFly"
    print(f"His first name is {first_name} and his surname is {sur_name}")

    #more advanced use of printf with an array. The <10 means there will be 10characters before the :
    #with left justification
    for article in ["bread", "butter", "tea"]:
        print(f"{article:<10}:")

        
#basic_outs()
out_extension()

