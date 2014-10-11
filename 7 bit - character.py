#oscar stanley
#11/10/2014

option=int(input("Would you like to convert a (1)7 bit binary code to its equivalent character or (2)character to its equivalent 7 bit binary code?"))

print()

if option==1:
    binary_string=input("Please enter a 7 bit binary code:")
    binary2decimal=int(binary_string,2)
    denary=chr(binary2decimal)
    print()
    print("The equivalent character of {0} is {1}.".format(binary_string,denary))

elif option==2:
    character=input("Please enter any character to convert:")
character2integer=ord(character)

print()

print("The equivalent 7 bit binary code for {0} is {1:b}.".format(character,character2integer))
