# contains functions and dictionaries for the quiz
#dictionaries for user score and assigned cat breeds and descriptions of breeds
# function contains questions that each have different values assigned to them that add to score and the sum of these values are all different and correspond to different breeds

#dictionary containing possible sums(user score) and associated cat breeds
catBreeds = {
    21:'British Shorthair',
    37:'Ragdoll',
    25:'Russian Blue',
    41:'Persian',
    22:'Siamese',
    38:'Balinese',
    26:'Abyssinian',
    42:'Norwegian Forest Cat'
}

#dictionary contianing each cat breed and its description
catDesc = {
    'British Shorthair':'A suitable breed for you would be a British Shorthair cat.\nThey tend to be calm and relaxed, not overly vocal but are communicative, and need to be brushed at least once or twice a week.',
    'Ragdoll':'A suitable breed for you would be a Ragdoll cat.\nThey tend to be very laid-back, quite sociable, and have a long, soft coat which needs to be brushed every other day.',
    'Russian Blue':'A suitable breed for you would be a Russian Blue cat.\nThey tend to be very reserved and gentle, and need to be brushed at least once or twice a week.',
    'Persian':'A suitable breed for you would be a Persian cat.\nThey tend to be very calm and quiet, and require daily brushing.',
    'Siamese':'A suitable breed for you would be a Siamese cat.\nThey tend to be highly active, very vocal, and need to be brushed at least once or twice a week.',
    'Balinese':'A suitable breed for you would be a Balinese cat.\nThey tend to be highly active, very vocal, and need to be brushed at least once or twice a week.',
    'Abyssinian':'A suitable breed for you would be an Abyssinian cat.\nThey tend to be very energetic, can be vocal but are more soft-spoken, and need to be brushed at least once or twice a week.',
    'Norwegian Forest Cat':'A suitable breed for you would be a Norwegian Forest Cat.\nThey tend to be very active and enjoy high climbing spaces, not overly vocal and are soft-spoken, and have a long, dense coat which needs to be brushed every other day.'
}

#dictionary containing possible sums(user score) and associated dog breeds
dogBreeds = {
    21:'Pug',
    37:'Maltese',
    25:'Golden Retriever',
    41:'Labradoodle',
    22:'Chihuahua',
    38:'Miniature Schnauzer',
    26:'Siberian Husky',
    42:'Standard Poodle'
}

#dictionary contianing each dog breed and its description
dogDesc = {
    'Pug':'A suitable dog breed for you would be a pug.\nThey tend to be very friendly, small, and need to be brushed 2-3 times a week.',
    'Maltese':'A suitable dog breed for you would be a maltese.\nThey tend to be very friendly, small, and need to be brushed 3-4 times a week.',
    'Golden Retriever':'A suitable dog breed for you would be a golden retriever.\nThey tend to be very friendly, medium to large in size, and need to be brushed 2-3 times a week.',
    'Labradoodle':'A suitable dog breed for you would be a labradoodle.\nThey tend to be very friendly, generally medium in size but can be smaller, and need to be brushed 2-3 times a week.',
    'Chihuahua':'A suitable dog breed for you would be a Chihuahua.\nThey tend to be deeply loyal to their owner and may be defensive against strangers, small, and need to be brushed at least once or twice a week.',
    'Miniature Schnauzer':'A suitable dog breed for you would be a Miniature Schnauzer.\nThey tend to be friendly but more alert and stubborn, small, and need to be brushed daily or at least twice a week.',
    'Siberian Husky':'A suitable dog breed for you would be a Siberian Husky.\nThey tend to be friendly but independent, medium in size, and need to be brushed once or twice a week but daily during shedding season.',
    'Standard Poodle':'A suitable dog breed for you would be a Standard Poodle.\nThey tend to be quite independent, intelligent, and can be aloof with strangers, medium to large in size, and need to be brushed daily.'
}

def askQuestion(question,opt1,opt2,score1,score2):#asks a multiple-choice question and returns the score value based on user input and ensures only valid options are accepted
    while True:
        print(question)
        print('\nOptions:')
        print(f'1. {opt1}')
        print(f'2. {opt2}')
        answer=input('Enter your answer: ')
        if answer=='1':
            print('---------------------------------------')
            return score1
        elif answer=='2':
            print('---------------------------------------')
            return score2
        else:
            print('---------------------------------------')
            print('Please enter an option, either "1" or "2".')
            print('---------------------------------------')

def dogPicked():#asks all dog questions and calculates total score based on answers
    score=0
    score+=askQuestion(
        'Would you prefer a friendly or more independent dog?\n\n'
        'Friendly dogs may be very affectionate and require significant attention.\n'
        'This type of dog may not be suitable for you if you work long hours and do not have enough time to pay a lot of attention to it.\n'
        'Independent dogs may be more comfortable on their own and may be stubborn and less affectionate.\n'
        'This type of dog may not be suitable for you if you want to cuddle or train it.',
        'Friendly', 'Independent',1,2
    )
    score+=askQuestion(
        'Would you prefer a smaller or larger dog?\n\n'
        'Smaller dogs are good for smaller living spaces and tend to live longer.\n'
        'However, they tend to be more energetic and noisy and more likely to get injured.\n'
        'Larger dogs are good for protection and better for being active.\n'
        'However, they take up more space and cost more to own.',
        'Smaller', 'Larger',4,8
    )
    score+=askQuestion(
        'Would you prefer a dog that sheds more but needs less grooming or a dog that sheds less but needs regular grooming?\n\n',
        'More shedding, less grooming', 'Less shedding, more grooming',16,32
    )
    return score

def catPicked():#asks all cat questions and calculates total score based on answers
    score=0
    score+=askQuestion(
        'Would you prefer a more mellow or active cat?\n\n'
        'Mellow cats tend to sleep more and relax quite often, and are better suited for a quieter environment.\n'
        'This type of cat may not be suitable for you if you want to play often or have a loud environment/children.\n'
        'More active cats tend to be more playful and curious, and need more stimulation.\n'
        'This type of cat may not be suitable for you if you dislike disruptions like running around and knocking things over, especially at night.',
        'Mellow', 'Active',1,2
    )
    score+=askQuestion(
        'Would you prefer a vocal or less vocal cat?\n\n'
        'Vocal cats are more expressive, making it easier to understand them.\n'
        'However, they can be noisy, especially at night, and can be quite demanding.\n'
        'Less vocal cats are quieter and less communicative.\n'
        'They may be harder to understand.',
        'Vocal', 'Less Vocal',4,8
    )
    score+=askQuestion(
        'Would you prefer a cat with lower maintenance short hair or higher maintenance long hair?\n\n'
        'Shorter-haired cats tend to be sleek.\n'
        'When shorter-haired cats shed, more fur may fall out rather than sticking to the coat, ending up around your home, but they usually require less brushing.\n'
        'Longer-haired cats tend to be more fluffy.\n'
        'When longer-haired cats shed, more fur sticks to its coat than falling off, causing matting if not regularly brushed. Long hair that does fall out can also be more noticeable.',
        'Lower maintenance, little brushing', 'Higher maintenance, more brushing',16,32
    )
    return score

def catBreed(score):#returns the cat breed that matches the user's score
    return catBreeds.get(score)

def descCat(breed):#returns the description for the selected cat breed
    return catDesc.get(breed)

def dogBreed(score):#returns the dog breed that matches the user's score
    return dogBreeds.get(score)

def descDog(breed):#returns the description for the selected dog breed
    return dogDesc.get(breed)
