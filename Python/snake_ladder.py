# create a game for two player who will reach to 100 first 
p1 = 0
p2 = 0
import os
import random as rd
for i in range(1,101):
    os.system('cls')
    print(f'Round = {i}')
    a = input('P1 : Enter any to roll the Dice')
    pp1 = rd.randint(1,6)
    print(f'Current P1 point = {pp1}')
    if p1+pp1 <=100:
        p1+=pp1
        #print(f'P1 Score = {p1}')
        if p1==80:
            p1=12
            print(f'Snake Bite go to  = {p1}')
        elif p1==15:
            p1=75
            print(f'Got the LADDER go to  = {p1}')
        elif p1==100:
            print(f'P1 Score = {p1}')
            print('Player P1 Wins')
            a = input('---- Press any Key to Exit ----')
            break
    print(f'P1 Score = {p1}')  
    pp2 = rd.randint(1,6)
    a = input('P2 : Enter any to roll the Dice')
    print(f'Current P2 point = {pp2}')
    if p2+pp2 <=100:
        p2+=pp2
        
        if p2==80:
            p2=12
            print(f'Snake Bite go to  = {p2}')
        elif p2==15:
            p2=75
            print(f'Got the LADDER go to  = {p2}')
        elif p2==100:
            print(f'P2 Score = {p2}')
            print('Player P2 Wins')
            a = input('---- Press any Key to Exit ----')
            break
    print(f'P2 Score = {p2}')
    a = input('----NEXT ROUND----')