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
        score=v1Functions.catPicked()
        breed=v1Functions.catBreed(score)
        result=v1Functions.descCat(breed)
        print('---------------------------------------')
        print(result)
        break
    elif answer=='2':
        print('---------------------------------------')
        score=v1Functions.dogPicked()
        breed=v1Functions.dogBreed(score)
        result=v1Functions.descDog(breed)
        print('---------------------------------------')
        print(result)
        break
    else:
        print('---------------------------------------')
        print('Please enter an option, "1" or "2".')
