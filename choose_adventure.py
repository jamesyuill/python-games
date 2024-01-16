name = input('Type your name: ')
print('Welcome', name,"to this adventure!")

answer = input('You are on a dirt road, it has come to an end and you can go left or right. Which way would you like to go?: ').lower()

if answer == 'left':
    answer = input('you come to a river, you can walk around it or swim across, type walk or swim: ').lower()

    if answer == 'swim':
        print('you swam across and were eated by a crocodile')
    elif answer == 'walk':
        print('you walked for many miles and ran out of water, you lost the game')
    else:
        print('not a valid option, you lose')
elif answer == 'right':
    answer = input('You come to a bridge, it looks wobbly, do you want to cross it or head back, cross or back? ')
    if answer == 'back':
        print('you go back to the main road and die, you lose')
    elif answer == 'cross':
        answer = input('you cross the bridge and meet a stranger')
    else:
        print('not a valid option, you lose')
else:
    print('not a valid option, you lose!')