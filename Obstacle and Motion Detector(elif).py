#A robot is moving in a corridor. Based on the distance from obstacles, it must ..
#...decidewhether to stop, slow down, turn, or move forward.

Distance_from_Obstacle = int(input("Enter Distance from Obstacle : "))

if Distance_from_Obstacle <= 10 :
    print("Stop")
elif Distance_from_Obstacle > 10 and Distance_from_Obstacle <= 30 :
    print("Slow Down")
elif Distance_from_Obstacle > 30 and Distance_from_Obstacle <= 50 :
    print("Turn")
else :
    print("Move Forward")
