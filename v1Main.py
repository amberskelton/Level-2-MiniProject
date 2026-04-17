# the following program is a simple multichoice quiz to help you decide which breed of cat/dog to get

import v1Functions
import sys
print('Instructions')

while True:
    print('---------------------------------------')
    print('Do you want a cat or a dog?')
    print('\nOptions:')
    print('1. Cat\n2. Dog')
    answer=input('Enter your answer: ')
    if answer=='1':
        print('---------------------------------------')
        v1Functions.catPicked()
        break
    elif answer=='2':
        print('---------------------------------------')
        v1Functions.dogPicked()
        break
    else:
        print('---------------------------------------')
        print('Please enter "dog" or "cat".')
