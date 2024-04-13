def Menus(option):
    if option == 1:
        Menu.SaveCar()
    elif option == 2:
        Menu.DeleteVehicle()
    elif option == 3:
        Menu.ShowParkedSpaces()
    elif option == 4:
        Menu.ShowSpacesLeft()
    elif option ==5:
        Menu.Rates()
    elif option ==6:
        print("... Thank you for using our service ...")
        print("............... Bye Bye ...............")
        exit()

class Menu:
    pass