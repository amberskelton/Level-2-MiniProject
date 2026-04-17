# the following program is a simple multichoice quiz to help you decide which breed of cat/dog to get

import Functions1
import sys
print('Instructions')

while True:
    print('---------------------------------------')
    print('Do you want a cat or a dog?')
    print('\nOptions:')
    print('1. Cat\n2. Dog')
    answer=input('Enter your answer: ')
    if answer=='Cat'.lower():
        print('---------------------------------------')
        Functions1.catPicked()
        break
    elif answer=='Dog'.lower():
        print('---------------------------------------')
        Functions1.dogPicked()
        break
    else:
        print('---------------------------------------')
        print('Please enter "dog" or "cat".')
