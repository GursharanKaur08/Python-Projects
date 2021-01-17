# We want random number in b/w 1 and 6, condition provided is that 1 and 6 should be included.

import random
print('|---Welcome to dice stimulator---|')
while True:
    dice_number = random.randint(1,6)

    if dice_number == 1:
        print('-----------')
        print('|         |')
        print('|    o    |')
        print('|         |')
        print('-----------')
    elif dice_number == 2:
        print('-----------')
        print('|o        |')
        print('|         |')
        print('|        o|')
        print('-----------')
    elif dice_number == 3:
        print('-----------')
        print('|o        |')
        print('|    o    |')
        print('|        o|')
        print('-----------')
    elif dice_number == 4:
        print('-----------')
        print('|o       o|')
        print('|         |')
        print('|o       o|')
        print('-----------')
    elif dice_number == 5:
        print('-----------')
        print('|o       o|')
        print('|    o    |')
        print('|o       o|')
        print('-----------')
    elif dice_number == 6:
        print('-----------')
        print('|o       o|')
        print('|o       o|')
        print('|o       o|')
        print('-----------')
    enter = input("$$$---Enter Y/n for continue/stop rolling the dice---$$$\n")
    enter = enter.upper()
    if enter != 'Y':
        break
