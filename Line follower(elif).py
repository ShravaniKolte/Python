#A robot follows a line using sensors. Based on sensor input, it adjusts its direction.

Left_Sensor = int(input("Enter Left Sensor Value : "))
Right_Sensor = int(input("Enter Right Sensor Value : "))
if Left_Sensor > Right_Sensor :
    print("Turn Left")
elif Left_Sensor < Right_Sensor :
    print("Turn Right")
else :
    print("Move Forward")
    