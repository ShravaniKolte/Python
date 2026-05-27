#Create an automated door system that detects a person and, if detected, verifies
#authorization before granting or denying access.
Person_Detected = input("Is there a person detected? (yes/no) : ").lower()
if Person_Detected == "yes" :
    Authorization = input("Is the person authorized? (yes/no) : ").lower()
    if Authorization == "yes" :
        print("Access Granted")
    else :
        print("Access Denied")
else :
    print("No Person Detected")
    