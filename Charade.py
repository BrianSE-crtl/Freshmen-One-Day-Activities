import random
import os
os.system(
    'cls' if os.name == 'nt'
    else 'clear'
    )
randStuff = [
    "Chopping down wood",
    "Plunging a toilet",
    "A grandma using TikTok",
    "Getting attacked by bees",
    "Trying to catch a fly",
    "Trying to sneak out of the house",
    "Lost in a grocery store", 
    "A baby learning to walk",
    "Eating extremely spicy food",
    "A dog chasing its tail",
    "Trying to sneak out of the house"
]
print(f"Your prompt is: \n{random.choice(randStuff)}")
