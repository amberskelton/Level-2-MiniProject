# contains functions for the quiz

import sys
global score
score=0
def dogPicked():
    while True:
        print('Would you prefer a friendly or more independent dog?')
        print()
        print('Friendly dogs tend to be very affectionate and require significant attention.')
        print('This type of dog may not be suitable for you if you work long hours and do not have enough time to pay a lot of attention to it.')
        print()
        print('Independent dogs tend to be more comfortable on their own and can be quite stubborn and less affectionate.')
        print('This type of dog may not be suitable for you if you want to cuddle or train it.')
        print('\nOptions:')
        print('1. Friendly\n2. Independent\n')
        answer = input('Enter your answer: ')
        if answer=='1'.lower():
            print('okie dokie')
            score+=1
            break
        elif answer=='2'.lower():
            print('okie dookie')
            score+=2
            break
        else:
            print('---------------------------------------')
            print('Please type either "1" or "2".')
        print('---------------------------------------')
    while True:
        print('Would you prefer a smaller or larger dog?')
        print()
        print('Smaller dogs are good for smaller living spaces and tend to live longer.')
        print('However, they tend to be more energetic and noisy and more likely to get injured.')
        print()
        print('Larger dogs are good for protection and better for being active.')
        print('However, they take up more space and cost more to own.')
        print('\nOptions:')
        print('1. Smaller\n2. Larger\n')
        answer = input('Enter your answer: ')
        if answer=='1'.lower():
            print('okie dokie')
            score+=4
            break
        elif answer=='2'.lower():
            print('okie dookie')
            score+=8
            break
        else:
            print('---------------------------------------')
            print('Please type either "1" or "2".')
        print('---------------------------------------')
    while True:
        print('Would you prefer a dog that sheds more but needs less grooming or a dog that sheds less but needs regular grooming?')
        print('\nOptions:')
        print('1. Sheds more, less grooming\n2. Sheds less, more grooming\n')
        answer = input('Enter your answer: ')
        if answer=='1'.lower():
            print('okie dokie')
            score+=16
            break
        elif answer=='2'.lower():
            print('okie dookie')
            score+=32
            break
        else:
            print('---------------------------------------')
            print('Please type either "1" or "2".')
        print('---------------------------------------')
            
def catPicked():
