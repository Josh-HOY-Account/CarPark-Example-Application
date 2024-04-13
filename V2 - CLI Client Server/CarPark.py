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
        from Commands import Menus
        Menus(MenuOption)

except KeyboardInterrupt:
    print("Restarting Program")
    Program()
Program()

        
