#5. Design an irrigation system that checks soil moisture and, if the level is low, evaluates
#weather conditions (rain/no rain) before deciding to start or stop watering.
Soil_Moisture = int(input("Enter Soil Moisture Level : "))
if Soil_Moisture < 30 :
    Rain_Condition = input("Is it raining? (yes/no) : ").lower()
    if Rain_Condition == "yes" :
        print("Stop Watering")
    else :
        print("Start Watering")
else :
    print("Soil Moisture is sufficient, no need to water")