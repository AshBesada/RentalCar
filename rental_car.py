import sys


# Asks the user to input the rental code B, D, or W.
# Variabl used to determine the rental type| string type.
rentalCode = input("(B)udget, (D)aily, or (W)eekly rental?\n")

# For the code entered, will ask the user to input the rental period.
# IF statement used to determine rental time and assign the correct
# rate for each category.
if rentalCode == "W":
    rentalPeriod = input("Number of weeks rented:\n")
elif rentalCode == "B":
    rentalPeriod = input("Number of Days Rented:\n")
elif rentalCode == "D":
    rentalPeriod = input("Number of Days Rented:\n")

# Assign the rental price variables | float type
budgetCharge = 40.00
dailyCharge = 60.00
weeklyCharge = 190.00

# Logic branch that runs depending on rental type
if rentalCode == "B":
    baseCharge = int(rentalPeriod) * int(budgetCharge)
elif rentalCode == "D":
    baseCharge = int(rentalPeriod) * int(dailyCharge)
elif rentalCode == "W":
    baseCharge = int(rentalPeriod) * int(weeklyCharge)

# Prompt the user to input the starting and ending mileage
# and assigns them to the variable odoStart and odoEnd.
odoStart = input("Starting odometer reading:\n")
odoEnd = input("Ending odometer reading:\n")

# calculating miles driven and assign it to the variable totalMiles.
totalMiles = int(odoEnd) - int(odoStart)

# Claculating mile charge for budget category B.
# Logic branch that runs depending on rental type.
if rentalCode == "B":
    mileCharge = float(totalMiles) * 0.25

# Claculating mile charge for daily category D.
# Logic branch that runs depending on rental type.
elif rentalCode == "D":
    averageDayMiles = float(totalMiles)/float(rentalPeriod)
    if float(averageDayMiles) <= 100:
        extraMiles = 0
    else:  # This cod only run if miles driven were over 100 miles per day
        extraMiles = float(averageDayMiles) - 100
    mileCharge = (.25 * float(extraMiles))  
    #mileCharge *=  float(rentalPeriod) #Re-assign the variable with new value when miles change.

# Claculating mile charge for weekley category W.
# Logic branch that runs depending on rental type.
elif rentalCode == "W":
    averageWeekMiles = float(totalMiles) / float(rentalPeriod)
    if averageWeekMiles <= 900:
        mileCharge = 0
    else:  # For miles driven over 900 a week, $100 fee is added.
        mileCharge = 100 * float(rentalPeriod)

# Calculating base charge + mile charge and assigns result to the variable amtDue.
amtDue = float(baseCharge) + float(mileCharge)

# Display result to the customer.
print("Rental Summary")
print("Rental Code:       " + str(rentalCode))
print("Rental Period:         " + str(rentalPeriod))
print("Starting Odometer: " + str(odoStart))
print("Ending Odometer:   " + str(odoEnd))
print("Miles Driven:      " + str(totalMiles))
print("Amount Due:        " + "$" + str(amtDue) + '0')

# Pause program on screen until user hit the enter key.
input("Press \"Enter\" to close")