from tkinter import *
from defofthemain import *
from PIL import Image, ImageTk
# GUI





showOrNotValue = 0
class app():
    def __init__(self):
        global mainwindow
        self.mainwindow = Tk()
        #ALL OF THIS IS PART OF THE SAME FUNCTION
        #########################################
        #I'm not pretty sure why but the function have to be right below the window variable ¯\_(ツ)_/¯

        showingimage = Image.open(r"C:\Users\guilh\Desktop\ThisIsMyMainProjectRightNow\images\showing.png")
        showingimage = showingimage.resize((50,25))
        
        
        showingimg = ImageTk.PhotoImage(showingimage)
        
        notshowingimage = Image.open(r"C:\Users\guilh\Desktop\ThisIsMyMainProjectRightNow\images\notshowing.png")
        notshowingimage = notshowingimage.resize((50,25))
        
        
        notshowingimg = ImageTk.PhotoImage(notshowingimage)
        
        
        def changeImage(button, showEntry):
            global showOrNotValue
            
            if showOrNotValue == 1:
                showOrNotValue = 0
                # print(showOrNotValue)
                button.config(image=showingimg)
                showEntry.config(show="*")
            else:
                showOrNotValue = 1
                button.config(image=notshowingimg)
                showEntry.config(show="")
                # print(showOrNotValue)
        
        #########################################
        mainwindow = self.mainwindow
        self.mainwindow.title('Database Manager')
        self.mainwindow.state("zoomed")
        self.menu_frame = Frame(self.mainwindow, relief= FLAT)
        menu_frame = self.menu_frame
        self.register_frame = Frame(self.mainwindow, relief=FLAT)
        self.loggin_frame = Frame(self.mainwindow, relief=FLAT)

        self.width = self.mainwindow.winfo_screenwidth()
        self.height = self.mainwindow.winfo_screenheight()
        # mainwindow.resizable(False, False)
        #-------------------------------------------------------------------------------------
        #WIDGETS menu_frame
        self.registerbutton = Button(self.menu_frame, text='Register', font='Arial 40', command=lambda: show(self.register_frame), padx=15, pady=10)
        self.logginbutton = Button(self.menu_frame, text='Loggin', font='Arial 40', command=lambda: show(self.loggin_frame), padx=50, pady=10)
        ab(self.registerbutton)
        ab(self.logginbutton)

        #LAYOUT menu_frame
        self.menu_frame['width'] = self.width
        self.menu_frame['height'] = self.height
        self.registerbutton.place(relx=0.5, rely=0.4, anchor=CENTER)
        self.logginbutton.place(relx=0.5, rely=0.6, anchor=CENTER)

        #-----------------------------------------------------------------------------------------------------------------------
        #-----------------------------------------------------------------------------------------------------------------------
        #-----------------------------------------------------------------------------------------------------------------------
        
        
        #WIDGETS register_frame
        #Labels
        self.label_user = Label(self.register_frame, text='User:', font='Arial 30')
        self.label_password = Label(self.register_frame, text='Password:', font='Arial 30')
        self.label_confirm_password = Label(self.register_frame, text='Confirm Password:', font='Arial 30')
        #----------------------------------------------------------------------------------
        #Entries
        self.user_entry_register = Entry(self.register_frame, font='Arial 40')
        self.password_entry_register = Entry(self.register_frame, show="*", font='Arial 40')
        self.confirm_password_entry_register = Entry(self.register_frame, show="*", font='Arial 40')
        #----------------------------------------------------------------------------------
        #Buttons
        self.register_button = Button(self.register_frame, text='Register', font='Arial 40', command=lambda: register_attempt(mainwindow, self.user_entry_register, self.password_entry_register, self.confirm_password_entry_register,frameback=menu_frame))
        self.goback_button = Button(self.register_frame,  text='Go back', font='Arial 40', command=lambda: show(self.menu_frame, self.user_entry_register, self.password_entry_register, self.confirm_password_entry_register))
        self.showpasswordbutton = Button(self.register_frame, image=showingimg, command=lambda:changeImage(self.showpasswordbutton, self.password_entry_register))
        self.showconfirmpasswordbutton = Button(self.register_frame, image=showingimg, command=lambda:changeImage(self.showconfirmpasswordbutton, self.confirm_password_entry_register))
        
        ab(self.register_button)
        ab(self.showpasswordbutton)
        ab(self.showconfirmpasswordbutton)
        ab(self.goback_button)

        #Checkbutton
        # self.cregister_var = IntVar()
        # self.register_checkbutton = Checkbutton(self.register_frame,font="Arial 15", text="Show Password", width=20,height=20, variable=self.cregister_var, onvalue=1, offvalue=0, command=lambda:showPassword(self.password_entry_register, self.cregister_var))
        
        #------------------------------------------------------------------------------------------------------------------------
        
        #LAYOUT register_frame
        self.loggin_frame['width'] = self.width 
        self.loggin_frame['height'] = self.height

        self.label_user.place(relx=0.25, rely=0.2, anchor=CENTER)
        self.label_password.place(relx=0.219, rely=0.3, anchor=CENTER)
        self.user_entry_register.place(relx=0.55, rely=0.2, anchor=CENTER)
        self.password_entry_register.place(relx=0.55, rely=0.3, anchor=CENTER)
        self.confirm_password_entry_register.place(relx=0.55, rely=0.4, anchor=CENTER)
        self.register_button.place(relx=0.5, rely=0.65, anchor=CENTER)
        self.label_confirm_password.place(relx=0.162, rely=0.4, anchor=CENTER)
        # self.register_checkbutton.place(relx=0.920, rely=0.65, anchor=CENTER)
        self.showpasswordbutton.place(relx=0.73, rely=0.3, anchor=CENTER)
        self.showconfirmpasswordbutton.place(relx=0.73, rely=0.4, anchor=CENTER)
        self.goback_button.place(relx=0.713, rely=0.65, anchor=CENTER)
        #change x back to 0.92
        #16
        #-----------------------------------------------------------------------------------------------------------------------
        #-----------------------------------------------------------------------------------------------------------------------
        #-----------------------------------------------------------------------------------------------------------------------
        #-----------------------------------------------------------------------------------------------------------------------

        #WIDGETS loggin_frame
        #Labels
        self.label_user = Label(self.loggin_frame, text='User:', font='Arial 40')
        self.label_password = Label(self.loggin_frame, text='Password:', justify="right", font='Arial 40')
        #-----------------------------------------------------------------------------------------------------------------------
        #Entries
        self.user_entry_loggin = Entry(self.loggin_frame, font='Arial 40')
        self.password_entry_loggin = Entry(self.loggin_frame, show="*", font='Arial 40')
        #-----------------------------------------------------------------------------------------------------------------------
        #Buttons
        self.loggin_button = Button(self.loggin_frame, text='Loggin', font='Arial 40', command=lambda: loggin_attempt(mainwindow,self.user_entry_loggin, self.password_entry_loggin))
        self.goback_button = Button(self.loggin_frame,  text='Go Back', font='Arial 40', command=lambda: show(self.menu_frame, self.user_entry_loggin, self.password_entry_loggin))
        ab(self.loggin_button)
        ab(self.goback_button)
        #-----------------------------------------------------------------------------------------------------------------------
        #Checkbutton
        self.cloggin_var = IntVar()
        self.showpasswordbuttonlogin = Button(self.loggin_frame, image=showingimg, command=lambda:changeImage(self.showpasswordbuttonlogin, self.password_entry_loggin))
        #-----------------------------------------------------------------------------------------------------------------------
        #Checkbutton(self.loggin_frame,font="Arial 15", text="Show Password", width=20,height=20, variable=self.cloggin_var, onvalue=1, offvalue=0, command=lambda:showPassword(self.password_entry_loggin, self.cloggin_var))
        #LAYOUT loggin_frame     
        self.loggin_frame['width'] = self.width
        self.loggin_frame['height'] = self.height

        self.label_user.place(relx=0.25, rely=0.3, anchor=CENTER)
        self.label_password.place(relx=0.210, rely=0.5, anchor=CENTER)
        self.user_entry_loggin.place(relx=0.55, rely=0.3, anchor=CENTER)
        self.password_entry_loggin.place(relx=0.55, rely=0.5, anchor=CENTER)
        self.loggin_button.place(relx=0.5, rely=0.65, anchor=CENTER)
        self.showpasswordbuttonlogin.place(relx=0.920, rely=0.65, anchor=CENTER)
        self.goback_button.place(relx=0.713, rely=0.65, anchor=CENTER)
        #---------------------------------------------------------------------------------------------------------------------------
        #starting application
        #(relx=0.920, rely=0.65, anchor=CENTER
        

        #-------------------------------------------------------------------------------------
        #GUI
        self.menu_frame.grid(row=0, column=0, sticky="nsew")
        self.register_frame.grid(row=0, column=0, sticky="nsew")
        self.loggin_frame.grid(row=0, column=0, sticky="nsew")
        

        show(self.menu_frame)

        self.mainwindow.mainloop() 
        


if __name__ == "__main__":
    app()