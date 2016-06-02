"""
For the sake of testing, here we have a 'random' class that is not very random at all.
"""


GIANT_GLOBAL_COUNTER = 0

def seed(seed_value=0):
    global GIANT_GLOBAL_COUNTER
    GIANT_GLOBAL_COUNTER = seed_value

def choice(listy_thing):
    global GIANT_GLOBAL_COUNTER
    thing = listy_thing[GIANT_GLOBAL_COUNTER % len(listy_thing)]
    GIANT_GLOBAL_COUNTER += 1
    if GIANT_GLOBAL_COUNTER >= 10:
        GIANT_GLOBAL_COUNTER = 0
    return thing

def randint(start, end):
    return start
