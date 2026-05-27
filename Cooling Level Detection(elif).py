#In a factory, machines generate heat. The system must activate different cooling levels..
#..depending on temperature.
Temperature = int(input("Enter Temperature : "))

if Temperature >= 80 :
    print("Activate High Cooling Level")
elif Temperature >= 60 and Temperature < 80 :
    print("Activate Medium Cooling Level")
elif Temperature >= 40 and Temperature < 60 :
    print("Activate Low Cooling Level")
else :
    print("Cooling Not Required")    