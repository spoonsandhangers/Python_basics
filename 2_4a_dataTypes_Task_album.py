def album():

    try:
        title = input("Enter the title of the album:")
        artist = input("Enter the artist name")
        genre = input("Enter the genre of the album")
        numTracks = int(input("Enter the number of tracks on the album"))
        #anything other than 0 entered here will result in True
        #So the input must first be cast to an int before being cast to bool
        inStock = bool(int(input("Enter 1 or 0, is the album in stock?")))
        price = float(input("Enter the price of the album"))

        #The function round(float, number of decimal places)
        price = round(price,2)
    except ValueError:
        print("The value you have entered is the wrong data type")

    print("Your album choice:",end="\n\t*")
    print(title, artist, genre, numTracks,inStock,price,sep='\n\t*')

album()
