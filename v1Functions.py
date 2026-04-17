# contains functions for the quiz
# function contains questions that each have different values assigned to them that add to score and the sum of these values are all different and correspond to different breeds

import sys
def dogPicked():
    score=0
    while True:
        print('Would you prefer a friendly or more independent dog?')
        print()
        print('Friendly dogs may be very affectionate and require significant attention.')
        print('This type of dog may not be suitable for you if you work long hours and do not have enough time to pay a lot of attention to it.')
        print()
        print('Independent dogs may be more comfortable on their own and may be stubborn and less affectionate.')
        print('This type of dog may not be suitable for you if you want to cuddle or train it.')
        print('\nOptions:')
        print('1. Friendly\n2. Independent\n')
        answer = input('Enter your answer: ')
        if answer=='1':
            score+=1
            break
        elif answer=='2':
            score+=2
            break
        else:
            print('---------------------------------------')
            print('Please enter an option, either "1" or "2".')
        print('---------------------------------------')
    while True:
        print('---------------------------------------')
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
        if answer=='1':
            score+=4
            break
        elif answer=='2':
            score+=8
            break
        else:
            print('---------------------------------------')
            print('Please enter an option, either "1" or "2".')
        print('---------------------------------------')
    while True:
        print('---------------------------------------')
        print('Would you prefer a dog that sheds more but needs less grooming or a dog that sheds less but needs regular grooming?')
        print('\nOptions:')
        print('1. Sheds more, less grooming\n2. Sheds less, more grooming\n')
        answer = input('Enter your answer: ')
        if answer=='1':
            score+=16
            break
        elif answer=='2':
            score+=32
            break
        else:
            print('---------------------------------------')
            print('Please enter an option, either "1" or "2".')
        print('---------------------------------------')
    return score
            
def catPicked():
    score=0
    while True:
        print('Would you prefer a more mellow or active cat?')
        print()
        print('Mellow cats tend to sleep more and relax quite often, and are better suited for a quieter environment.')
        print('This type of cat may not be suitable for you if you want to play often or have a loud environment/children.')
        print()
        print('More active cats tend to be more playful and curious, and need more stimulation.')
        print('This type of cat may not be suitable for you if you dislike disruptions like running around and knocking things over, especially at night.')
        print('\nOptions:')
        print('1. Mellow\n2. Active\n')
        answer = input('Enter your answer: ')
        if answer=='1':
            score+=1
            break
        elif answer=='2':
            score+=2
            break
        else:
            print('---------------------------------------')
            print('Please enter an option, either "1" or "2".')
        print('---------------------------------------')
    while True:
        print('---------------------------------------')
        print('Would you prefer a vocal or less vocal cat?')
        print()
        print('Vocal cats are more expressive, making it easier to understand them.')
        print('However, they can be noisy, especially at night, and can be quite demanding.')
        print()
        print('Less vocal cats are quieter and less communicative.')
        print('They may be harder to understand.')
        print('\nOptions:')
        print('1. Vocal\n2. Less Vocal\n')
        answer = input('Enter your answer: ')
        if answer=='1':
            score+=4
            break
        elif answer=='2':
            score+=8
            break
        else:
            print('---------------------------------------')
            print('Please enter an option, either "1" or "2".')
        print('---------------------------------------')
    while True:
        print('---------------------------------------')
        print('Would you prefer a cat with lower maintenance short hair or higher maintenance long hair?')
        print()
        print('Shorter-haired cats tend to be sleek.')
        print('When shorter-haired cats shed, more fur may fall out rather than sticking to the coat, ending up around your home, but they usually require less brushing.')
        print()
        print('Longer-haired cats tend to be more fluffy.')
        print('When longer-haired cats shed, more fur sticks to its coat than falling off, causing matting if not regularly brushed. Long hair that does fall out can also be more noticeable.')
        print('\nOptions:')
        print('1. Lower maintenance, little brushing\n2. Higher maintenance, more brushing\n')
        answer = input('Enter your answer: ')
        if answer=='1':
            score+=16
            break
        elif answer=='2':
            score+=32
            break
        else:
            print('---------------------------------------')
            print('Please enter an option, either "1" or "2".')
        print('---------------------------------------')
    return score

def catBreed(score):
    if score==21:
        return 'British Short Hair'
    elif score==37:
        return 'Ragdoll'
    elif score==25:
        return 'Russian Blue'
    elif score==41:
        return 'Persian'
    elif score==22:
        return 'Siamese'
    elif score==38:
        return 'Balinese'
    elif score==26:
        return 'Bengal'
    elif score==42:
        return 'Norwegian Forest Cat'
