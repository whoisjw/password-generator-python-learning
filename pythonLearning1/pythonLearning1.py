#password generator<3

import random
import string

def genPwd(n):
    #choose from all letters and numbers
    chars = string.ascii_letters + string.digits
    randPwd = ''.join((random.choice(chars)) for x in range(n))
    return randPwd

print('Password Generator\n\n')

pwdAmount = input('How many passwords would you like to generate?: ')
pwdLen = input('How many characters should each password be?: ')

file = open('passwords.txt', 'a')

for i in range(int(pwdAmount)):
    pwd = genPwd(int(pwdLen))
    file.write(pwd)

