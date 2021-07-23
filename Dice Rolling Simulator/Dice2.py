import random

print('|---Welcome to dice stimulator---|')

while True:
    print(''' 1. Roll the Dice     2. exit''')
    user = int(input("what you want to do\n"))
    if user == 1:
        number = random.randint(1,6)
        print(number)
    else:
        break
    