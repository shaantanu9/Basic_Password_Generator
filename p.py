import random as r

az  = "abcdefghijklmnopqrstuvwxyz"
AZ = az.upper()

laz = list(az)

lAZ = list(AZ)

no = "123456789"
lno = list(no)
sym = "!@#$%^&*()_+\{\}?><:"""
lsym = list(sym)

full = laz+lAZ+lno
sfull = laz+lAZ+lno+lsym
i = 0
car = int(input("no of character in password"))
password = ""
username = f"{r.choice(lAZ)}"

while i in range(car):
    nn = r.choice(full)
    username = username+nn
    psw = r.choice(sfull)
    password = password+psw
    i = i+1

    # print(username)
print(f" username is {username}")
print(f"password is  {password}")
