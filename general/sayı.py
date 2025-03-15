import random as rd

sayi = rd.randint(1,100)
print("Lutfen sayiyi tahmin ediniz.")
count = 0

while(True):
    tahmin = int(input())
    if(tahmin==sayi):
        break
    elif(tahmin<sayi):
        print("Daha buyuk bir sayi giriniz.")
        count+=1
    else:
        print("Daha kucuk bir sayi giriniz.")
        count+=1

print(f"Tebrikler! {count+1} denemede bildiniz. \nPuaniniz: {100-count*10}")

