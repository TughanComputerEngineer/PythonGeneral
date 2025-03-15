import random as rd
import tkinter 
import numpy as np
import time

koyumor = "#0D0A11"
gri = "#1A1A1A"

gelis = 0
radios = 0

form = tkinter.Tk() # Tk() class ını çağırır

form.title("Python Tkinter") # pencerenin başlığını belirler

form.geometry("500x350+720+350")
# form.minsize(400,300) # en küçük boyutu belirler
# form.maxsize(1000,700)  en büyük boyutu belirler
form.resizable(False,False) # pencerenin boyutunu değiştirmeyi engeller

form.state("normal") # pencerenin açılışını belirler. iconic = ikon / normal / zoomed = tam ekran 
form.wm_attributes("-alpha",1) # pencerenin saydamlığını ayarlar

etiket1 = tkinter.Label( form, text="Tus Kontrol: " , fg="white", bg=gri )
etiket1.place(width=500,height=20,relx=0.0,rely=0.001)

etiket2 = tkinter.Label(form, text="Bir Tusa Basin...", fg="white",bg="black" , font="Times 18 bold")
etiket2.place(width=500,height=60,relx=0.0,rely=0.055)

def solts():
    etiket2.config(text="Sol tusa basildi")
    print("sol")

def sagts():
    etiket2.config(text="Sag tusa basildi")
    print("sag")

soltus = tkinter.Button(form, text="Sol Tus", fg="white" , bg=gri , border=0 , command = solts)
soltus.place(width=70,height=30,relx=0.68,rely=0.87)

sagtus = tkinter.Button(form, text="Sag Tus", fg="white" , bg=gri ,border=0 , command = sagts)
sagtus.place(width=70,height=30,relx=0.83,rely=0.87)

def temiz():
    etiket2.config(text="Temizlendi \nBir Tusa Basiniz...")

temizle = tkinter.Button(form, text="Temizle", fg="white" , bg=gri ,border=0 , command = temiz)
temizle.place(width=70,height=30,relx=0.83,rely=0.77)

liste = np.zeros(5).astype(int)

def sayicek():
    global liste
    for i in range(0,5):
        liste[i] = rd.randint(0,100)
    global count
    count = 0
    etiket2.config(text="Sayi cekildi")

rdnumber = tkinter.Button(form,text="Sayi cek.",bg=gri, fg="white",border=0,command=sayicek)
rdnumber.place(width=100,height=40,relx=0.24,rely=0.72)

def shownumber():
    global gelis
    if(gelis==0):
        global count 
        global liste
        if(liste[0]!=liste[1] and liste[1]!=liste[2] and liste[2]!=liste[3] and liste[3]!=liste[4]):
            if(count<5):
                etiket2.config(text=liste[count])
                print(f"Sayi: {liste[count]}")
                count += 1
            elif(count==5):
                etiket2.config(text="Sayilar Bitti \nLutfen sayi cekiniz")
                print("Sayilar bitti")
        else:
            etiket2.config(text="Lutfen once sayi cekiniz")
    else:
        etiket2.config(text=liste[int(y.get())])

shownum = tkinter.Button(form, text="Sayi Goster", fg="white", bg=gri , border=0 , command = shownumber)
shownum.place(width=100,height=40,relx=0.24,rely=0.85)

sayit=0
def fulscreen():
    global sayit
    if(sayit%2==0):
        form.state("zoomed")
        etiket2.config(text="Tam Ekrana Gecildi")
        sayit = 1
    else:
        form.state("normal")
        etiket2.config(text="Tam Ekrandan Cikildi")
        sayit = 0

tamekran = tkinter.Button(form, text="Tam Ekran", fg="white", bg=gri, border=0 , command = fulscreen)
tamekran.place(width=100,height=40,relx=0.03,rely=0.72)

sayis=0
def saydam():
    global sayis
    if(sayis==0):
        form.wm_attributes("-alpha",0.8)
        etiket2.config(text="Opaklik %80")
        sayis=1
    elif(sayis==1):
        form.wm_attributes("-alpha",0.4)
        etiket2.config(text="Opaklik %40")
        sayis=2
    else:
        form.wm_attributes("-alpha",1)
        etiket2.config(text="Opak")
        sayis=0


saydamlas = tkinter.Button(form, text="Saydamlastir", fg="white", bg=gri, border=0 , command = saydam)
saydamlas.place(width=100,height=40,relx=0.03,rely=0.85)

giris1 = tkinter.Entry()
giris1.place(width=200,height=25,relx=0.16,rely=0.3)
giris1.config(bg=gri,fg="white",border=0,insertbackground="white")

def veriyaz():
    yazi = giris1.get()
    if("/color=" in yazi):
        yaz = yazi.split("=")
        etiket2.config(fg=yaz[1],text="Yazi Rengi Degistirildi")
    else:
        etiket2.config(text=yazi)
    giris1.delete(0,"end")

girisb = tkinter.Button(form, text="Veriyi Yaz",bg=gri , fg="white", border=0, command=veriyaz)
girisb.place(width=70,height=25,relx=0.707,rely=0.3)

shaw = 0
def gizle():
    global shaw
    if(shaw==0):
        giris1.config(show="*")
        shaw=1
    else:
        giris1.config(show="")
        shaw=0

showhide = tkinter.Button(form, text="Gizle/Goster",bg=gri,fg="white",border=0,command=gizle)
showhide.place(width=70,height=25,relx=0.563,rely=0.3)

regloc = 0

def silici():
    girisk.delete(0,"end")
    giriss1.delete(0,"end")
    giriss2.delete(0,"end")

sil = tkinter.Button(form, text="Sil",bg=gri,fg="white",border=0,command=silici)

def kapatt():
    global regloc
    girisk.place_forget()
    giriss1.place_forget()
    giriss2.place_forget()
    sil.place_forget()
    kullanici.place_forget()
    sifr1.place_forget()
    sifr2.place_forget()
    regloc=0
    kapat.place_forget()

kapat = tkinter.Button(form, text="Kapat",bg=gri,fg="white",border=0,command=kapatt)

girisk = tkinter.Entry()
giriss1 = tkinter.Entry()
giriss2 = tkinter.Entry()
kullanici = tkinter.Label(form,text="UserName:",bg=gri,fg="white")
sifr1 = tkinter.Label(form,text="Sifre:           ",bg=gri,fg="white")
sifr2 = tkinter.Label(form,text="Sifre:           ",bg=gri,fg="white")

def registr():
    global regloc
    if(regloc==0):
        girisk.place(width=200,height=25,relx=0.303,rely=0.376)
        girisk.config(fg="white",bg=gri,border=0,insertbackground="white")
        giriss1.place(width=200,height=25,relx=0.303,rely=0.45)
        giriss1.config(fg="white",bg=gri,border=0,insertbackground="white")
        giriss2.place(width=200,height=25,relx=0.303,rely=0.525)
        giriss2.config(fg="white",bg=gri,border=0,insertbackground="white")
        sil.place(width=70,height=25,relx=0.707,rely=0.45)
        kapat.place(width=70,height=25,relx=0.707,rely=0.525)
        kullanici.place(width=72,height=25,relx=0.16,rely=0.376)
        sifr1.place(width=72,height=25,relx=0.16,rely=0.45)
        sifr2.place(width=72,height=25,relx=0.16,rely=0.525)
        regloc=1
    elif(regloc==1):
        username = girisk.get()
        sifre1 = giriss1.get()
        sifre2 = giriss2.get()
        if((len(username)>8 and len(username)<25) and (sifre1 == sifre2) and (len(sifre1)>8)):
            etiket2.config(text="Basariyla Kayit Yapildi")
            girisk.delete(0,"end")
            giriss1.delete(0,"end")
            giriss2.delete(0,"end")
            regloc=2
        else:
            etiket2.config(text="Kayit Yapilamadi")
            regloc=1
    else:
        girisk.place_forget()
        giriss1.place_forget()
        giriss2.place_forget()
        sil.place_forget()
        kapat.place_forget()
        kullanici.place_forget()
        sifr1.place_forget()
        sifr2.place_forget()
        regloc=0


kaydol = tkinter.Button(form, text="Kaydol",bg=gri,fg="white", border=0, command=registr)
kaydol.place(width=70,height=25,relx=0.707,rely=0.377)

def gelisms():
    global gelis
    if(x.get()==0):
        gelis = 0
        radio1.place_forget()
        radio2.place_forget()
        radio3.place_forget()
        radio4.place_forget()
        radio5.place_forget()
    else:
        gelis = 1
        radio1.place(width=50,height=25,relx=0.45,rely=0.63)
        radio2.place(width=50,height=25,relx=0.45,rely=0.7)
        radio3.place(width=50,height=25,relx=0.45,rely=0.77)
        radio4.place(width=50,height=25,relx=0.55,rely=0.63)
        radio5.place(width=50,height=25,relx=0.55,rely=0.7)


x = tkinter.IntVar()
x.set(0)
gelismis = tkinter.Checkbutton(form,text="Gelismis",bg=gri,fg="white",border=0,variable=x,indicatoron=0,selectcolor="black",command=gelisms)
gelismis.place(width=100,height=40,relx=0.45,rely=0.85)

y = tkinter.StringVar()
y.set(0)
radio1 = tkinter.Radiobutton(form,text="Sayi1",bg=gri,fg="white",value=0,selectcolor="black",variable=y)
radio2 = tkinter.Radiobutton(form,text="Sayi2",bg=gri,fg="white",value=1,selectcolor="black",variable=y)
radio3 = tkinter.Radiobutton(form,text="Sayi3",bg=gri,fg="white",value=2,selectcolor="black",variable=y)
radio4 = tkinter.Radiobutton(form,text="Sayi4",bg=gri,fg="white",value=3,selectcolor="black",variable=y)
radio5 = tkinter.Radiobutton(form,text="Sayi5",bg=gri,fg="white",value=4,selectcolor="black",variable=y)

form.config(bg=koyumor)
form.mainloop() # pencerenin sürekli açık kalmasını sağlar