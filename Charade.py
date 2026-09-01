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
    "Lost in a desert",
    "A baby learning to walk",
    "Eating extremely spicy food",
    "Milking a cow",
    "Walking on a rope",
    "A dog chasing its tail",
    "Eating noodles with chopsticks",
    "Finding your car in a huge parking lot",
    "A snowball fight",
    "Doing karaoke",
    "Juggling oranges",
    "Pretending to be a zombie",
    "Inflating a balloon with your mouth",
    "Sneaking a snack",
    "Eating a burger",
    "Singing a birhday song",
    "Using a toaster"
]
print(f"Your prompt is: \n{random.choice(randStuff)}\n\n")