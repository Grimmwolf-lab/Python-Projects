import random

passlen =int(input("Please enter the length of the password:"))

s = 'abcdefghijklmnopqrstuvwxyz0123456789!@#$%^&*~ABCDEFGHIJKLMNOPQRSTUVWXYZ'

p = "".join(random.sample(s, passlen))

print(p)