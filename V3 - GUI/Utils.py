import datetime
import os
class Files:
    class Config:
        Flag = "--- Config File ---"
        def Append(Text,State):
            if os.path.exists("Config.cfg"):
                #print("debug Point 1")
                f = open("Config.cfg", "a")
                TempRead = Files.Config.ReadLine(1)
                if TempRead.__contains__(Files.Config.Flag):
                    #print("debug Point 2")
                    f.write(Text + ":"+ State +":\n")
                else:
                    f.write(Files.Config.Flag + ":\n")
                    f.write(Text + ":"+ State +":\n")
                    #print("debug Point 3")
                f.close()
                
            else:
                f = open("Config.cfg", "x")
                f.close()
                Files.Config.Append(Text,State)  


        def Dump():
            f = open("Config.cfg", "r")
            dump = f.read()
            lines = dump.split("\n")
            State = str(lines).split(":")
            f.close()
            return State

        def ReadLine(line):
            arr = Files.Config.Dump()
            output = arr[line - 1]
            return output
        def Read(Search):
            dump = Files.Config.Dump()
            for i in range(0, len(Search)):
                if (i % 2) == 1:
                    cleaned = dump[i].split("[")
                    print(cleaned[0])
                elif (i % 2) == 0:
                    cleaned = dump[i].split("'")
                    print(cleaned[0])
                i = i + 1
class Array:
    def Write(Store:list,Index:int,Data):
        Store.append(Store[Index])
        Store[Index] = Data
    def Append(Store,Data):
        Store.append(Data)
    def Remove(Store,Index):
        del Store[Index]
    def Clear(Store):
        Store.clear()
class Input:
    def ReadString():
        Read = str(input())
        return Read
    def ReadInt():
        Read = int(input())
        return Read
    def ReadBool():
        Read = bool(input())
        return Read
    def ReadAny():
        Read = input()
        return Read
class Time:
    x = datetime.datetime.now()
    shortday = x.strftime("%a")
    longday = x.strftime("%A")
    day = x.strftime("%d")
    month = x.strftime("%m")
    year = x.strftime("%Y")
    hour = x.strftime("%H")
    Min = x.strftime("%M")
    shortmonthname = x.strftime("%b")
    longmonthname = x.strftime("%B")

    def GetTime():
        return(Time.hour + ":" + Time.Min)

    def GetDay(Text):
        return(Time.longday)
    
    def GetDate():
            return(""+Time.day+"/"+Time.month+"/"+Time.year)

    def GetDT():
        date = Time.GetDate()
        time = Time.GetTime()
        return(date + " " + time)


class CarPark:
    def ValidPlate(UsersPlate,Checker):
        SysCheckBits = 0
        CheckBits = 0
        ResultsUser = []
        ResultsSys = []
        for I in range(0,len(UsersPlate)):
            if UsersPlate[I] == "-":
                ResultsUser.append(I)
                CheckBits = CheckBits + 1
        for S in range(0,len(Checker)):
            if str(Checker[S]) == "-":
                ResultsSys.append(S)
                SysCheckBits = SysCheckBits + 1
        if CheckBits == SysCheckBits:
            for R in range(0,len(ResultsUser)):
                if ResultsUser[R] == ResultsSys[R]:
                    pass
                else:
                    return "Error"
            return "Done"
        else:
            return "Error"
    def RunBilling(Type:str,ArrivalTimeDate:dict):
        print(".............................................................. Generating Bill ..........................................................................")
        from Data import Settings,Config
        Days = 0
        Months = 0
        Years = 0
        Cost =0
        DaysElapsed =0
        DifInHours = 0
        if Config.UseAutomaticTime:
            LeaveTime = Time.GetTime()
            LeaveDate = Time.GetDate()
            LeaveDay = LeaveDate.split("/")[0]
            LeaveMonth = LeaveDate.split("/")[1]
            LeaveYear = LeaveDate.split("/")[2]
            Leave_date_object = datetime.datetime.strptime(LeaveDay+"-"+LeaveMonth+"-"+LeaveYear, '%d-%m-%Y').date()
            LeaveHour = LeaveTime.split(":")[0]
            LeaveMin = LeaveTime.split(":")[1]
        else:
            LeaveDate = input("Please Enter The Leave Date Eg, xx-xx-xx dd-mm-yy, or leave blank to use Todays Date: ("+str(Time.GetDate())+")")
            LeaveTime = input("Please Enter the Leave Time, Eg. xx:xx hh:mm")
            if not LeaveDate: #Checks that LeaveDate is Blank if it is then LeaveDate is None neaning it would eval to False
                LeaveDate = Time.GetDate()
            elif LeaveDate.__contains__("-"):
                if len(LeaveDate.split("-")) == 3:
                    LeaveDay = LeaveDate.split("-")[0]
                    LeaveMonth = LeaveDate.split("-")[1]
                    LeaveYear = LeaveDate.split("-")[2]
                    Leave_date_object = datetime.datetime.strptime(LeaveDay+"-"+LeaveMonth+"-"+LeaveYear, '%d-%m-%Y').date()
            if len(LeaveTime.split(":")) == 2:
                LeaveHour = LeaveTime.split(":")[0]
                LeaveMin = LeaveTime.split(":")[1]
        ArrivalDate = ArrivalTimeDate["Date"]
        ArrivalTime = ArrivalTimeDate["Time"]
        date_string = Leave_date_object.strftime('%Y-%m-%d')
        print("Arrival At: "+ ArrivalDate,ArrivalTime," Leave At: "+date_string+" "+LeaveHour+":"+LeaveMin)
        ArrivalDay = ArrivalDate.split("/")[0]
        ArrivalMonth = ArrivalDate.split("/")[1]
        ArrivalYear = ArrivalDate.split("/")[2]
        if ArrivalDay == LeaveDay:
            if ArrivalMonth == LeaveMonth:
                if ArrivalYear == LeaveYear:
                    print("Leave Same Day")
                else:
                    print("Static Charged Applied")
                    
        if int(LeaveMonth) > int(ArrivalMonth):
            Months = int(LeaveMonth) - int(ArrivalMonth)
            if LeaveMonth == 2:
                DaysInMonth = Config.Days_In_Feb
            else:
                DaysInMonth = Config.Days_In_Month
        if int(LeaveDay) > int(ArrivalDay):
            Days = int(LeaveDay) - int(ArrivalDay)
        if int(LeaveYear) > int(ArrivalYear):
            Years = int(LeaveYear) - int(ArrivalYear)
            DaysInYear = Config.Days_In_Year
        if Months != 0:
            for i in range(0,Months):
                DaysElapsed = DaysElapsed + DaysInMonth
        if Years != 0:
            for i in range(0,Years):
                DaysElapsed = DaysElapsed + DaysInYear
        DaysElapsed = DaysElapsed + Days
        if DaysElapsed > Config.ParkingExpire:
            DaysOver = DaysElapsed - Config.ParkingExpire
            if Config.StaticChargePerDay:
                for i in range(0,DaysOver):
                    Cost = Cost + Config.StaticCharge
            else:
                Cost = Cost + Config.StaticCharge
            for i in range(0,DaysElapsed):
                if Config.PriceInDays:
                    Cost = Cost + Settings[Type]['Price']
                else:
                    UpdatedCost = Settings[Type]['Price'] * Config.WorkLength
                    Cost = Cost + UpdatedCost
        else:
            for i in range(0,DaysElapsed):
                if Config.PriceInDays:
                    Cost = Cost + Settings[Type]['Price']
                else:
                    UpdatedCost = Settings[Type]['Price'] * Config.WorkLength
                    Cost = Cost + UpdatedCost
        if DaysElapsed == 0:
            if Config.PriceInDays:
                Cost = Cost + Settings[Type]['Price']
            else:
                DifInHours = int(LeaveHour) - int(ArrivalTime.split(":")[0])
                UpdatedCost = Settings[Type]['Price'] * DifInHours
                Cost = Cost + UpdatedCost
        return Cost.__round__(2),LeaveTime,LeaveDate
    
    def HandlePayment(VehicleData:dict,Cost:float,LeaveTime, LeaveDate):
        from Data import Config
        print("Payment Due: "+Config.Currency+str(Cost))
        if Config.HandlePaymentInternal:
            try:
                cardNumber = input("Please Enter Card Number: ")
                ExpireM = input("Please Enter Expiry Month Eg. XX 10: ")
                ExpireY = input("Please Enter Expiry Year Eg. XXXX 2026: ")
                CVV = input("Please Enter your CVV: ")
                Name = input("Please Enter the Name on the Account: ")
                card_values = {
                'card_number': cardNumber,
                'card_holder': Name,
                'expiration_date': ExpireM+"/"+ExpireY,
                'cvv': CVV,
                'Amount_Paid': Cost
                }
                from Utils import CarPark
                ID = CarPark.Write_Card_Details_To_Database(card_values)
                VehicleDetails ={'NumberPlate':VehicleData['NumberPlate'],'Owner_Name':VehicleData['Owner_Name'], 'vehicle_type':VehicleData['Vehicle_Type'], 'ArrivalTime':VehicleData['Arrival']['Time'], 'ArrivalDate':VehicleData['Arrival']['Date'], 'TotalAmountDue':Cost, 'PaymentID':ID, 'LeaveTime':LeaveTime, 'LeaveDate':LeaveDate}
                CarPark.Write_Previous_Vehicle_To_Database(VehicleDetails)
            except:
                return "Failed"
            return "OK"
        else:
            return "OK" #Once Code Wrote please Change this to be OK and Failed to be on a Failed Transaction or Error
    def Write_Card_Details_To_Database(values):
        import sqlite3
        from Data import Config
        print("Running A")
        # Connect to the database (creates it if not exists)
        conn = sqlite3.connect(Config.CardDatabase_FileName)
        print("Running A1")
        cursor = conn.cursor()
        print("Running A2")
        # Create a table if not exists
        cursor.execute('''CREATE TABLE IF NOT EXISTS CardDetails (
                            id INTEGER PRIMARY KEY,
                            card_number TEXT,
                            card_holder TEXT,
                            expiration_date TEXT,
                            cvv TEXT,
                            Amount_Paid REAL
                        )''')
        print("Running A3")
        id = cursor.lastrowid
        print("Running A4")
        print(values)
        # Insert values into the table
        # Assuming values is a dictionary
        values_tuple = (values['card_number'], values['card_holder'], values['expiration_date'], values['cvv'], values['Amount_Paid'])

        # Then execute the query
        cursor.execute('''
            INSERT INTO CardDetails (card_number, card_holder, expiration_date, cvv, Amount_Paid)
            VALUES (?, ?, ?, ?, ?)
        ''', values_tuple)


        print("Running A5")
        # Commit changes and close connection
        conn.commit()
        conn.close()
        print(str(id))
        return id

    def Write_Previous_Vehicle_To_Database(values):
        import sqlite3
        from Data import Config
        print("Running B")
        # Connect to the database (creates it if not exists)
        conn = sqlite3.connect(Config.PreviousVehicle_Database_FileName)
        cursor = conn.cursor()

        # Create a table if not exists
        cursor.execute('''CREATE TABLE IF NOT EXISTS PreviousVehicle (
                            space_id INTEGER PRIMARY KEY,
                            NumberPlate TEXT,
                            Owner_Name TEXT,
                            vehicle_type TEXT,
                            ArrivalTime TEXT,
                            ArrivalDate TEXT,
                            TotalAmountDue TEXT,
                            PaymentID TEXT,
                            LeaveTime TEXT,
                            LeaveDate TEXT
                        )''')

        # Insert values into the table
        cursor.execute('''INSERT INTO PreviousVehicle (NumberPlate, Owner_Name, vehicle_type, ArrivalTime, ArrivalDate, TotalAmountDue, PaymentID, LeaveTime, LeaveDate)
                    VALUES (:NumberPlate, :Owner_Name, :vehicle_type, :ArrivalTime, :ArrivalDate, :TotalAmountDue, :PaymentID, :LeaveTime, :LeaveDate)''', values)
        print(str(cursor.arraysize))
        # Commit changes and close connection
        conn.commit()
        conn.close()

    def Generate_SpacesRemainingLabels():
        Output =[]
        from Data import SpacesUsed
        for Key,Val in SpacesUsed.items():
            Output.append(str(Key+" "+str(Val['Occupied'])+"/"+str(Val['Allowed'])))
        return Output
