while True:
    mon = input("Enter a month or type exit to cancel : ")
    month = mon.capitalize()
    if month == "Exit":
        break
    if month == "April" or month == "June" or month == "September" or month == "November" or month == "30":
        print(mon,"has 30 days.")
    elif month == "January" or month == "March" or month == "May" or month == "July" or month == "August" or month == "October" or month == "December" or month == "31":
        print(mon,"has 31 days.")
    else:
        print("Invalid input")
        break
