import tkinter as tk
import tkinter.font as tkFont

class App:
    def __init__(self, root):
        #setting title
        root.title("undefined")
        #setting window size
        width=588
        height=546
        screenwidth = root.winfo_screenwidth()
        screenheight = root.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        root.geometry(alignstr)
        root.resizable(width=False, height=False)

        GButton_557=tk.Button(root)
        GButton_557["bg"] = "#e9e9ed"
        GButton_557["cursor"] = "circle"
        ft = tkFont.Font(family='Times',size=22)
        GButton_557["font"] = ft
        GButton_557["fg"] = "#000000"
        GButton_557["justify"] = "center"
        GButton_557["text"] = "Add New vehicle"
        GButton_557["relief"] = "raised"
        GButton_557.place(x=30,y=70,width=256,height=70)
        GButton_557["command"] = self.GButton_557_command

        GButton_298=tk.Button(root)
        GButton_298["bg"] = "#e9e9ed"
        GButton_298["cursor"] = "circle"
        ft = tkFont.Font(family='Times',size=22)
        GButton_298["font"] = ft
        GButton_298["fg"] = "#000000"
        GButton_298["justify"] = "center"
        GButton_298["text"] = "Remove vehicle"
        GButton_298["relief"] = "raised"
        GButton_298.place(x=30,y=150,width=256,height=70)
        GButton_298["command"] = self.GButton_298_command

        GLabel_968=tk.Label(root)
        ft = tkFont.Font(family='Times',size=10)
        GLabel_968["font"] = ft
        GLabel_968["fg"] = "#333333"
        GLabel_968["justify"] = "center"
        GLabel_968["text"] = "Current Spaces Remaining"
        GLabel_968.place(x=70,y=230,width=176,height=30)

        GLabel_13=tk.Label(root)
        ft = tkFont.Font(family='Times',size=10)
        GLabel_13["font"] = ft
        GLabel_13["fg"] = "#333333"
        GLabel_13["justify"] = "center"
        GLabel_13["text"] = "123456789"
        GLabel_13.place(x=120,y=260,width=70,height=25)

        GLabel_917=tk.Label(root)
        ft = tkFont.Font(family='Times',size=10)
        GLabel_917["font"] = ft
        GLabel_917["fg"] = "#333333"
        GLabel_917["justify"] = "center"
        GLabel_917["text"] = "123456789"
        GLabel_917.place(x=120,y=290,width=70,height=25)

        GLabel_308=tk.Label(root)
        ft = tkFont.Font(family='Times',size=10)
        GLabel_308["font"] = ft
        GLabel_308["fg"] = "#333333"
        GLabel_308["justify"] = "center"
        GLabel_308["text"] = "123456789"
        GLabel_308.place(x=120,y=320,width=70,height=25)

        GLabel_406=tk.Label(root)
        ft = tkFont.Font(family='Times',size=10)
        GLabel_406["font"] = ft
        GLabel_406["fg"] = "#333333"
        GLabel_406["justify"] = "center"
        GLabel_406["text"] = "123456789"
        GLabel_406.place(x=120,y=380,width=70,height=25)

        GLabel_965=tk.Label(root)
        ft = tkFont.Font(family='Times',size=10)
        GLabel_965["font"] = ft
        GLabel_965["fg"] = "#333333"
        GLabel_965["justify"] = "center"
        GLabel_965["text"] = "123456789"
        GLabel_965.place(x=120,y=350,width=70,height=25)

        GLabel_564=tk.Label(root)
        ft = tkFont.Font(family='Times',size=10)
        GLabel_564["font"] = ft
        GLabel_564["fg"] = "#333333"
        GLabel_564["justify"] = "center"
        GLabel_564["text"] = "123456789"
        GLabel_564.place(x=120,y=410,width=70,height=25)

        GLabel_285=tk.Label(root)
        ft = tkFont.Font(family='Times',size=30)
        GLabel_285["font"] = ft
        GLabel_285["fg"] = "#333333"
        GLabel_285["justify"] = "center"
        GLabel_285["text"] = "vehicle Parking System"
        GLabel_285.place(x=80,y=20,width=434,height=30)

        GListBox_484=tk.Listbox(root)
        GListBox_484["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        GListBox_484["font"] = ft
        GListBox_484["fg"] = "#333333"
        GListBox_484["justify"] = "center"
        GListBox_484.place(x=390,y=90,width=80,height=25)
        GListBox_484["listvariable"] = "1,2,3,4,5"
        GListBox_484["selectmode"] = "single"
        GListBox_484["setgrid"] = "True"

        GLineEdit_795=tk.Entry(root)
        GLineEdit_795["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        GLineEdit_795["font"] = ft
        GLineEdit_795["fg"] = "#333333"
        GLineEdit_795["justify"] = "center"
        GLineEdit_795["text"] = "Entry"
        GLineEdit_795.place(x=440,y=130,width=70,height=25)

        GLineEdit_546=tk.Entry(root)
        GLineEdit_546["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        GLineEdit_546["font"] = ft
        GLineEdit_546["fg"] = "#333333"
        GLineEdit_546["justify"] = "center"
        GLineEdit_546["text"] = "Entry"
        GLineEdit_546.place(x=440,y=170,width=70,height=25)

        GLabel_767=tk.Label(root)
        ft = tkFont.Font(family='Times',size=10)
        GLabel_767["font"] = ft
        GLabel_767["fg"] = "#333333"
        GLabel_767["justify"] = "center"
        GLabel_767["text"] = "Owner Name"
        GLabel_767.place(x=340,y=130,width=88,height=31)

        GLineEdit_266=tk.Entry(root)
        GLineEdit_266["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        GLineEdit_266["font"] = ft
        GLineEdit_266["fg"] = "#333333"
        GLineEdit_266["justify"] = "center"
        GLineEdit_266["text"] = "Number Plate"
        GLineEdit_266.place(x=340,y=170,width=88,height=30)

        GButton_497=tk.Button(root)
        GButton_497["bg"] = "#e9e9ed"
        ft = tkFont.Font(family='Times',size=10)
        GButton_497["font"] = ft
        GButton_497["fg"] = "#000000"
        GButton_497["justify"] = "center"
        GButton_497["text"] = "Button"
        GButton_497.place(x=400,y=220,width=70,height=25)
        GButton_497["command"] = self.GButton_497_command

        GLabel_982=tk.Label(root)
        ft = tkFont.Font(family='Times',size=10)
        GLabel_982["font"] = ft
        GLabel_982["fg"] = "#333333"
        GLabel_982["justify"] = "center"
        GLabel_982["text"] = "label"
        GLabel_982.place(x=400,y=260,width=70,height=25)

    def GButton_557_command(self):
        print("command")


    def GButton_298_command(self):
        print("command")


    def GButton_497_command(self):
        print("command")

if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()
