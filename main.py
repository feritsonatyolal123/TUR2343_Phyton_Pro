import random
harfler = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"


F = int(input("Parolan Ne Kadar Uzun Olsun"))

password = ""

for i in range(F):
    password += random.choice(harfler)

print(password)

