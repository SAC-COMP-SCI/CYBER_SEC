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
    
    win5.mainloop()


def Op_Dem_Func():
    global Op_Dem_Func
    global win1
    win1 = Toplevel(MAIN_PAGE)
    win1.geometry("600x600")
    win1.configure(bg="purple",)
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
    win4.configure(bg="Orange", fg="Black")
    win4.resizable(False, False)
    win4.title("Pecunia Secretum")
    win4 = label("Gaslight, Gatekeep, Girlboss")
    
    
    win4.mainloop()














MAIN_PAGE = Tk()
MAIN_PAGE.title("Home Made Malware")
MAIN_PAGE.geometry("600x600")
MAIN_PAGE.configure(bg="grey")
MAIN_PAGE.resizable(False, False)
Operation_Dementia = Button(MAIN_PAGE, text="Operation Dementia", command=Op_Dem_Func, bg="Purple", fg="turquoise", font=("Arial", 20))
Pecunia_Secretum = Button(MAIN_PAGE, text="Pecunia Secretum", command=Pecunia_func, bg="Orange", fg="White", font=("Arial", 20))
Utiligram = Button(MAIN_PAGE, text="Utiligram", command=Utiligram_Func, bg="Blue", fg="White", font=("Arial", 20))
Triple_G = Button(MAIN_PAGE, text="Triple G", command=Triple_G_Func, bg="Black", fg="Green", font=("Arial", 20))



Operation_Dementia.pack(pady=20)
Pecunia_Secretum.pack(pady=20)
Utiligram.pack(pady=20)
Triple_G.pack(pady=20)
MAIN_PAGE.mainloop()

