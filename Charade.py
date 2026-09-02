import random
import os
import time
os.system('cls' if os.name == 'nt'else 'clear')
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
    "Walking on a tightrope",
    "Eating noodles with chopsticks",
    "A snowball fight",
    "Doing karaoke",
    "Juggling balls",
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
]
while True:
    print(f"Your prompt is: \n{random.choice(randStuff)}\n\n")
    time.sleep(60)
    os.system('cls' if os.name == 'nt'else 'clear')