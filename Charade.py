import random
import os
os.system(
    'cls' if os.name == 'nt'
    else 'clear'
    )
randStuff = [
    "Chopping down wood",
    "Plunging a toilet",
    "A grandma/grandpa using TikTok",
    "Getting attacked by bees",
    "Trying to catch a fly",
    "Lost in a desert",
    "A baby learning to walk",
    "Eating extremely spicy food",
    "Milking a cow",
    "Walking on a rope",
    "Eating noodles with chopsticks",
    "A snowball fight",
    "Doing karaoke",
    "Juggling oranges",
    "Walking Zombie",
    "Inflating a balloon with your mouth",
    "Sneaking a snack",
    "Eating a burger",
    "Using a toaster",
    "Trying to open a jar",
    "Walking like a penguin", 
    "Playing the guitar", 
    "Lifting weights",
    "Having a pillowfight",
    "Reading a newspaper",
    "Taking a nap",
    "Making your bed"
]
print(f"Your prompt is: \n{random.choice(randStuff)}\n\n")