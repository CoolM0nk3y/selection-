#oscar stanley
#7-10-14
#the biggest out of three int
number1 = int(input("What is your first number: "))
number2 = int(input("What is your second number: "))
number3 = int(input("What is your third number: "))

if number1 == number2 == number3:
    print("All your numbers are of the same number")
elif number1 > number2 and number1 > number3:
    print("The first number you enterd was the biggest")
elif number2 > number1 and number2 > number3:
    print("The second number you enterd was the biggest")
elif number3 > number2 and number3 > number1:
    print("The third  number you enterd was the biggest")
