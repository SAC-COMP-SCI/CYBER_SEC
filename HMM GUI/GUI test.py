from cProfile import label
from struct import pack
import tkinter
from tkinter import *



def OPD_INSTALL_FUNC():
    global OPD_INSTALL_FUNC
    win5 = Toplevel(win1)
    win5.geometry("600x600")
    win5.configure(bg="Black")
    win5.title("Operation Dementia")
    win5.resizable(False, False)

    win5_l1 = Label(win5, text="Install Operation Dementia", bg="Black", fg="White", font=("Arial", 20))
    win5_l2 = Label(win5, text="This wont take long!", bg="Black", fg="White", font=("Arial", 20))
    win5_but1 = Button(win5, text="Install", command=OPD_INSTALL_FUNC)

    win5_l1.pack()
    win5_l2.pack()
    win5_but1.pack()
    win5.mainloop()


def Op_Dem_Func():
    global Op_Dem_Func
    global win1
    win1 = Toplevel(MAIN_PAGE)
    win1.geometry("600x600")
    win1.configure(bg="purple")
    win1.title("Operation Dementia")
    win1.resizable(False, False)
    
    win1_l1 = Label(win1, text="Operation Dementia", bg="purple", fg="white", font=("Arial", 20))
    win1_butt1 = Button(win1, text="Download .exe", command=OPD_INSTALL_FUNC)
    win1_t1 = Text(win1, height=10, width=50, bg="blue", font=("Arial", 20))
    win1_t1.insert(INSERT, "Not your Grandpappy's Malware")
    
    win1_l1.pack()
    win1_butt1.pack()
    win1_t1.pack()
    win1.mainloop()







def Pecunia_func():
    global Pecunia_func
    win2 = Toplevel(MAIN_PAGE)
    win2.geometry("600x600")
    win2.configure(bg="black")
    win2.title("Pecunia Secretum")
    win2.resizable(False, False)
    win2.mainloop()








def Utiligram_Func():
    global Utiligram_Func
    win3 = Toplevel(MAIN_PAGE)
    win3.geometry("600x600")
    win3.configure(bg="black")
    win3.title("Pecunia Secretum")
    
    win3.resizable(False, False)
    
    win3.mainloop()



def Triple_G_Func():
    global Triple_G_Func
    win4 = Toplevel(MAIN_PAGE)
    win4.geometry("600x600")
    win4.configure(bg="black")
    win4.resizable(True, True)
    win4.title("Triple G")
    win4_l1 = Label(win4, text="Gaslight, Gatekeep, Girlboss", bg="Black", fg="Green", font=("Roboto Mono", 30))
    win4_l2 = Label(win4, text="Gaslight: To manipulate (someone) by psychological means into questioning their own sanity.", bg="Black", fg="Green", font=("Roboto Mono", 14))
    win4_l3 = Label(win4, text="Gatekeep: To control access to (something) by controlling who is allowed to enter or leave.", bg="Black", fg="Green", font=("Roboto Mono", 14))
    win4_l4 = Label(win4, text="Girlboss: IDK what this means, but it's in the Urban Dictionary.", bg="Black", fg="Green", font=("Roboto Mono", 14))
    win4_l1.pack()
    win4_l2.pack()
    win4_l3.pack()
    win4_l4.pack()
    
    win4.mainloop()




def LogRoller_Func():
    global LogRoller_Func
    win6 = Toplevel(MAIN_PAGE)
    win6.geometry("600x600")
    win6.configure(bg="black")
    win6.title("Log Roller")
    win6.resizable(True, True)
    win6_l1 = Label(win6, text="Log Roller is a lightweight botnet GUI", bg="Black", fg="Green", font=("Roboto Mono", 30))
    win6.mainloop()













MAIN_PAGE = Tk()
MAIN_PAGE.title("Home Made Malware")
MAIN_PAGE.geometry("600x600")
MAIN_PAGE.configure(bg="grey")
MAIN_PAGE.resizable(False, False)
Operation_Dementia = Button(MAIN_PAGE, text="Operation Dementia", command=Op_Dem_Func, bg="Purple", fg="turquoise", font=("Arial", 20))
Pecunia_Secretum = Button(MAIN_PAGE, text="Pecunia Secretum", command=Pecunia_func, bg="Orange", fg="White", font=("Arial", 20))
Utiligram = Button(MAIN_PAGE, text="Utiligram", command=Utiligram_Func, bg="Blue", fg="White", font=("Arial", 20))
Triple_G = Button(MAIN_PAGE, text="Triple G", command=Triple_G_Func, bg="Black", fg="Green", font=("Arial", 20))
LogRolling = Button(MAIN_PAGE, text="Log Rolling", command=Log_Rolling_Func, bg="Black", fg="Green", font=("Arial", 20))




Operation_Dementia.pack(pady=20)
Pecunia_Secretum.pack(pady=20)
Utiligram.pack(pady=20)
Triple_G.pack(pady=20)
MAIN_PAGE.mainloop()

