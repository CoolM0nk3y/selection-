#oscar stanley
#7-10-14
# gross pay
pay = int(input("How much do you get payed per hour? £ "))
hours = int(input("How many hours do you worked this week: "))
if hours >= 40:
    gross = pay * hours
    gross1 = gross * 1.5
    print("The amout of money you have made this week is £{0}".format(gross1))

else:
    gross = pay * hours
    print("The amout of money you have made this week is £{0}".format(gross))

