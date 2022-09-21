import random

def f1():

    n="ROCK PAPER SCISSORS"
    print(n.center(100))

    #User's choice

    x = str(input('''Enter the tool you choose 
                    1.Rock 2.Paper 3.Scissors:\n'''))
    if x == '1':
        a = 'Rock'
    elif x == '2':
        a = 'Paper'
    elif x == '3':
        a = 'Scissors'
    else:
        print('Don\'t act dumb! Choose a number corresponding to the tool')
        f1()

    #Computer's choice

    list1 = ['Rock','Paper','Scissors']    
    b = random.choice(list1)

    print(f'You chose {a} and my choice is {b}')

    #Conditional Programming

    if a == 'Rock' and b == 'Paper':
        print(f'You lose! {b} beats {a}!')
    elif a == 'Rock' and b == 'Scissors':
        print(f'Huh! You won. {a} beats {b}')
    elif a == 'Paper' and b == 'Rock':
        print(f'Huh! You won. {a} beats {b}')
    elif a == 'Paper' and b == 'Scissors':
        print(f'You lose! {b} beats {a}!') 
    elif a == 'Scissors' and b == 'Rock':
        print(f'You lose! {b} beats {a}!')
    elif a == 'Scissors' and b == 'Paper':
        print(f'Huh! You won. {a} beats {b}')
    else:
        print('It\'s a tie. It will be my victory next time!')    

    z= input('Wanna play again? Press Y or just hit enter if you\'re ready to lose:\n').lower()

    if z == 'y' or z == '':
        print('Alrighty! Here we go!')
        f1()
    else:
        print('Oh alright! See you next time!') 
        exit()    

f1()