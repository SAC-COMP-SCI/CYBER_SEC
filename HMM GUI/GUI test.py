from cProfile import label
from struct import pack
import tkinter
from tkinter import *



def Op_Dem_Func():
    global Op_Dem_Func
    win1 = Toplevel(MAIN_PAGE)
    win1.geometry("600x600")
    win1.title("Operation Dementia")
    win1.configure(bg="purple", fg="turquoise")
    win1.resizable(False, False)
    
    win1.mainloop()







def Pecunia_func():
    global Pecunia_func
    win2 = Toplevel(MAIN_PAGE)
    win2.geometry("600x600")
    win2.title("Pecunia Secretum")
    win2.configure(bg="black")
    win2.resizable(False, False)
    
    win2.mainloop()








def Utiligram_Func():
    global Utiligram_Func
    win2 = Toplevel(MAIN_PAGE)
    win2.geometry("600x600")
    win2.title("Pecunia Secretum")
    win2.configure(bg="black")
    win2.resizable(False, False)
    
    win2.mainloop()



def Triple_G_Func():
    global Utiligram_Func
    win3 = Toplevel(MAIN_PAGE)
    win3.geometry("600x600")
    win3.title("Pecunia Secretum")
    Triple_G_L1 = label("Gaslight, Gatekeep, Girlboss")
    win3.configure(bg="Orange", fg="Black")
    win3.resizable(False, False)
    
    win3.mainloop()














MAIN_PAGE = Tk()
MAIN_PAGE.title("Home Made Malware")
MAIN_PAGE.geometry("600x600")
MAIN_PAGE.configure(bg="black")
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

