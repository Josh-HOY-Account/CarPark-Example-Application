def Test_Add():
    from Commands import SaveVehicle
    Details = {'NumberPlate':"1234",'Vehicle_Type':"Car",'OwnerName':"GitHub"}
    SaveVehicle(Details,"GitHub Test")
def Test_Remove():
    from Data import Vehicle
    from Commands import DeleteCar
    for VehicleID in range(0,len(Vehicle)+1):
        if Vehicle[VehicleID-1]['NumberPlate'] == "1234":
            DeleteCar(VehicleID-1)