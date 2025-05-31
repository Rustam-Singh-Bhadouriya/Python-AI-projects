import random

charater_list = "abcdefgh,ijklmnopqrstu#$vwxyzABC()DEFGHIJKLMNOPQRSTUVWXYZ1234567890(),#$@"
length = int(input("Enter lenght of password: "))
password=""

for i in range(length):
    password += random.choice(charater_list)
print(password)

with open("Passwords.txt" , 'a') as f:
    f.write(password)

