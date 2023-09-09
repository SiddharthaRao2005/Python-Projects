import random
def RuRou():
    print("Welcome to Russian Roulette !!")
    inp=int(input('Choose a number:'))

    no=random.randint(1,5)
    if inp == no:
        print('You won!!!')
    else:
        print('*BOOM* your dead.')
RuRou()