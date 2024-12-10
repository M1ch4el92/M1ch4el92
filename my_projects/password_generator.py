"""Password_generator"""

import random

my_password = ''

letter = 'qwertyuiopasdfghjklzxcvbnm'
cap_letter = 'QWERTYUIOPASDFGHJKLZXCVBNM'
numbers = '1234567890'
symbols = '~!@#$%^&*()_+=-№\/'

for l in range(int(input("Welcome to password generator!\nHow much letters you want in your password?\n"))):
    my_password = my_password + random.choice(letter)

for cl in range(int(input("How much capital letters you want in your password?\n"))):
    my_password = my_password + random.choice(cap_letter)

for n in range(int(input("How much numbers you want in your password?\n"))):
    my_password = my_password + random.choice(numbers)
   
for s in range(int(input("How much symbols you want in your password?\n"))):
    my_password = my_password + random.choice(symbols)

my_password = list(my_password) #преобразуем строку в список

random.shuffle(my_password) #перемешиваем пароль

my_password = ''.join(my_password) #возвращаем в виде строки

print(f'Your password is: {my_password}')
