import random

print('\n\t   --^--Welcome--^--')
print('\t__Rock__Paper__Scissor__')
print('\nRules : ')
print(' * Rock beats Scissor.')
print(' * Scissor beats Paper.')
print(' * Paper beats Rock.')

print('\n** Keys **')
print('-- Rock : R')
print('-- Paper : P')
print('-- Scissor : S')

name = input('Enter your name : ')


'''
1 : R
2 : P
3 : S
'''
l = [1,2,3]
comp_key = {'1':'Rock','2':'Paper','3':'Scissor'}
user_key = {'r':'Rock','R':'rock',
            'p':'Paper','P':'Paper',
            's':'Scissor','S':'Scissor'}

u,com,c = 0,0,0
e = 'y'



while(e == 'y' or e == 'Y'):
    
    comp = random.choice(l)
    user = input('Enter your choice : ')
    
    if(user == 'R' or user == 'r' and comp == 3):
        win = 1
        c += 1
        u += 1
    elif(user == 'S' or user == 's' and comp == 2):
        win = 1
        c += 1
        u += 1
    elif(user == 'P' or user == 'p' and comp == 1):
        win = 1
        c += 1
        u += 1
    elif(user == 'R' or user == 'r' and comp == 1):
        win = 2
        c += 1
    elif(user == 'P' or user == 'p' and comp == 2):
        win = 2
        c += 1
    elif(user == 'S' or user == 's' and comp == 3):
        win = 2
        c += 1
    else:
        win = 0
        c += 1
        com += 1

    print('\n\tYou selected : ',user_key[user])
    print('\tComputer selected : ',comp_key[str(comp)])

    print('\n\t-----------------------')
    if(win == 1):
        print('\tCongrats!!\n\tYou Win...')
        print('\tWinner : ',name)
    elif(win == 2):
        print('\tOops!!')
        print('\tThis one is draw...')
    else:
        print('\tSorry!!\n\tYou Lose...')
        print('\tWinner : Computer')
        print('\tBetter Luck Next Time.')
        
    print('\t-----------------------')
    print('\tNo. of Attempts : ',c)
    print('\t-----------------------')
    e = input('\nWant to play more(y\\n): ')

print('\n\t-----------------------')
print('\tScore Board :')
print('\t ',name,':',u)
print('\t  Computer :',com)
print('\t-----------------------')
if(u>comp):
    print('\tFinal Winner :',name)
else:
    print('\tFinal Winner : Computer')
print('\t-----------------------')
print('\tThanks for Playing...')
print('\t-----------------------')        


