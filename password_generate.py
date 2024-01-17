import random
passlen = int(input("input the lenght of password: "))
s = "abcdefghijklmnopqrstwxyz01234567890ABCDEFGHIJKLMNOPQRSTWXYZ!@#$%^&8()"
p = "".join(random.sample(s,passlen))
print(p)
