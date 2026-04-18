# contains functions for the quiz
# function contains questions that each have different values assigned to them that add to score and the sum of these values are all different and correspond to different breeds

def dogPicked():#function containing three questions on dogs
    score=0
    while True:#loop that continues until condition is met to catch errors and invalid input
        print('Would you prefer a friendly or more independent dog?')
        print()
        print('Friendly dogs may be very affectionate and require significant attention.')
        print('This type of dog may not be suitable for you if you work long hours and do not have enough time to pay a lot of attention to it.')
        print()
        print('Independent dogs may be more comfortable on their own and may be stubborn and less affectionate.')
        print('This type of dog may not be suitable for you if you want to cuddle or train it.')
        print('\nOptions:')
        print('1. Friendly\n2. Independent\n')
        answer = input('Enter your answer: ')#takes and stores user input
        if answer=='1':
            score+=1#adds to score
            print('---------------------------------------')
            break
        elif answer=='2':
            score+=2
            print('---------------------------------------')
            break
        else:#handles invalid input from user
            print('---------------------------------------')
            print('Please enter an option, either "1" or "2".')
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
        if answer=='1':
            score+=4
            print('---------------------------------------')
            break
        elif answer=='2':
            score+=8
            print('---------------------------------------')
            break
        else:
            print('---------------------------------------')
            print('Please enter an option, either "1" or "2".')
        print('---------------------------------------')
    while True:
        print('Would you prefer a dog that sheds more but needs less grooming or a dog that sheds less but needs regular grooming?')
        print('\nOptions:')
        print('1. Sheds more, less grooming\n2. Sheds less, more grooming\n')
        answer = input('Enter your answer: ')
        if answer=='1':
            score+=16
            print('---------------------------------------')
            break
        elif answer=='2':
            score+=32
            print('---------------------------------------')
            break
        else:
            print('---------------------------------------')
            print('Please enter an option, either "1" or "2".')
        print('---------------------------------------')
    return score#sends result
            
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
            print('---------------------------------------')
            break
        elif answer=='2':
            score+=2
            print('---------------------------------------')
            break
        else:
            print('---------------------------------------')
            print('Please enter an option, either "1" or "2".')
        print('---------------------------------------')
    while True:
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
            print('---------------------------------------')
            break
        elif answer=='2':
            score+=8
            print('---------------------------------------')
            break
        else:
            print('---------------------------------------')
            print('Please enter an option, either "1" or "2".')
        print('---------------------------------------')
    while True:
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
            print('---------------------------------------')
            break
        elif answer=='2':
            score+=32
            print('---------------------------------------')
            break
        else:
            print('---------------------------------------')
            print('Please enter an option, either "1" or "2".')
        print('---------------------------------------')
    return score

def catBreed(score):#function containing if statement that returns different breeds of cats based on different possible sums(user score)
    if score==21:#e.g. if user score is equal to this possibility, assign 'British Shorthair'
        return 'British Shorthair'
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
        return 'Abyssinian'
    elif score==42:
        return 'Norwegian Forest Cat'

def descCat(breed):#functions containing if statement that returns descriptions of cat breeds based on user's suggested cat breed
    if breed=='British Shorthair':
        return 'A suitable breed for you would be a British Shorthair cat.\nThey tend to be calm and relaxed, not overly vocal but are communicative, and need to be brushed at least once or twice a week.'
    elif breed=='Ragdoll':
        return 'A suitable breed for you would be a Ragdoll cat.\nThey tend to be very laid-back, quite sociable, and have a long, soft coat which needs to be brushed every other day.'
    elif breed=='Russian Blue':
        return 'A suitable breed for you would be a Russian Blue cat.\nThey tend to be very reserved and gentle, and need to be brushed at least once or twice a week.'
    elif breed=='Persian':
        return 'A suitable breed for you would be a Persian cat.\nThey tend to be very calm and quiet, and require daily brushing.'
    elif breed=='Siamese':
        return 'A suitable breed for you would be a Siamese cat.\nThey tend to be highly active, very vocal, and need to be brushed at least once or twice a week.'
    elif breed=='Balinese':
        return 'A suitable breed for you would be a Balinese cat.\nThey tend to be highly active, very vocal, and need to be brushed at least once or twice a week.'
    elif breed=='Abyssinian':
        return 'A suitable breed for you would be an Abyssinian cat.\nThey tend to be very energetic, can be vocal but are more soft-spoken, and need to be brushed at least once or twice a week.'
    elif breed=='Norwegian Forest Cat':
        return 'A suitable breed for you would be a Norwegian Forest Cat.\nThey tend to be very active and enjoy high climbing spaces, not overly vocal and are soft-spoken, and have a long, dense coat which needs to be brushed every other day.'

def dogBreed(score):#function containing if statement that returns different breeds of dogs based on different possible sums(user score)
    if score==21:#e.g. if user score is equal to this possibility, assign 'Pug'
        return 'Pug'
    elif score==37:
        return 'Maltese'
    elif score==25:
        return 'Golden Retriever'
    elif score==41:
        return 'Labradoodle'
    elif score==22:
        return 'Chihuahua'
    elif score==38:
        return 'Miniature Schnauzer'
    elif score==26:
        return 'Siberian Husky'
    elif score==42:
        return 'Standard Poodle'

def descDog(breed):#functions containing if statement that returns descriptions of dog breeds based on user's suggested dog breed
    if breed=='Pug':
        return 'A suitable dog breed for you would be a pug.\nThey tend to be very friendly, small, and need to be brushed 2-3 times a week.'
    elif breed=='Maltese':
        return 'A suitable dog breed for you would be a maltese.\nThey tend to be very friendly, small, and need to be brushed 3-4 times a week.'
    elif breed=='Golden Retriever':
        return 'A suitable dog breed for you would be a golden retriever.\nThey tend to be very friendly, medium to large in size, and need to be brushed 2-3 times a week.'
    elif breed=='Labradoodle':
        return 'A suitable dog breed for you would be a labradoodle.\nThey tend to be very friendly, generally medium in size but can be smaller, and need to be brushed 2-3 times a week.'
    elif breed=='Chihuahua':
        return 'A suitable dog breed for you would be a Chihuahua.\nThey tend to be deeply loyal to their owner and may be defensive against strangers, small, and need to be brushed at least once or twice a week.'
    elif breed=='Miniature Schnauzer':
        return 'A suitable dog breed for you would be a Miniature Schnauzer.\nThey tend to be friendly but more alert and stubborn, small, and need to be brushed daily or at least twice a week.'
    elif breed=='Siberian Husky':
        return 'A suitable dog breed for you would be a Siberian Husky.\nThey tend to be friendly but independent, medium in size, and need to be brushed once or twice a week but daily during shedding season.'
    elif breed=='Standard Poodle':
        return 'A suitable dog breed for you would be a Standard Poodle.\nThey tend to be quite independent, intelligent, and can be aloof with strangers, medium to large in size, and need to be brushed daily.'
