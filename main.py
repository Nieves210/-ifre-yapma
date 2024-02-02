import random

harfler="abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
sayilar="1234567890"
semboller="+-/*!&$#?=@"

uzunluk=int(input("Parolanızın uzunluğunu yazınız:"))


sifre=""

for i in range(uzunluk):

    if i % 3 ==0:
        sifre += random.choice(harfler)
    if i % 3 ==1:
        sifre += random.choice(sayilar)    
    if i % 3 ==2:
        sifre += random.choice(semboller)

print(sifre)
