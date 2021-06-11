print("Plate number validator\n")
plateNumber = input("Please enter a plate number\n")
#consider validity of plate number
if (len(plateNumber) == 6 or len(plateNumber) == 7):
    #consider old plate number
    if plateNumber[0:3].isalpha():
        print("plate number is new")
    elif plateNumber[0:2].isalpha():
        print("plate number is old")
else:
    print ("plate number is not valid")
