#1. Design a robot that first checks for the presence of an obstacle and, if detected,
#decides the direction (left or right) to avoid it; otherwise, the robot should move
#forward.(NESTED IF ELSE STATEMENT)
Obstacle_Detected = input("Is there an obstacle detected? (yes/no) : ").lower()
if Obstacle_Detected == "yes" :
    Left_Sensor = int(input("Enter Left Sensor Value : "))
    Right_Sensor = int(input("Enter Right Sensor Value : "))
    if Left_Sensor > Right_Sensor :
        print("Turn Left")
    elif Left_Sensor < Right_Sensor :
        print("Turn Right")
    else :
        print("Move Forward")

