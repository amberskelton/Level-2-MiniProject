# the following program is a simple multichoice quiz to help you decide which breed of cat/dog to get

import v2Functions#to access functions from the other file containing questions, breeds, and info
import sys#sys.exit() to exit program
print('About this quiz:')
print('The following program is a simple multi-choice quiz to help owners that have difficulty deciding which breed of cat/dog to get!')
print('This quiz will find a breed that is suitable to your physical and behavioural preferences.')
print('Please note that the questions asked are based on generalised breed traits and that individual pets may differ!')
print('Also, please remember to research more about your suggested breed to ensure you are confident and know the correct requirements to meet its needs.')

while True:#outer loop allowing quiz to restart
    while True:#loop that continues until condition is met to catch errors and invalid input
        print('---------------------------------------')
        print('Do you want a cat or a dog?')
        print('\nOptions:')
        print('1. Cat\n2. Dog')
        answer=input('Enter your answer: ')
        if answer=='1':
            print('---------------------------------------')
            score=v2Functions.catPicked()#calls function from v2Functions for cat questions
            breed=v2Functions.catBreed(score)#calls function from v2Functions to align user score with cat breed
            result=v2Functions.descCat(breed)#calls function from v2Functions for selected cat breed description
            print(result)
            break#ends inner loop
        elif answer=='2':
            print('---------------------------------------')
            score=v2Functions.dogPicked()#calls function from v2Functions for dog questions
            breed=v2Functions.dogBreed(score)#calls function from v2Functions to align user score with dog breed
            result=v2Functions.descDog(breed)#calls function from v2Functions for selected dog breed description
            print(result)
            break#ends inner loop
        else:#handles invalid input from user
            print('---------------------------------------')
            print('Please enter an option, "1" or "2".')
    while True:#retry loop
        print('---------------------------------------')
        print('Do you want to take the quiz again?')
        print('\nOptions:')
        print('1. Yes\n2. No')
        answer=input('Enter your answer: ')
        if answer=='1':
            break #restarts outer loop
        elif answer=='2':
            print('---------------------------------------')
            print('Thank you for using the quiz!')
            sys.exit()
        else:#handles invalid input from user
            print('---------------------------------------')
            print('Please enter an option, "1" or "2".')
