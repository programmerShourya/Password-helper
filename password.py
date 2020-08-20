
import random

chars = 'abcdefghijklmnopqrstuxyz1234567890ABCDEFGHIJKLMNOPQRSTUVXYZ!@#$%^&*-~:;"".,><}{][|'

sh = input('no. of passwords')
sh = int(sh)

go = input('password legnth')
go = int(go)

for s in range(sh):
    password = ''
    for a in range(go):
        password += random.choice(chars)
    print(password)
