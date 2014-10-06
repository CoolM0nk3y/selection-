#oscar stanley
#5-10-14
#are you old enough to drive

age = int(input("What is your age: "))


if age >= 17 :
    print("You are old enough to drive legally")

elif age < 17 :
    ageleft =  17-age 
    print("You are to young to drive. You have {0} years to wait.".format(ageleft))
