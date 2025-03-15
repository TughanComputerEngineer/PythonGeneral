import tkinter as tk
from tkinter.ttk import Combobox 
from tkinter import ttk
import time
# Fonksiyonlar

def yazdir():
    yazi.config(text=x.get())




# Arayüz 
koyumor = "#0D0A11"
gri = "#1A1A1A"

form = tk.Tk()
form.config(bg=koyumor)
form.geometry("500x400+350+250")
form.title("Python Tkinter 2")

yazi = tk.Label(form,bg="black",fg="white",text="Secim yapiniz!")
yazi.place(relx=0.0001,rely=0.02,width=500,height=60)




secmelistyle = ttk.Style()
secmelistyle.theme_create("combostyle",parent="alt",settings={"TCombobox":
                                                              {"configure":
                                                               {"selectbackground": "",
                                                                "fieldbackground": gri,
                                                                "background": gri,
                                                                "arrowcolor": "white"}}})
secmelistyle.theme_use("combostyle")
x = tk.StringVar()
x.set(1)
secenek = ["1","2","3","4","5"]
secmeli = Combobox(form, height=3, values=secenek,state="readonly",textvariable=x)
secmeli.config(justify="center")
secmeli.place(width=100,height=25,relx=0.1,rely=0.25)

yazdirma = tk.Button(form,bg=gri,fg="white",text="Secimi Yazdir",border=0,command=yazdir)
yazdirma.place(width=100,height=25,relx=0.35,rely=0.25)







form.mainloop()
