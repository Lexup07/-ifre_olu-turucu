import random

a = ("+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890")
b = int(input("parolanın uzunluğu?"))

sifre = ""

for i in range(b):      
    sifre += random.choice(a)

print(sifre)
