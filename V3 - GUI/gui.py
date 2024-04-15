import tkinter as tk
from tkinter import ttk
import tkinter.font as tkFont
from Utils import CarPark

StationID = "GUI 1"
width = 588
height = 546
Type = ""

class App:
    def __init__(self, root):
        # Setting title
        self.expandable_widgets = []
        root.title("Car Park Application")
        # Setting window size and position
        screenwidth = root.winfo_screenwidth()
        screenheight = root.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % ((width, height, (screenwidth - width) / 2, (screenheight - height) / 2))
        root.geometry(alignstr)
        root.resizable(width=False, height=False)
        
        # Initialize labels
        self.lbl_spaces = []
        self.reload_labels()
        
        # Buttons
        btn_add = tk.Button(root, bg="#e9e9ed", cursor="circle", font=tkFont.Font(family='Times', size=22), fg="#000000",
                            justify="center", text="Add New vehicle", relief="raised", command=self.btn_add_command)
        btn_add.place(x=30, y=70, width=256, height=70)

        btn_remove = tk.Button(root, bg="#e9e9ed", cursor="circle", font=tkFont.Font(family='Times', size=22), fg="#000000",
                               justify="center", text="Remove vehicle", relief="raised", command=self.btn_remove_command)
        btn_remove.place(x=30, y=150, width=256, height=70)
        
        # Labels
        lbl_spaces_main = tk.Label(root, font=tkFont.Font(family='Times', size=10), fg="#333333", justify="center",
                                   text="Current Spaces Remaining")
        lbl_spaces_main.place(x=70, y=230, width=176, height=30)

        lbl_main_title = tk.Label(root, font=tkFont.Font(family='Times', size=30), fg="#333333", justify="center",
                                   text="Vehicle Parking System")
        lbl_main_title.place(x=80, y=20, width=434, height=30)

    def reload_labels(self):
        SPCalc = CarPark.Generate_SpacesRemainingLabels()
        
        if not self.lbl_spaces:
            for i in range(6):
                lbl_space = tk.Label(root, font=tkFont.Font(family='Times', size=10), fg="#333333", justify="center")
                lbl_space.place(x=120, y=260 + i * 30, width=70, height=25)
                self.lbl_spaces.append(lbl_space)

        for i in range(len(self.lbl_spaces)):
            try:
                self.lbl_spaces[i]["text"] = SPCalc[i]
            except IndexError:
                self.lbl_spaces[i]["text"] = ""

    def expand(self):
        
        def on_select(event):
            global Type
            selected_item = event.widget.get()
            print(selected_item)
            btn_save = tk.Button(root, bg="#e9e9ed", font=tkFont.Font(family='Times', size=10), fg="#000000", justify="center", text="Save")
            btn_save.place(x=400, y=220, width=70, height=25)
            btn_save["command"] = lambda: self.btn_save_command(txt_name, txt_plate)
            self.expandable_widgets.append(btn_save)
            Type = selected_item

        # Array of options
        from Data import Settings
        Out = ["Select a Type"]
        for k,v in Settings.items():
            Out.append(k)

        gbx_type = ttk.Combobox(root, values=Out, state="readonly")
        gbx_type.current(0)
        gbx_type.bind("<<ComboboxSelected>>", on_select)
        gbx_type.place(x=390, y=90, width=80, height=25)
        self.expandable_widgets.append(gbx_type)

        txt_name = tk.Text(root, height=1, width=20)
        txt_name.place(x=440, y=130, width=70, height=25)
        self.expandable_widgets.append(txt_name)
        txt_plate = tk.Text(root, height=1, width=20)
        txt_plate.place(x=440, y=170, width=70, height=25)
        self.expandable_widgets.append(txt_plate)

        lbl_Name = tk.Label(root, text="Owner Name", font=tkFont.Font(family='Times', size=10), fg="#333333", justify="center")
        lbl_Name.place(x=340, y=130, width=88, height=31)
        self.expandable_widgets.append(lbl_Name)

        lbl_Plate = tk.Label(root, text="Number Plate", font=tkFont.Font(family='Times', size=10), fg="#333333", justify="center")
        lbl_Plate.place(x=340, y=170, width=88, height=30)
        self.expandable_widgets.append(lbl_Plate)

        root.geometry(str(width + 200) + "x" + str(height))

    def btn_save_command(self, txt_name, txt_plate):
        name = txt_name.get("1.0", "end-1c")
        plate = txt_plate.get("1.0", "end-1c")
        global Type
        if name:
            if plate:
                from Commands import Checks
                from Data import Config
                if Checks.Numberplate_Format(plate):
                    from Commands import SaveVehicle
                    Details = {'NumberPlate': plate, 'Vehicle_Type': Type, 'OwnerName': name}
                    SaveVehicle(Details, StationID)
                    self.reload_labels()
                    root.geometry(str(width) + "x" + str(height))
                    for widget in self.expandable_widgets:
                        widget.destroy()
                    # Clear the list of expandable widgets
                    self.expandable_widgets.clear()
                else:
                    try:
                        GLabel_982
                    except:
                        pass
                    GLabel_982=tk.Label(root)
                    ft = tkFont.Font(family='Times',size=10)
                    GLabel_982["font"] = ft
                    GLabel_982["fg"] = "#333333"
                    GLabel_982["justify"] = "center"
                    GLabel_982["text"] = "Plate Format: "+Config.PlateFormat
                    GLabel_982.place(x=400,y=260,width=190,height=25)
            else:
                try:
                    GLabel_982
                except:
                    pass
                GLabel_982=tk.Label(root)
                ft = tkFont.Font(family='Times',size=10)
                GLabel_982["font"] = ft
                GLabel_982["fg"] = "#333333"
                GLabel_982["justify"] = "center"
                GLabel_982["text"] = "Please Enter Your Number Plate"
                GLabel_982.place(x=400,y=260,width=190,height=25)
        else:
            try:
                GLabel_982["text"] = ""
            except:
                pass
            GLabel_982=tk.Label(root)
            ft = tkFont.Font(family='Times',size=10)
            GLabel_982["font"] = ft
            GLabel_982["fg"] = "#333333"
            GLabel_982["justify"] = "center"
            GLabel_982["text"] = "Please Enter your Name:"
            GLabel_982.place(x=400,y=260,width=150,height=25)

    def btn_add_command(self):
        self.expand()

    def btn_remove_command(self):
        print("Remove")

if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()
