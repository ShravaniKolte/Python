#3. Design a robot that checks battery level and, if sufficient, determines whether a task is
#assigned to either execute the task or remain idle; otherwise, it should go for charging.
Battery_Level = int(input("Enter Battery Level : "))
if Battery_Level >= 80 :
    Task_Assigned = input("Is there a task assigned? (yes/no) : ").lower()
    if Task_Assigned == "yes" :
        print("Execute the Task")
    else :
        print("Remain Idle")
elif Battery_Level >= 30 and Battery_Level < 80 :
    print("Return to Base")
elif Battery_Level >= 10 and Battery_Level < 30 :
    print("Shut Down Soon Return to Base")
else :
    print("Shut Down Immediately")
    