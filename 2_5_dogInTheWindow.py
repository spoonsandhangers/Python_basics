"""
2 solutions for the dog in the window challenge.
dog2() puts all the code in the try/except block
dog() uses a different variable so it still creates an output but the output is
not correct e.g. whatever the user entered in price will be shown as the price.
The value error is shown so the user knows what has happened.
I prefer dog2()
"""
def dog():

    dog_name = input("Enter the dog's name: ")
    coat_colour = input("Enter the dogs coat colour: ")
    eye_colour = input("Enter the dogs eye colour: ")
    length_cm = input("Enter the dog's length in cm: ")
    weight_kg = input("Enter the dog's weight in Kg: ")
    price = input("Enter the dog's price in pence: ")

    try:
        price = float(price)
        price = str(round(price/100,2))

    except ValueError:
        print("The price you have entered is not a number")


    price = "price: £" + price
    dog_name = "Dog name: " + dog_name
    coat_colour = "Coat colour: " + coat_colour
    eye_colour = "Eye colour: " + eye_colour
    length_cm = "Length: "+ length_cm + "cm"
    weight_kg = "weight: " + weight_kg + "kg"

    print("Dog details: ", end="\n\t*")
    print(dog_name,coat_colour,eye_colour,length_cm,weight_kg,price, sep="\n\t*")

def dog2():
    dog_name = input("Enter the dog's name: ")
    coat_colour = input("Enter the dogs coat colour: ")
    eye_colour = input("Enter the dogs eye colour: ")
    length_cm = input("Enter the dog's length in cm: ")
    weight_kg = input("Enter the dog's weight in Kg: ")
    price_pence = input("Enter the dog's price in pence: ")

    try:
        #Converts the price of the dog to a float if it is a number
        #otherwise an exception is thrown and caught
        #rounds the float to 2 decimal places and coverts back to a string
        price_pounds = float(price_pence)
        price = str(round(price_pounds/100,2))

        #sets up the strings to be printed
        price = "price: £" + price
        dog_name = "Dog name: " + dog_name
        coat_colour = "Coat colour: " + coat_colour
        eye_colour = "Eye colour: " + eye_colour
        length_cm = "Length: "+ length_cm + "cm"
        weight_kg = "weight: " + weight_kg + "kg"

        #prints out the dogs details in a bulletted list.
        print("Dog details: ", end="\n\t*")
        print(dog_name,coat_colour,eye_colour,length_cm,weight_kg,price, sep="\n\t*")

    except ValueError:
        #if a ValueError is thrown this will print out a message here.
        print("The price you have entered is not a number")



#dog()
dog2()
