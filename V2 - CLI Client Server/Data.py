Vehicle = []
Settings ={'Bikes':{'Price':6.70,'Allowed':10},'Cars':{'Price':9.90,'Allowed':80},'Bicycles':{'Price':2.50,'Allowed':20}}
SpacesUsed = {vehicle_type: {'Occupied': 0, 'Allowed': settings['Allowed']} for vehicle_type, settings in Settings.items()}

class Config:
    AskToLoop = True
    Currency = "£"
    RunValid_CarPlate = True
    RunValid_VType = False
    RunValid_OwnerName = False
    PlateFormat = "****"
    RunValid_DeleteVehicle=True
    NumberPlates = []
    UseAutomaticTime = False #Use Current Time on Leave (False = Debugging) Should be True during Deployment
    StaticCharge = 100 #static charge per day after expiry
    WorkLength = 6 #hours in a day Calc Refers as 6.001492537313433
    ParkingExpire = 10 #Length in days before static charge
    Days_In_Feb = 28
    Days_In_Month = 31
    Days_In_Year = 365
    PriceInDays = False
    StaticChargePerDay = True
    HandlePaymentInternal = True #Will Display Payment declined Currently as there is no code wrote in Utils.CarPark.HandlePayments
    CardDatabase_FileName = "CardDetails.db"
    PreviousVehicle_Database_FileName = "PreviousVehicle.db"