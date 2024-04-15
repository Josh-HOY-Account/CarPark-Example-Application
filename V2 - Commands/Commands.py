from Data import Vehicle,Settings,SpacesUsed,Config
from Utils import Array,Time,CarPark
StationID = "Test"
def Menus(option:int):
    if option == 1:
        Menu.SaveMenu()
    elif option == 2:
        Menu.DeleteMenu()
    elif option == 3:
        Menu.ParkedSpaces()
    elif option == 4:
        Menu.RemaingSpaces()
    elif option ==5:
        Menu.ParkingRates()
    elif option ==6:
        print("... Thank you for using our service ...")
        print("............... Bye Bye ...............")
        exit()
    from CarPark import Program
    Program()
class Menu:
    def SaveMenu():
        Name = input("\tEnter owner name - ")
        if Name != "":
            print("Welcome: "+ Name)
            Types = []
            for Key, Value in Settings.items():
                print(Key)
                Types.append(Key)
            Vtype = int(input("\tEnter vehicle type: 1-" + str(len(Types))))
            if Checks.Spaces(Vtype):
                NumberPlate = input(f"Enter Vehicle Number Plate ({Config.PlateFormat}) - ").upper()
                if Checks.Numberplate_Format(NumberPlate):
                    Types = []
                    for Key, Value in Settings.items():
                        Types.append(Key)
                    Vehicle_Type = Types[Vtype - 1]
                    Details = {'NumberPlate':NumberPlate,'Vehicle_Type':Vehicle_Type,'OwnerName':Name}
                    SaveVehicle(Details,StationID)

    def DeleteMenu():
        NumberPlate=input(f"Enter vehicle number to Delete({Config.PlateFormat}) - ").upper()
        if Checks.Numberplate_Format(NumberPlate):
            for VehicleID in range(0,len(Vehicle)+1):
                if Vehicle[VehicleID-1]['NumberPlate'] == NumberPlate:
                    DeleteCar(VehicleID-1)
                    print("............................................................Removed Sucessfully..................................................................")


    def ParkedSpaces():
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


    def ParkingRates():
        C = Config.Currency
        V = 0
        print("----------------------------------------------------------------------------------------------------------------------")
        print("Parking Rate")
        print("----------------------------------------------------------------------------------------------------------------------")
        for I,P in Settings.items():
            V = V +1
            print(f"*{V}.{I}      {C}"+str(P['Price'])+ " / Hour")
        print("----------------------------------------------------------------------------------------------------------------------")


    def RemaingSpaces():
        print("----------------------------------------------------------------------------------------------------------------------")
        print("Spaces Left For Parking")
        print("----------------------------------------------------------------------------------------------------------------------")
        for Type,Val in SpacesUsed.items():
            print(f"Spaces Available for {Type} - ",str(Val['Occupied'])+"/"+str(Val['Allowed']))
        print("----------------------------------------------------------------------------------------------------------------------")


def SaveVehicle(Details:dict,StationID:str):
    Array.Append(Vehicle,{'NumberPlate':Details['NumberPlate'],'Vehicle_Type':Details['Vehicle_Type'],'Owner_Name':Details['OwnerName'],'Arrival':{'Date':Time.GetDate(),'Time':Time.GetTime()},'Station':StationID})
    SpacesUsed[Details['Vehicle_Type']]['Occupied'] += 1
    print("\n...Record detail saved...")

def Billing(VehicleID):
    Vehicle_Type = Vehicle[int(VehicleID)]['Vehicle_Type']
    ArrivalDTDict = Vehicle[int(VehicleID)]['Arrival']
    Cost,LeaveTime,LeaveDate = CarPark.RunBilling(Vehicle_Type,ArrivalDTDict)
    CarPark.HandlePayment(Vehicle[int(VehicleID)],Cost,LeaveTime,LeaveDate)

def DeleteCar(VehicleID):
    Vehicle.pop(VehicleID-1)
    Vehicle_Type = Vehicle[int(VehicleID)]['Vehicle_Type']
    SpacesUsed[Vehicle_Type]['Occupied'] -= 1



class Checks:
    def Numberplate_Format(NumberPlate):
        if NumberPlate == "":
            return False
        elif NumberPlate in Config.NumberPlates:
            return False
        elif len(NumberPlate) == len(Config.PlateFormat):
            if CarPark.ValidPlate(NumberPlate,Config.PlateFormat) == "Done":
                return True
            else:
                return False
        else:
            return False
        

    def Spaces(VType:int):
        Types = []
        for Key, Value in Settings.items():
            Types.append(Key)
        if 1 <= VType <= len(Types):
            Vehicle_Type = Types[VType - 1]
            if SpacesUsed[Vehicle_Type]['Occupied'] < SpacesUsed[Vehicle_Type]['Allowed']:
                return True
            else:
                return False
        else:
            return False