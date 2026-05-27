# Develop a system that verifies whether a machine is operational and, if running,
#monitors temperature to decide whether cooling is required or normal operation can
#continue.
Machine_Status = input("Is the machine running? (yes/no) : ")
if Machine_Status.lower() == "yes" :
    Temperature = int(input("Enter Temperature : "))
    if Temperature >= 80 :
        print("Cooling Required")
    else :
        print("Normal Operation Can Continue")
else :
    print("Machine is not running") 