#A delivery robot decides whether to continue delivery, return to base, or shut down..
#..based on battery level.
Battery_Level = int(input("Enter Battery Level : "))

if Battery_Level >= 80 :
    print("Continue Delivery")

elif Battery_Level >= 30 and Battery_Level < 80 :
    print("Return to Base") 
elif Battery_Level >= 10 and Battery_Level < 30 :
    print("Shut Down Soon Return to Base")
else :
    print("Shut Down Immediately")