import random as rd

def end():
    print("21 i gectiniz. Kaybettiniz")

def kartcek():
    puan=0
    cvp="add"
    while(cvp == "add"):
        kart = rd.randint(1,13)
        if(kart==1):
            print("Kartiniz: Ace")
            if(puan+kart<=21):
                kart2 = 11
            else:
                kart2 = 1
        elif(kart==11):
            print("Kartiniz: Joker")
            kart2 = 10
        elif(kart==12):
            print("Kartiniz: Queen")
            kart2 = 10
        elif(kart==13):
            print("Kartiniz: King")
            kart2 = 10
        else:
            print(f"Kartiniz: {kart}")
            kart2 = kart
        puan+=kart2
        if(puan > 21):
            end()
            return "break"
        else:
            print(f"Oyuncu: {puan}")
            cvp = input("Kart cekmek icin 'add', durmak icin 'call' giriniz: ")
    return puan

def kurpiyer():
    puan2 = 0
    kart = rd.randint(1,13)
    if(kart==1):
        print("Kurpiyer: Ace")
        if(puan2+kart<=21):
            kart2=11
        else:
            kart2=1
    elif(kart==11):
        print("Kurpiyer: Joker")
        kart2 = 10
    elif(kart==12):
        print("Kurpiyer: Queen")
        kart2 = 10
    elif(kart==13):
        print("Kurpiyer: King")
        kart2 = 10
    else:
        print(f"Kurpiyer: {kart}")
        kart2 = kart
    puan2+=kart2
    return puan2   

oyuncu="a"
masa=0
while(oyuncu!="break"):
    print("Kart oyununa hoşgeldiniz.")
    masa += kurpiyer()
    print(f"Masa: {masa}")
    oyuncu = kartcek()
    masa += kurpiyer()
    print(f"Masa: {masa}")
    if(21-masa>21-int(oyuncu)):
        print("Tebrikler!")
    elif(21-int(oyuncu)==21-masa):
        print("Berabere!")
    else:
        end()


