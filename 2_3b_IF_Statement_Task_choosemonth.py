def chooseMonth():
    current_month = input("Enter the current month as a number: ")
    year = int(input("What year is it?"))

    #This code determines whether it is a leap year and could go
    #in the february elif block instead of having a whole block here.
    if year%4 == 0 and current_month == '2':
        print("It's a leap year!")
        days = 29
    elif current_month == '2':
        days = 28


    if current_month == "1":
        print("The current month is: January")
        month_name = "january"
        season = "Winter"
        days = 31
    elif current_month == "2":
        print("The current month is: February")
        month_name = "february"
        season = "Winter"

    elif current_month == "3":
        print("The current month is: March")
        month_name = "march"
        season = "Spring"
        days = 31
    elif current_month == "4":
        print("The current month is: April")
        month_name = "april"
        season = "Spring"
        days = 30
    elif current_month == "5":
        print("The current month is: May")
        month_name = "may"
        season = "Spring"
        days = 31
    elif current_month == "6":
        print("The current month is: June")
        month_name = "june"
        season = "Summer"
        days = 30
    elif current_month == "7":
        print("The current month is: July")
        month_name = "july"
        season = "Summer"
        days = 31
    elif current_month == "8":
        print("The current month is: August")
        month_name = "august"
        season = "Summer"
        days = 31
    elif current_month == "9":
        print("The current month is: September")
        month_name = "september"
        season = "Autumn"
        days = 30
    elif current_month == "10":
        print("The current month is: October")
        month_name = "october"
        season = "Autumn"
        days = 31
    elif current_month == "11":
        print("The current month is: November")
        month_name = "november"
        season = "Autumn"
        days = 30
    else:
        print("The current month is: December")
        month_name = "december"
        season = "Winter"
        days = 31

    if 'e' in month_name:
        print(month_name, "contains an e")
    else:
        print(month_name, "does not contain an e")

    print(month_name, "has", days, "days")



chooseMonth()


