WIDTH, HEIGHT = SIZE = (1200, 600)


SHORT_DECK = True

COLOUR_INDEX = [x for x in range(0, 4)]
COLOUR_NAME = ['clubs', 'diamonds', 'hearts', 'spades']
COLOUR_NAME_INDEX = {COLOUR_NAME[i]: i for i in COLOUR_INDEX}
COLOUR_INDEX_NAME = {i: COLOUR_NAME[i] for i in COLOUR_INDEX}

RANK_NAME_INDEX = {
    '2': 2,
    '3': 3,
    '4': 4,
    '5': 5,
    '6': 6,
    '7': 7,
    '8': 8,
    '9': 9,
    '10': 10,
    'jack': 10,
    'queen': 10,
    'king': 10,
    'ace': 11
}


RANK_INDEX_NAME = {i: r for r, i in RANK_NAME_INDEX.items()}

EUROPE = 0
AMERICAN = 1

FULL_TRANSPARENCY = 0
HIGH_TRANSPARENCY = 30
MEDIUM_TRANSPARENCY = 80
LOW_TRANSPARENCY = 150
VERY_LOW_TRANSPARENCY = 200
NOT_TRANSPARENCY = 255
