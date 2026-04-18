# the following program is a simple multichoice quiz to help you decide which breed of cat/dog to get

import v1Functions #to access functions from the other file containing questions, breeds, and info
print('About this quiz:')
print('The following program is a simple multi-choice quiz to help owners that have difficulty deciding which breed of cat/dog to get!')
print('This quiz will find a breed that is suitable to your physical and behavioural preferences.')
print('Please note that the questions asked are based on generalised breed traits and that individual pets may differ!')
print('Also, please remember to research more about your suggested breed to ensure you are confident and know the correct requirements to meet its needs.')

while True:#loop that continues until condition is met to catch errors and invalid input
    print('---------------------------------------')
    print('Do you want a cat or a dog?')
    print('\nOptions:')
    print('1. Cat\n2. Dog')
    answer=input('Enter your answer: ')#takes and stores user input
    if answer=='1':
        print('---------------------------------------')
        score=v1Functions.catPicked()#calls function from v1Functions for cat questions
        breed=v1Functions.catBreed(score)#calls function from v1Functions to align user score with cat breed
        result=v1Functions.descCat(breed)#calls function from v1Functions for selected cat breed description
        print(result)
        break#ends loop
    elif answer=='2':
        print('---------------------------------------')
        score=v1Functions.dogPicked()#calls function from v1Functions for dog questions
        breed=v1Functions.dogBreed(score)#calls function from v1Functions to align user score with dog breed
        result=v1Functions.descDog(breed)#calls function from v1Functions for selected dog breed description
        print(result)
        break#ends loop
    else:#handles invalid input from user
        print('---------------------------------------')
        print('Please enter an option, "1" or "2".')
