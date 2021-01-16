from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import time
import User_interface as UU
import Scraper as SC
root = Tk(className = "dUB_IOS")
root.geometry('380x400')
root.configure(bg = 'black')

BACK_GROUND = 'black'
FORE_GROUND =  'black'
FONT = "Helvetica 10 bold"
FONT_COLOR = 'white'
COLOR_ON  = 'red'
COLOR_OFF = 'white'


class UI:
    def __init__(self):
        r = UU.User_I()
        self.r = r
        self.scrapper = SC.SCRAPE()
        self.USER_ACCOUNT = r.USER_ACCOUNT

        l1 = Label(root , text = "FROM SKYE_SOFTWARES:" , fg = FONT_COLOR, bg = BACK_GROUND , font = "Helvetica 8 bold")
        l1.place(x = 10 , y = 340)

        ACCOUNT_PSWD = Label(root , text = "ACCOUNT_PSWD  :"  , fg = FONT_COLOR, bg = BACK_GROUND , font = FONT)
        l1 = Label(root , text = 'DEMO PRODUCT FOR\n\n{}\n\nJUST ENTER YOUR PASSWORD\n AND PRESS LAUNCH dUB_IOS'.format(self.USER_ACCOUNT), fg = FONT_COLOR, bg = BACK_GROUND , font = FONT)
        l1.place(x = 150 , y = 200)
        ACCOUNT_EMAIL = Label(root , text = "ACCOUNT_EMAIL  :" , fg = FONT_COLOR, bg = BACK_GROUND , font = FONT)
        ACCOUNT_EMAIL.place(x = 10 , y = 40)   

        ACCOUNT_PSWD = Label(root , text = "ACCOUNT_PSWD  :"  , fg = FONT_COLOR, bg = BACK_GROUND , font = FONT)
        ACCOUNT_PSWD.place(x = 10 , y = 80) 

        REFRESH_RATE = Label(root , text = "REFRESH_RATE    :"  , fg = FONT_COLOR, bg = BACK_GROUND , font = FONT)
        REFRESH_RATE.place(x = 10 , y = 120)

        self.e1 = Entry(root , width = 30 , font = FONT)
        self.e1.place(x =150 , y = 40)

        self.e2 = Entry(root , width = 30 , font = FONT)
        self.e2.place(x =150 , y = 80)

        self.e4 = Entry(root , width = 30 , font = FONT)
        self.e4.place(x =150 , y = 120)

        self.Go_BTN =Button(root , text = 'LAUNCH dUB_IOS' , command = self.Go_Button , font = FONT)
        self.Go_BTN.place(x = 10 , y = 280)

        self.B_Head = Button(root , text = 'ENABLE BROWSER' ,command = self.Enable_Browser_Button , font = FONT, bg = COLOR_OFF)#User_I.Enable_Browser)
        self.B_Head.place(x = 10 , y = 200)
   
    def Go_Button(self):
        if self.r.ERROR(self.USER_ACCOUNT) == 'True':
            messagebox.showwarning(title = "ERROR" , message = "PLEASE ENTER YOUR ACCOUNT_EMAIL")
            return 0
        if self.r.ERROR(self.e2.get() , email = self.USER_ACCOUNT) == 'True':
            messagebox.showwarning(title = "ERROR" , message = "THE USER ACCOUNT_EMAIL {} DOESNT SEEM TO EXIST\n\n1:  CHECK WHETHER YOU HAVE ENTERED THE CORRECT EMAIL ADDRESS(CHECK FOR SPACES AT THE BEGINNING OF THE EMAIL ADDRESSS)\n\n2: SAVE A NEW ACCOUNT BY FILLING THE ENTIRE FORM AND PRESSING LAUNCH dUB_IOS".format(self.USER_ACCOUNT))
            return 0        
        else:
            if self.r.ERROR(self.e2.get() , email = self.USER_ACCOUNT) == 'False':
                pswd = self.r.PSWD
            else:
                pswd = self.e2.get()
            print(pswd,self.USER_ACCOUNT )
            pswd  , email =self.scrapper.PASS_CODES(pswd ,self.USER_ACCOUNT )
            try:
                if int(self.e4.get()) < 3:
                    r_time = 3
                else:
                    r_time = int(self.e4.get())
                self.scrapper = SC.SCRAPE(visible = self.r.head , password=pswd , email  = email , refresh_time= r_time)
                messagebox.showinfo(title = 'RUNNING', message='THIS MIGHT TAKE A MOMENT. PLEASE BE PATIENT')
                error = self.scrapper.Launch()
                if error == 'SUCCESSFUL':
                    messagebox.showwarning(title = 'SUCCESSFUL', message= 'YOU GOT WORK TO DO')
                if error ==  'FAILED':
                    choice = messagebox.askyesno(title = "ERROR" , message = "SEEMS YOU LOST THE JOB/ALREADY WORKING ON ONE\nPLEASE CHECK INTO YOUR ACCOUNT OR RESTART dUB_IOS")
                    if choice == 1:
                        self.scrapper.driver.close()
                        self.Go_Button()
            except ValueError:
                    messagebox.showwarning(title = "ERROR" , message = "PLEASE ENTER A REFRESH RATE/USE AN INTEGERS e.g 10\n(suggested rate is 10 seconds)")
        
    def Enable_Browser_Button(self):
        action = self.r.Enable_Browser()
        if action == 'headless':
            self.B_Head.destroy()
            self.B_Head = Button(root , text = 'ENABLE BROWSER' ,command = self.Enable_Browser_Button , font = FONT, bg = COLOR_OFF)#User_I.Enable_Browser)
            self.B_Head.place(x = 10 , y = 200)
        else:
            self.B_Head.destroy()
            self.B_Head = Button(root , text = 'DISABLE BROWSER' ,command = self.Enable_Browser_Button , font = FONT, bg = COLOR_ON)#User_I.Enable_Browser)
            self.B_Head.place(x = 10 , y = 200)

    def AUTO_FILL(self):
        pass

        
j = UI()


root.resizable(width=False, height=False)
root.mainloop()  

