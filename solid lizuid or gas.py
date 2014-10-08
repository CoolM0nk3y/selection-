#oscar stanley
#7-10-14
# solid liquid or gas
temp = int(input("Please enter th temperature(°C) of the water: "))
if temp <= 0:
    print("Your water ia ice which is a solid")
elif temp > 0 and temp < 100:
    print(" Your water is in a liquid state")
else:
    print("Your water is a gas it has evaporated")
