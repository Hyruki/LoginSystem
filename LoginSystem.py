import customtkinter

#Custom Tkinter Init
customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("green")

#Tkinter Init
win = customtkinter.CTk()
win.geometry("500x350")
win.title("Register")

def menu():

    #=================Login=====================

    def login():

        #Frame gestion
        menulabel.pack_forget()
        framelogin = customtkinter.CTkFrame(master=win)
        framelogin.pack(pady=20, padx=60, fill="both", expand=True)

        #Contenent

        titlelogin = customtkinter.CTkLabel(master=framelogin, text="Login", text_font=("Roboto", 24))
        titlelogin.pack(pady=12, padx=10)

        lentry1 = customtkinter.CTkEntry(master=framelogin, placeholder_text="Username")
        lentry1.pack(pady=12, padx=10)
        lentry2 = customtkinter.CTkEntry(master=framelogin, placeholder_text="Password", show="•")
        lentry2.pack(pady=12, padx=10)

        labelerror = customtkinter.CTkLabel(master=framelogin, text="Username or password is incorrect ! Retry ! ",text_color="red")

        def buttonaction():
            labelerror.pack_forget()
            with open('./datauserlogin/user.txt', 'r+') as userfile:
                if lentry1.get() == userfile.read():
                    with open('./datauserlogin/password.txt', 'r+') as passfile:
                        if lentry2.get() == passfile.read():
                            print("Connect")
                            win.quit()
                        else:
                            labelerror.pack(pady=12, padx=10)
                else:
                    labelerror.pack(pady=12, padx=10)

        def returnmenu():
            framelogin.pack_forget()
            menulabel.pack(pady=20, padx=60, fill="both", expand=True)


        button = customtkinter.CTkButton(master=framelogin, text="Login", command=buttonaction)
        button.pack(pady=12, padx=10)

        menubuttonR = customtkinter.CTkButton(master=framelogin, text="Return Menu", command=returnmenu)
        menubuttonR.pack(pady=12, padx=10)

    #================Register====================

    def register():

        #Frame gestion

        menulabel.pack_forget()
        registerframe = customtkinter.CTkFrame(master=win)
        registerframe.pack(pady=20, padx=60, fill="both", expand=True)

        #Definition

        def registersys():
            if registeruser.get() != "":
                if registerpassword.get() != "":
                    registerframe.pack_forget()
                    menulabel.pack(pady=20, padx=60, fill="both", expand=True)
                    with open('./datauserlogin/user.txt', 'w') as userfile:
                        userfile.write(registeruser.get())
                    with open('./datauserlogin/password.txt', 'w') as passfile:
                        passfile.write(registerpassword.get())
                else:
                    buttonerrorR.pack(pady=12, padx=10)
            else:
                buttonerrorR.pack(pady=12, padx=10)
        def returnmenu():
            registerframe.pack_forget()
            menulabel.pack(pady=20, padx=60, fill="both", expand=True)

        #Contenent

        titleregister = customtkinter.CTkLabel(master=registerframe, text="Register", text_font=("Roboto", 24))
        titleregister.pack(pady=12, padx=10)

        registeruser = customtkinter.CTkEntry(master=registerframe, placeholder_text="Username")
        registeruser.pack(pady=12, padx=10)

        registerpassword = customtkinter.CTkEntry(master=registerframe, placeholder_text="Password", show="•")
        registerpassword.pack(pady=12, padx=10)

        registerbutton = customtkinter.CTkButton(master=registerframe, text="Register", command=registersys)
        registerbutton.pack(pady=12, padx=10)

        menubuttonR = customtkinter.CTkButton(master=registerframe, text="Return Menu", command=returnmenu)
        menubuttonR.pack(pady=12, padx=10)

        buttonerrorR = customtkinter.CTkLabel(master=registerframe, text="You need to type an Username and Password", text_color="red")

    #Menu part

    menulabel = customtkinter.CTkFrame(master=win)
    menulabel.pack(pady=20, padx=60, fill="both", expand=True)

    titlemenu = customtkinter.CTkLabel(master=menulabel, text="Login or Register", text_font=("Roboto", 24))
    titlemenu.pack(pady=12, padx=10)

    loginmenuB = customtkinter.CTkButton(master=menulabel, text="Login", command=login)
    loginmenuB.pack(pady=40, padx=10)

    registermenuB = customtkinter.CTkButton(master=menulabel, text="Register", command=register)
    registermenuB.pack(pady=12, padx=10)

#Launching

menu()

win.mainloop()