from Utils import Array,Time,CarPark,datetime
from Data import Vehicle,Settings,SpacesUsed,Config
def Program():
    Menu_MainMenu()  
try:
    def Menu_MainMenu():
        print("----------------------------------------------------------------------------------------")
        print("                               Parking Management System                                ")
        print("----------------------------------------------------------------------------------------")
        print("1.    Vehicle Entry")#
        print("2.    Remove Entry" )#
        print("3.    View Parked Vehicle ")
        print("4.    View Left Parking Space ")#
        print("5.    View Parking Rates ")#
        print("6.    Close Programme ")#
        print("+-------------------------------------------------------------------------------------+")
        MenuOption = int(input("\tSelect option:"))
        if MenuOption == 1:
            Menu_SaveCar()
        elif MenuOption == 2:
            Menu_DeleteVehicle()
        elif MenuOption == 3:
            Menu_ShowParkedSpaces()
        elif MenuOption == 4:
            Menu_ShowSpacesLeft()
        elif MenuOption ==5:
            Menu_Rates()
        elif MenuOption ==6:
            print("... Thank you for using our service ...")
            print("............... Bye Bye ...............")
            exit()

    def Menu_SaveCar():
        Config.RunValid_CarPlate = True
        Config.RunValid_VType = False
        Config.RunValid_OwnerName = False
        while Config.RunValid_CarPlate:
            NumberPlate = input(f"Enter Vehicle Number Plate ({Config.PlateFormat}) - ").upper()
            if NumberPlate == "":
                print("#Enter Vehicle Number Plate")
            elif NumberPlate in Config.NumberPlates:
                print("#Vehicle Number Already Exists")
            elif len(NumberPlate) == len(Config.PlateFormat):
                if CarPark.ValidPlate(NumberPlate,Config.PlateFormat) == "Done":
                    Config.RunValid_CarPlate = False
                    Config.RunValid_OwnerName = False
                    Config.RunValid_VType = True
                    print("Number Plate Saved")
                else:
                    print("#Enter Valid Vehicle Number...")
            else:
                print("#Enter Valid Vehicle Number...")

        while Config.RunValid_VType == True:
            Types = []
            for Key, Value in Settings.items():
                print(Key)
                Types.append(Key)
            Vtype = int(input("\tEnter vehicle type: 1-" + str(len(Types))))
            if 1 <= Vtype <= len(Types):
                Vehicle_Type = Types[Vtype - 1]
                if SpacesUsed[Vehicle_Type]['Occupied'] < SpacesUsed[Vehicle_Type]['Allowed']:
                    SpacesUsed[Vehicle_Type]['Occupied'] += 1
                    Config.RunValid_CarPlate = False
                    Config.RunValid_OwnerName = True
                    Config.RunValid_VType = False
                else:
                    print("###### No more parking space available for {} ######".format(Vehicle_Type))

        else:
            print("###### Please Enter Valid Option ######")

        while Config.RunValid_OwnerName==True:
            OwnerName = input("\tEnter owner name - ")
            if OwnerName == "":
                print("###### Please Enter Owner Name ######")
            else:
                Array.Append(Vehicle,{'NumberPlate':NumberPlate,'Vehicle_Type':Vehicle_Type,'Owner_Name':OwnerName,'Arrival':{'Date':Time.GetDate(),'Time':Time.GetTime()}})
                Config.RunValid_OwnerName = False
        print("\n...Record detail saved...")
        if Config.AskToLoop:
            Waiting = True
            while Waiting:
                RunAgain = str(input("Would You Like to Add Another Vehicle?"))
                Answer = RunAgain[0].lower()
                if Answer == "y":
                    Waiting = False
                    Config.RunValid_CarPlate = True
                    Config.RunValid_VType = False
                    Config.RunValid_OwnerName = False
                    Menu_SaveCar()
                elif Answer == "n":
                    Waiting = False
                    print(SpacesUsed)
                    #print(Vehicle)
                    Menu_MainMenu()
                else:
                    print("Please Enter Yes or No")

    def Menu_ShowSpacesLeft():
        print("----------------------------------------------------------------------------------------------------------------------")
        print("Spaces Left For Parking")
        print("----------------------------------------------------------------------------------------------------------------------")
        for Type,Val in SpacesUsed.items():
            print(f"Spaces Available for {Type} - ",str(Val['Occupied'])+"/"+str(Val['Allowed']))
        print("----------------------------------------------------------------------------------------------------------------------")
        Menu_MainMenu()
    def Menu_DeleteVehicle():
        Config.RunValid_DeleteVehicle=True
        while Config.RunValid_DeleteVehicle==True:
            NumberPlate=input(f"Enter vehicle number to Delete({Config.PlateFormat}) - ").upper()
            if NumberPlate=="":
                print("###### Enter Vehicle No. ######")
            elif len(NumberPlate)==len(Config.PlateFormat):
                if CarPark.ValidPlate(NumberPlate,Config.PlateFormat) == "Done":
                    for I in range(0,len(Vehicle)+1):
                        if Vehicle[I-1]['NumberPlate'] == NumberPlate:
                            Vehicle_Type = Vehicle[I-1]['Vehicle_Type']
                            print(Vehicle[I-1])
                            Cost = CarPark.RunBilling(Vehicle[I-1])
                            CarPark.HandlePayment(Vehicle[I-1],Cost)
                            print("Payment Due: "+Config.Currency+str(Cost))
                            Vehicle.pop(I)
                            SpacesUsed[Vehicle_Type]['Occupied'] -= 1
                            Config.RunValid_DeleteVehicle=False
                            print("............................................................Removed Sucessfully..................................................................")
                            if Config.AskToLoop:
                                Waiting = True
                                while Waiting:
                                    RunAgain = str(input("Would You Like to Remove Another Vehicle?"))
                                    Answer = RunAgain[0].lower()
                                    if Answer == "y":
                                        Waiting = False
                                        Menu_DeleteVehicle()
                                    elif Answer == "n":
                                        Waiting = False
                                        Config.RunValid_DeleteVehicle=False
                                        print(SpacesUsed)
                                        #print(Vehicle)
                                        Menu_MainMenu()
                                    else:
                                        print("Please Enter Yes or No")
            else:
                print("###### Enter Valid Vehicle Number ######")

    def Menu_Rates():
        C = Config.Currency
        V = 0
        print("----------------------------------------------------------------------------------------------------------------------")
        print("Parking Rate")
        print("----------------------------------------------------------------------------------------------------------------------")
        for I,P in Settings.items():
            V = V +1
            print(f"*{V}.{I}      {C}"+str(P['Price'])+ " / Hour")
        print("----------------------------------------------------------------------------------------------------------------------")
    def Menu_ShowParkedSpaces():
        print("----------------------------------------------------------------------------------------------------------------------")
        print("\t\t\t\tParked Vehicle")
        print("----------------------------------------------------------------------------------------------------------------------")
        print("Vehicle No.\tVehicle Type\t\t\tOwner Name\t\tDate\t\t\tTime")
        print("----------------------------------------------------------------------------------------------------------------------")
        for i in range(len(Vehicle)):
            print(Vehicle[i]['NumberPlate'],"\t\t",Vehicle[i]['Vehicle_Type'],"\t\t\t\t",Vehicle[i]['Owner_Name'],"\t\t\t",Vehicle[i]['Arrival']['Date'],"\t\t",Vehicle[i]['Arrival']['Time'])
        print("----------------------------------------------------------------------------------------------------------------------")
        print("------------------------------------------ Total Records - ",len(Vehicle),"-------------------------------------------------------")
        print("----------------------------------------------------------------------------------------------------------------------")
        Menu_MainMenu()
except KeyboardInterrupt:
    print("Restarting Program")
    Program()
Program()

        
