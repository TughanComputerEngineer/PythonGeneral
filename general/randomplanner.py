import random as rd
import numpy as np
import pandas as pd

def derssec():
    dersler = np.array(["Mat2","Lineer Cebir","Fizik2","C Programlama","TurkD2","İng2","Tarih2"])
    ders = ["a","b"]
    p=-1
    i=0
    while(i<2) :
        a = rd.randint(0,len(dersler)-1)
        if(a==p):
            i-=1
        else:
            ders[i] = dersler[a]
            i+=1
        p=a
    return ders

def yazilimsec():
    yazilimlar = np.array(["C","Python","Html/Css/Js","Otonom arac"])
    yazilim = ["a","b"]
    g=-1
    i=0
    while(i<2):
        a = rd.randint(0,len(yazilimlar)-1)
        if(a==g):
            i-=1
        else:
            yazilim[i] = yazilimlar[a]
            i+=1
        g=a
    return yazilim

def kisiselsec():
    kisisel = np.array(["YtLong","YtShort","YtMusic","Freelance","Github","Blog","Websitesi"])
    a = rd.randint(1,len(kisisel))-1
    return kisisel[a]


def odulsec():
    oduller = np.array(["1 bölüm anime","Ets de 1 teslimat","Genshin de 1 görev","30 dk pinterest","Yt de 1 video"])
    a = rd.randint(1,len(oduller))-1
    return oduller[a]

planner=["a","b","c"]
for i in range(0,3):
    data = dict(____Ders__160dk____ = derssec(),___Yazilim_120dk___ = yazilimsec(),___Kisisel__30dk___ = kisiselsec(),________Odul________ = odulsec(),___Odulkatsayisi___ = (rd.randint(10,25)/10))
    planner[i] = pd.DataFrame(data,index=["1.Oncelik","2.Oncelik"])
for i in range(0,3):
    print(f"\n{i+1}. planner: \n{planner[i]}\n")
sec = input("Lutfen bir planner seciniz: ")
print(f"\n\n\n\n\n\n\n{sec}. planner secildi. \n\n\n{planner[int(sec)-1]}\n\n\n\n\n\n\n")