def test_Add():
    from Commands import SaveVehicle
    Details = {'NumberPlate':"1111",'Vehicle_Type':"Cars",'OwnerName':"GitHub"}
    SaveVehicle(Details,"GitHub Test")
def test_Remove():
    from Data import Vehicle
    from Commands import DeleteCar,SaveVehicle
    Details = {'NumberPlate':"1234",'Vehicle_Type':"Cars",'OwnerName':"GitHub"}
    SaveVehicle(Details,"GitHub Test")
    for VehicleID in range(0,len(Vehicle)):
        print(VehicleID)
        if Vehicle[VehicleID]['NumberPlate'] == "1234":
            DeleteCar(VehicleID-1)