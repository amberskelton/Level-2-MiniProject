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
    'Norwegian Forest Cat':'A suitable breed for you would be a Norwegian Forest Cat.\nThey tend to be very active and enjoy high climbing spaces, not overly vocal and are soft-spoken,\nand have a long, dense coat which needs to be brushed every other day.'
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

#dictionary containing each cat breed and a photo of it
catPhotos={
    'British Shorthair':'britishshorthair.png',
    'Ragdoll':'ragdoll.png',
    'Russian Blue':'russianblue.png',
    'Persian':'persian.png',
    'Siamese':'siamese.png',
    'Balinese':'balinese.png',
    'Abyssinian':'abyssinian.png',
    'Norwegian Forest Cat':'norwegianforest.png'
}

#dicitonary containing each dog breed and a photo of it
dogPhotos={
    'Pug':'pug.png',
    'Maltese':'maltese.png',
    'Golden Retriever':'goldenretriever.png',
    'Labradoodle':'labradoodle.png',
    'Chihuahua':'chihuahua.png',
    'Miniature Schnauzer':'miniatureschnauzer.png',
    'Siberian Husky':'siberianhusky.png',
    'Standard Poodle':'standardpoodle.png'
}

def catResult(score):
    breed=catBreeds.get(score)
    return catDesc.get(breed)

def dogResult(score):
    breed=dogBreeds.get(score)
    return dogDesc.get(breed)
