import math

def swimmingPool():
    """
    Asks the user for length, width and depth of a swimming pool
    Prints out the perimeter and volume of the pool.
    :return: none
    """
    #convert the user input to a float value
    length = float(input("Enter the length of the pool in metres: "))
    width = float(input("Enter the width of the pool in metres: "))
    depth = float(input("Enter the depth of the pool in metres: "))

    #calculate the perimeter of the pool and print it out
    perimeter = (length * 2) + (width * 2)
    print("The perimeter of the pool is:", round(perimeter,2),"meters")

    #calculate the volume of the pool and print it out
    volume = (length * width) * depth
    print("The volume of the pool is:", round(volume,2),"meters squared")

def roundpool():
    """
    This function asks the input to input the diameter of a round pool
    and calculates and prints out the circumference and area of the pool.
    :return: none
    """
    #user input is converted to a float before being assigned to the variable
    dia_pool = float(input("Enter the diameter of the pool: "))

    #calculate the radius and cicumference of the pool
    radius_pool = dia_pool/2
    circumference_pool = 2 * math.pi * radius_pool
    print("Pool circumference is:",round(circumference_pool,2), "metres")

    #calculate the area of the pool
    area_pool = math.pi * radius_pool * radius_pool
    print("Pool area is: ", round(area_pool,2), "metres")

    print("The radius of the pool MOD 1 is:",radius_pool%1)

#swimmingPool()
roundpool()
