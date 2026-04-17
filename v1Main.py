# the following program is a simple multichoice quiz to help you decide which breed of cat/dog to get

import v1Functions
import sys
print('About this quiz:')
print('The following program is a simple multi-choice quiz to help owners that have difficulty deciding which breed of cat/dog to get!')
print('This quiz will find a breed that is suitable to your physical and behavioural preferences.')
print('Please note that the questions asked are based on generalised breed traits and that individual pets may differ!')
print('Also, please remember to research more about your suggested breed to ensure you are confident and know the correct requirements to meet its needs.')

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
        print(result)
        break
    elif answer=='2':
        print('---------------------------------------')
        score=v1Functions.dogPicked()
        breed=v1Functions.dogBreed(score)
        result=v1Functions.descDog(breed)
        print(result)
        break
    else:
        print('---------------------------------------')
        print('Please enter an option, "1" or "2".')
