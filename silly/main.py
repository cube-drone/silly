import datetime as _datetime
import os
import random
import string

import inflect
import six

from . import mock_random


inflectify = inflect.engine()


def _slugify(string):
    """
    This is not as good as a proper slugification function, but the input space is limited

    >>> _slugify("beets")
    'beets'
    >>> _slugify("Toaster Strudel")
    'toaster-strudel'


    Here's why: It handles very little. It doesn't handle esoteric whitespace or symbols:

    >>> _slugify("Hat\\nBasket- of justice and some @#*(! symbols")
    'hat-basket--of-justice-and-some-@#*(!-symbols'

    """
    return string.replace(" ", "-").replace("\n", "-").replace(".", "").replace(",", "").lower()


people = [
    "I",
    "You",
    "Nobody",
    "The government",
    "Everybody",
    "The illuminati",
    "God himself",
    "The President of the United States",
    "The world",
    "The United Nations",
    "The Oakland Raiders",
    "Your dad",
    "Your mom",
    "The band 'Queen'",
    "Customs & Immigration"
]


titles = [
    'captain',
    'lieutenant',
    'leftenant',
    'colonel',
    'general',
    'major',
    'sir',
    'sensei',
    'lord',
    'duke',
    'president',
    'master',
    'mister',
    'miss',
    'lady',
    'queen',
    'king',
    'doctor',
    'monsieur',
    'madame',
    'senor',
    'senorita',
    'lord commander',
    'commodore',
    'emperor',
    'super-emperor',
    'madam',
    'dame',
    'professor',
    'father',
    'brother',
    'sister',
    'reverend',
]

streets = [
    'street',
    'boulevard',
    'drive',
    'block',
    'place',
    'boardwalk',
]

countries = [
    'testonia',
    'testasia',
    'arztotzka',
    'mordor',
    'xanth',
    'stankonia',
    'strongbadia',
    'westeros',
    'qarth',
    'gallifrey',
    'tatooine',
    'cybertron',
    'aiur',
    'lordaeron',
    'yemen',
]

adjectives = [
    'heroic',
    'magnificent',
    'mighty',
    'amazing',
    'wonderful',
    'fantastic',
    'incredible',
    'spectacular',
    'tremendous',
    'throbbing',
    'enormous',
    'terrific',
    'wondrous',
    'spectacular',
    'big',
    'tiny',
    'small',
    'mighty',
    'musky',
    'sky',
    'transparent',
    'opaque',
    'light',
    'dark',
    'sassy',
    'scary',
    'extraneous',
    'huge',
    'aqua',
    'aqua',
    'marine',
    'azure',
    'beige',
    'black',
    'almond',
    'blue',
    'brown',
    'chartreuse',
    'coral',
    'corn',
    'flower',
    'crimson',
    'cyan',
    'navy',
    'golden',
    'rod',
    'gray',
    'grey',
    'green',
    'khaki',
    'magenta',
    'olive',
    'salmon',
    'slate',
    'turquoise',
    'violet',
    'pink',
    'brick',
    'white',
    'golden',
    'honeydew',
    'indigo',
    'ivory',
    'lavender',
    'lemon',
    'chiffon',
    'purple',
    'orchid',
    'linen',
    'rose',
    'orange',
    'pale',
    'sandy',
    'sea',
    'shell',
    'silver',
    'tan',
    'teal',
    'thistle',
    'violet',
    'plaid',
    'polka',
    'dot',
    'paisley',
    'iron',
    'bronze',
    'stone',
    'birch',
    'cedar',
    'cherry',
    'sandal',
    'pine',
    'fir',
    'yew',
    'hem',
    'lock',
    'spruce',
    'chest',
    'box',
    'butter',
    'nut',
    'camphor',
    'elm',
    'oak',
    'huckle',
    'berry',
    'wood'
    'maple',
    'poplar',
    'teak',
    'beech',
    'nutmeg',
    'willow',
    'cinnamon',
    'spice',
    'basil',
    'cardamom',
    'clove',
    'garlic',
    'juniper',
    'rum',
    'lime',
    'capable',
    'heavy',
    'fast',
    'slow',
    'charming',
    'noticeable',
    'sly',
    'slippery',
    'sluggish',
    'casual',
    'cautious',
    'cement',
    'evil',
    'banana',
    'good',
    'neutral',
    'apple',
    'pear',
    'winter',
    'spring',
    'fall',
    'autumn',
    'summer',
    'garbage',
    'imposing',
    'correct',
    'iced',
    'handed',
    'salty',
    'coffee',
    'cheese',
    'floppy',
    'popular',
    'misty',
    'soulful',
    'boaty',
    'gassy',
    'spectacular',
    'sleepy',
    'laudable',
    'comfortable',
    'soft',
    'dicey',
    'memorable',
    'patterned',
    'greasy',
    'elongated',
    'long',
    'collapsible',
    'mysterious',
    'expandible',
    'delicious',
    'edible',
    'scattered',
    'impenetrable',
    'sexy',
    'curvaceous',
    'avoidable',
    'tractable',
    'fussy',
    'touchable',
    'touchy',
    'scandalous',
    'murky',
    'sloshing',
    'damp',
    'chubby',
]

containers = [
    'bucket',
    'bale',
    'cluster',
    'armload',
    'group',
    'container',
    'box',
    'bunch',
    'bag',
    'tub',
    'tote',
    'wad',
]

directions = [
    "west",
    "east",
    "north",
    "south",
    "central",
]

city_suffixes = [
    "ford",
    "berg",
    "shire",
    "town",
    "hall",
    " city",
    "sound",
    "ton",
]

tlds = [
    '.xyz',
    '.blue',
    '.org',
    '.com',
    '.net',
    '.link',
    '.click',
    '.wedding',
    '.sexy',
    '.red',
    '.black',
    '.pics'
]

nouns = [
    'onion',
    'chimp',
    'blister',
    'poop',
    'britches',
    'mystery',
    'boat'
    'bench',
    'secret',
    'mouse',
    'house',
    'butt',
    'hunter',
    'fisher',
    'bean',
    'harvest',
    'mixer',
    'hand',
    'finger',
    'nose',
    'eye',
    'belly',
    'jean',
    'plan',
    'disk',
    'horse',
    'staple',
    'face',
    'arm',
    'cheek',
    'monkey',
    'shin',
    'button',
    'byte',
    'cabinet',
    'canyon',
    'dance',
    'crayon',
    'sausage',
    'meat',
    'wad',
    'napkin',
    'device',
    'cape',
    'chair',
    'person',
    'burger',
    'ham',
    'place',
    'beef',
    'kitten',
    'puppy',
    'book',
    'clamp',
    'cloud',
    'code',
    'coast',
    'coin',
    'concern',
    'space',
    'key',
    'bucket',
    'object',
    'heart',
    'stapler',
    'mug',
    'bottle',
    'cable',
    'note',
    'lamp',
    'shelf',
    'blanket',
    'dong',
    'board',
    'issue',
    'job',
    'knife',
    'thing',
    'phone',
    'sweater',
    'pant',
    'boot',
    'sock',
    'socks',
    'hat',
    'ring',
    'dong',
    'wang',
    'wrap',
    'holder',
    'pen',
    'pencil',
    'bag',
    'potato',
    'sword',
    'shield',
    'spear',
    'staff',
    'shaft',
    'slab',
    'grub',
    'song',
    'axe',
    'boat',
    'armour',
    'lamp',
    'club',
    'cage',
    'hole',
    'ass',
    'chump',
    'jerk',
    'foot',
    'spud',
]

verbs = [
    'jump',
    'twirl',
    'spin',
    'smell',
    'slap',
    'smack',
    'poke',
    'prod',
    'drop',
    'punch',
    'grab',
    'throw',
    'slide',
    'dunk',
    'braise',
    'scatter',
    'slide',
    'dice',
    'hurl',
    'buy',
    'toast',
    'align',
    'sell',
    'move',
    'shoop',
    'trade',
    'steal',
    'flip',
    'blast',
    'clean',
    'hide',
    'pinch',
    'grasp',
    'palm',
    'examine',
    'taste',
    'ingest',
    'swallow',
    'snort',
    'juggle',
    'lift',
    'eat',
    'quaff',
    'chug',
    'fear',
    'assemble',
]

firstnames = [
    'testy',
    'carl',
    'agatha',
    'agnes',
    'carol',
    'harry',
    'maya',
    'judy',
    'mike',
    'albert',
    'cornelius',
    'tim',
    'mary',
    'peter',
    'kiko',
    'wilhelm',
    'kimmy',
    'steve',
    'jennifer',
    'frank',
    'pierre',
    'george',
    'aya',
    'thiago',
    'rodrigo',
    'aasif',
    'mohammed',
    'daniel',
    'liam',
    'jack',
    'agustin',
    'santiago',
    'noah',
    'sofia',
    'olivia',
    'madison',
    'chloe',
    'camilla',
    'carla',
    'gary',
    'hiroto',
    'rasmus',
    'charlie',
    'miguel',
    'alexander',
    'youssef',
    'emma',
    'sara',
    'amelia',
    'tiffany',
    'arnold',
    'ronald',
    'hogan',
    'doug',
    'pete',
    'jim',
    'james',
    'mandy',
    'andy',
    'cole',
    'francis',
    'david',
    'margaret',
    'tracy',
    'jonathan',
    'daniel',
    'heather',
    'travis',
    'courteney',
    'yang',
    'vivian',
    'ryan',
    'phil',
    'shana',
    'allen',
    'karen',
    'henry',
    'graham',
    'jesse',
    'shirley',
    'rafa',
    'dylan',
    'javier',
    'ashley',
    'drew',
    'tomas',
    'taylor',
    'matt',
    'shigeru',
    'shayla',
    'stephanie',
    'oliver',
    'ron',
    'jason',
    'seth',
    'ronald',
    'miloslav',
    'walter',
]


def slugify_argument(func):
    """
    Wraps a function that returns a string, adding the 'slugify' argument.

    >>> slugified_fn = slugify_argument(lambda *args, **kwargs: "YOU ARE A NICE LADY")
    >>> slugified_fn()
    'YOU ARE A NICE LADY'
    >>> slugified_fn(slugify=True)
    'you-are-a-nice-lady'

    """
    @six.wraps(func)
    def wrapped(*args, **kwargs):
        if "slugify" in kwargs and kwargs['slugify']:
            return _slugify(func(*args, **kwargs))
        else:
            return func(*args, **kwargs)
    return wrapped


def capitalize_argument(func):
    """
    Wraps a function that returns a string, adding the 'capitalize' argument.

    >>> capsified_fn = capitalize_argument(lambda *args, **kwargs: "what in the beeswax is this?")
    >>> capsified_fn()
    'what in the beeswax is this?'
    >>> capsified_fn(capitalize=True)
    'What In The Beeswax Is This?'

    """
    @six.wraps(func)
    def wrapped(*args, **kwargs):
        if "capitalize" in kwargs and kwargs['capitalize']:
            return func(*args, **kwargs).title()
        else:
            return func(*args, **kwargs)
    return wrapped


def datetime(past=True, random=random):
    """
    Returns a random datetime from the past... or the future!

    >>> mock_random.seed(0)
    >>> datetime(random=mock_random).isoformat()
    '1950-02-03T03:04:05'
    >>> datetime(random=mock_random, past=False).isoformat()
    '2023-08-09T09:00:01'

    """

    def year():
        if past:
            return random.choice(range(1950,2005))
        else:
            return _datetime.datetime.now().year + random.choice(range(1, 50))

    def month():
        return random.choice(range(1,12))

    def day():
        return random.choice(range(1,31))

    def hour():
        return random.choice(range(0,23))

    def minute():
        return random.choice(range(0,59))

    def second():
        return random.choice(range(0,59))

    try:
        return _datetime.datetime(year=year(),
                                  month=month(),
                                  day=day(),
                                  hour=hour(),
                                  minute=minute(),
                                  second=second())
    except ValueError:
        return datetime(past=past)


@capitalize_argument
def letter(random=random, *args, **kwargs):
    """
    Return a letter!

    >>> mock_random.seed(0)
    >>> letter(random=mock_random)
    'a'
    >>> letter(random=mock_random)
    'b'
    >>> letter(random=mock_random, capitalize=True)
    'C'
    """

    return random.choice(string.ascii_lowercase)


def number(random=random, *args, **kwargs):
    """
    Return a number!

    >>> number(random=mock_random)
    0
    """
    return random.randint(0,9)


@slugify_argument
@capitalize_argument
def title(random=random, *args, **kwargs):
    """
    Return a title!

    >>> mock_random.seed(0)
    >>> title(random=mock_random)
    'captain'
    >>> title(random=mock_random, capitalize=True)
    'Lieutenant'
    >>> title(random=mock_random, slugify=True)
    'leftenant'
    """
    return random.choice(titles)


@slugify_argument
@capitalize_argument
def adjective(random=random, *args, **kwargs):
    """
    Return an adjective!

    >>> mock_random.seed(0)
    >>> adjective(random=mock_random)
    'heroic'
    >>> adjective(random=mock_random, capitalize=True)
    'Magnificent'
    >>> adjective(random=mock_random, slugify=True)
    'mighty'
    """
    return random.choice(adjectives)


@slugify_argument
@capitalize_argument
def noun(random=random, *args, **kwargs):
    """
    Return a noun!

    >>> mock_random.seed(0)
    >>> noun(random=mock_random)
    'onion'
    >>> noun(random=mock_random, capitalize=True)
    'Chimp'
    >>> noun(random=mock_random, slugify=True)
    'blister'
    """
    return random.choice(nouns)


@slugify_argument
@capitalize_argument
def a_noun(random=random, *args, **kwargs):
    """
    Return a noun, but with an 'a' in front of it. Or an 'an', depending!

    >>> mock_random.seed(0)
    >>> a_noun(random=mock_random)
    'an onion'
    >>> a_noun(random=mock_random, capitalize=True)
    'A Chimp'
    >>> a_noun(random=mock_random, slugify=True)
    'a-blister'
    """
    return inflectify.a(noun(random=random))


@slugify_argument
@capitalize_argument
def plural(random=random, *args, **kwargs):
    """
    Return a plural noun.

    >>> mock_random.seed(0)
    >>> plural(random=mock_random)
    'onions'
    >>> plural(random=mock_random, capitalize=True)
    'Chimps'
    >>> plural(random=mock_random, slugify=True)
    'blisters'
    """
    return inflectify.plural(random.choice(nouns))


@slugify_argument
@capitalize_argument
def verb(random=random, *args, **kwargs):
    """
    Return a verb!

    >>> mock_random.seed(0)
    >>> verb(random=mock_random)
    'jump'
    >>> verb(random=mock_random, capitalize=True)
    'Twirl'
    >>> verb(random=mock_random, slugify=True)
    'spin'
    """
    return random.choice(verbs)


@slugify_argument
@capitalize_argument
def firstname(random=random, *args, **kwargs):
    """
    Return a first name!

    >>> mock_random.seed(0)
    >>> firstname(random=mock_random)
    'testy'
    >>> firstname(random=mock_random, capitalize=True)
    'Carl'
    >>> firstname(random=mock_random, slugify=True)
    'agatha'
    """
    return random.choice(firstnames)


@slugify_argument
@capitalize_argument
def lastname(random=random, *args, **kwargs):
    """
    Return a first name!

    >>> mock_random.seed(0)
    >>> lastname(random=mock_random)
    'chimp'
    >>> mock_random.seed(1)
    >>> lastname(random=mock_random, capitalize=True)
    'Wonderful'
    >>> mock_random.seed(2)
    >>> lastname(random=mock_random, slugify=True)
    'poopbritches'

    >>> [lastname(random=mock_random) for x in range(0,10)]
    ['wonderful', 'chimp', 'onionmighty', 'magnificentslap', 'smellmouse', 'secretbale', 'boatbenchtwirl', 'spectacularmice', 'incrediblebritches', 'poopbritches']


    """
    types = [
        "{noun}",
        "{adjective}",
        "{noun}{second_noun}",
        "{adjective}{noun}",
        "{adjective}{plural}",
        "{noun}{verb}",
        "{noun}{container}",
        "{verb}{noun}",
        "{adjective}{verb}",
        "{noun}{adjective}",
        "{noun}{firstname}",
        "{noun}{title}",
        "{adjective}{title}",
        "{adjective}-{noun}",
        "{adjective}-{plural}"
    ]

    return random.choice(types).format(noun=noun(random=random),
                                       second_noun=noun(random=random),
                                       adjective=adjective(random=random),
                                       plural=plural(random=random),
                                       container=container(random=random),
                                       verb=verb(random=random),
                                       firstname=firstname(random=random),
                                       title=title(random=random))


@slugify_argument
@capitalize_argument
def container(random=random, *args, **kwargs):
    """
    Return a container!

    >>> mock_random.seed(0)
    >>> container(random=mock_random)
    'bucket'
    >>> container(random=mock_random, capitalize=True)
    'Bale'
    >>> container(random=mock_random, slugify=True)
    'cluster'
    """
    return random.choice(containers)


@slugify_argument
@capitalize_argument
def numberwang(random=random, *args, **kwargs):
    """
    Return a number that is spelled out.

    >>> numberwang(random=mock_random)
    'two'
    >>> numberwang(random=mock_random, capitalize=True)
    'Two'
    >>> numberwang(random=mock_random, slugify=True)
    'two'

    """
    n = random.randint(2, 150)
    return inflectify.number_to_words(n)


@slugify_argument
@capitalize_argument
def direction(random=random, *args, **kwargs):
    """
    Return a direction!

    >>> mock_random.seed(0)
    >>> direction(random=mock_random)
    'west'
    >>> direction(random=mock_random, capitalize=True)
    'East'
    >>> direction(random=mock_random, slugify=True)
    'north'
    """
    return random.choice(directions)


@slugify_argument
@capitalize_argument
def city_suffix(random=random, *args, **kwargs):
    """
    Return a city suffix, like 'berg' or 'hall'.

    >>> mock_random.seed(0)
    >>> city_suffix(random=mock_random)
    'ford'
    >>> city_suffix(random=mock_random, capitalize=True)
    'Berg'
    >>> city_suffix(random=mock_random, slugify=True)
    'shire'
    """
    return random.choice(city_suffixes)


@slugify_argument
@capitalize_argument
def tld(random=random, *args, **kwargs):
    """
    Return a direction!

    >>> mock_random.seed(0)
    >>> tld(random=mock_random)
    '.xyz'
    >>> tld(random=mock_random, capitalize=True)
    '.Blue'
    >>> tld(random=mock_random, slugify=True)
    'org'
    """
    return random.choice(tlds)



@slugify_argument
@capitalize_argument
def thing(random=random, *args, **kwargs):
    """
    Return a ... thing.

    >>> mock_random.seed(0)
    >>> thing(random=mock_random)
    'two secrets'
    >>> mock_random.seed(1)
    >>> thing(random=mock_random, capitalize=True)
    'Mighty Poop'
    >>> mock_random.seed(2)
    >>> thing(random=mock_random, slugify=True)
    'poop'
    >>> mock_random.seed(4)
    >>> thing(random=mock_random, slugify=True)
    'two-chimps'

    """

    def noun_or_adjective_noun():
        if random.choice([True, False]):
            return noun(random=random)
        else:
            return adjective(random=random) + " " + noun(random=random)

    def plural_or_adjective_plural():
        if random.choice([True, False]):
            return plural(random=random)
        else:
            return adjective(random=random) + " " + plural(random=random)

    def container_of_nouns():
        return container(random=random) + " of " + plural_or_adjective_plural()

    def number_of_plurals():
        return numberwang(random=random) + " " + plural_or_adjective_plural()

    if "an" in kwargs and kwargs['an']:
        return random.choice([
            inflectify.a(noun_or_adjective_noun()),
            inflectify.a(container_of_nouns()),
            number_of_plurals(),
        ])
    else:
        return random.choice([
            noun_or_adjective_noun(),
            container_of_nouns(),
            number_of_plurals(),
        ])


@slugify_argument
def a_thing(random=random, *args, **kwargs):
    """
    Return a ... thing.

    >>> mock_random.seed(0)
    >>> a_thing(random=mock_random)
    'two secrets'
    >>> mock_random.seed(1)
    >>> a_thing(random=mock_random, capitalize=True)
    'A Mighty Poop'
    >>> mock_random.seed(2)
    >>> a_thing(random=mock_random, slugify=True)
    'a-poop'
    >>> mock_random.seed(4)
    >>> a_thing(random=mock_random, slugify=True)
    'two-chimps'

    """
    return thing(random=random, an=True, *args, **kwargs)


@slugify_argument
@capitalize_argument
def things(random=random, *args, **kwargs):
    """
    Return a set of things.

    >>> mock_random.seed(0)
    >>> things(random=mock_random)
    'two secrets, two secrets, and two secrets'
    >>> mock_random.seed(1)
    >>> things(random=mock_random, capitalize=True)
    'A Mighty Poop, A Mighty Poop, And A Mighty Poop'

    """
    return inflectify.join([a_thing(random=random), a_thing(random=random), a_thing(random=random)])


@slugify_argument
@capitalize_argument
def name(random=random, *args, **kwargs):
    """
    Return someone's name

    >>> mock_random.seed(0)
    >>> name(random=mock_random)
    'carl poopbritches'
    >>> mock_random.seed(7)
    >>> name(random=mock_random, capitalize=True)
    'Duke Testy Wonderful'

    """
    if random.choice([True, True, True, False]):
        return firstname(random=random) + " " + lastname(random=random)
    elif random.choice([True, False]):
        return title(random=random) + " " + firstname(random=random) + " " + lastname(random=random)
    else:
        return title(random=random) + " " + lastname(random=random)


@slugify_argument
@capitalize_argument
def domain(random=random, *args, **kwargs):
    """
    Return a domain

    >>> mock_random.seed(0)
    >>> domain(random=mock_random)
    'onion.net'
    >>> domain(random=mock_random)
    'bag-of-heroic-chimps.sexy'

    """
    words = random.choice([
        noun(random=random),
        thing(random=random),
        adjective(random=random)+noun(random=random),
    ])
    return _slugify(words)+tld(random=random)


def email(random=random, *args, **kwargs):
    """
    Return an e-mail address

    >>> mock_random.seed(0)
    >>> email(random=mock_random)
    'onion@bag-of-heroic-chimps.sexy'
    >>> email(random=mock_random)
    'agatha-incrediblebritches+spam@amazingbritches.click'
    >>> email(random=mock_random, name="charles")
    'charles@secret.xyz'

    """
    if 'name' in kwargs and kwargs['name']:
        words = kwargs['name']
    else:
        words = random.choice([
            noun(random=random),
            name(random=random),
            name(random=random)+"+spam",
        ])
    return _slugify(words)+"@"+domain(random=random)


def phone_number(random=random, *args, **kwargs):
    """
    Return a phone number

    >>> mock_random.seed(0)
    >>> phone_number(random=mock_random)
    '555-0000'
    >>> phone_number(random=mock_random)
    '1-604-555-0000'
    >>> phone_number(random=mock_random)
    '864-70-555-0000'

    """
    return random.choice([
        '555-{number}{other_number}{number}{other_number}',
        '1-604-555-{number}{other_number}{number}{other_number}',
        '864-70-555-{number}{other_number}{number}{other_number}',
        '867-5309'
    ]).format(number=number(random=random),
              other_number=number(random=random))


@slugify_argument
@capitalize_argument
def sentence(random=random, *args, **kwargs):
    """
    Return a whole sentence

    >>> mock_random.seed(0)
    >>> sentence(random=mock_random)
    "Agatha Incrediblebritches can't wait to smell two chimps in Boatbencheston."

    >>> mock_random.seed(2)
    >>> sentence(random=mock_random, slugify=True)
    'blistersecret-studios-is-the-best-company-in-liveronion'

    """
    if 'name' in kwargs and kwargs['name']:
        nm = kwargs(name)
    elif random.choice([True, False, False]):
        nm = name(capitalize=True, random=random)
    else:
        nm = random.choice(people)

    def type_one():
        return "{name} will {verb} {thing}.".format(name=nm,
                                                    verb=verb(random=random),
                                                    thing=random.choice([a_thing(random=random),
                                                                         things(random=random)]))

    def type_two():
        return "{city} is in {country}.".format(city=city(capitalize=True, random=random),
                                                country=country(capitalize=True, random=random))

    def type_three():
        return "{name} can't wait to {verb} {thing} in {city}.".format(name=nm,
                                                                      verb=verb(random=random),
                                                                      thing=a_thing(random=random),
                                                                      city=city(capitalize=True, random=random))

    def type_four():
        return "{name} will head to {company} to buy {thing}.".format(name=nm,
                                                                     company=company(capitalize=True, random=random),
                                                                     thing=a_thing(random=random))


    def type_five():
        return "{company} is the best company in {city}.".format(city=city(capitalize=True, random=random),
                                                                 company=company(capitalize=True, random=random))

    def type_six():
        return "To get to {country}, you need to go to {city}, then drive {direction}.".format(
            country=country(capitalize=True, random=random),
            city=city(capitalize=True, random=random),
            direction=direction(random=random))

    def type_seven():
        return "{name} needs {thing}, badly.".format(name=nm, thing=a_thing(random=random))

    def type_eight():
        return "{verb} {noun}!".format(verb=verb(capitalize=True, random=random), noun=noun(random=random))

    return random.choice([type_one,
                          type_two,
                          type_three,
                          type_four,
                          type_five,
                          type_six,
                          type_seven,
                          type_eight])()


@slugify_argument
@capitalize_argument
def paragraph(random=random, length=10, *args, **kwargs):
    """
    Produces a paragraph of text.

    >>> mock_random.seed(0)
    >>> paragraph(random=mock_random, length=2)
    "Agatha Incrediblebritches can't wait to smell two chimps in Boatbencheston. Wonderfulsecretsound is in Gallifrey."

    >>> mock_random.seed(2)
    >>> paragraph(random=mock_random, length=2, slugify=True)
    'blistersecret-studios-is-the-best-company-in-liveronion-wonderfulsecretsound-is-in-gallifrey'

    """
    return " ".join([sentence(random=random) for x in range(0, length)])


def markdown(random=random, length=10, *args, **kwargs):
    """
    Produces a bunch of markdown text.

    >>> mock_random.seed(0)
    >>> markdown(random=mock_random, length=2)
    'Nobody will **head** _to_ Mystery Studies Department **to** _buy_ a mighty poop.\\nNobody will **head** _to_ Mystery Studies Department **to** _buy_ a mighty poop.'

    """

    def title_sentence():
        return "\n" + "#"*random.randint(1,5) + " " + sentence(capitalize=True, random=random)

    def embellish(word):
        return random.choice([word, word, word, "**"+word+"**", "_"+word+"_"])

    def randomly_markdownify(string):
        return " ".join([embellish(word) for word in string.split(" ")])

    sentences = []
    for i in range(0, length):
        sentences.append(random.choice([
            title_sentence(),
            sentence(random=random),
            sentence(random=random),
            randomly_markdownify(sentence(random=random))
        ]))
    return "\n".join(sentences)


@slugify_argument
@capitalize_argument
def gender(random=random, *args, **kwargs):
    return "Awesome"


@slugify_argument
@capitalize_argument
def company(random=random, *args, **kwargs):
    """
    Produce a company name

    >>> mock_random.seed(0)
    >>> company(random=mock_random)
    'faculty of applied chimp'
    >>> mock_random.seed(1)
    >>> company(random=mock_random)
    'blistersecret studios'
    >>> mock_random.seed(2)
    >>> company(random=mock_random)
    'pooppooppoop studios'
    >>> mock_random.seed(3)
    >>> company(random=mock_random)
    'britchesshop'
    >>> mock_random.seed(4)
    >>> company(random=mock_random, capitalize=True)
    'Mystery Studies Department'
    >>> mock_random.seed(5)
    >>> company(random=mock_random, slugify=True)
    'the-law-offices-of-magnificentslap-boatbench-and-smellmouse'

    """
    return random.choice([
        "faculty of applied {noun}",
        "{noun}{second_noun} studios",
        "{noun}{noun}{noun} studios",
        "{noun}shop",
        "{noun} studies department",
        "the law offices of {lastname}, {noun}, and {other_lastname}",
        "{country} ministry of {plural}",
        "{city} municipal {noun} department",
        "{city} plumbing",
        "department of {noun} studies",
        "{noun} management systems",
        "{plural} r us",
        "inter{verb}",
        "the {noun} warehouse",
        "integrated {noun} and {second_noun}",
        "the {noun} and {second_noun} pub",
        "e-cyber{verb}",
        "{adjective}soft",
        "{domain} Inc.",
        "{thing} incorporated",
        "{noun}co",
    ]).format(noun=noun(random=random),
              plural=plural(random=random),
              country=country(random=random),
              city=city(random=random),
              adjective=adjective(random=random),
              lastname=lastname(random=random),
              other_lastname=lastname(random=random),
              domain=domain(random=random),
              second_noun=noun(random=random),
              verb=verb(random=random),
              thing=thing(random=random))


@slugify_argument
@capitalize_argument
def country(random=random, *args, **kwargs):
    """
    Produce a country name

    >>> mock_random.seed(0)
    >>> country(random=mock_random)
    'testasia'
    >>> country(random=mock_random, capitalize=True)
    'West Xanth'
    >>> country(random=mock_random, slugify=True)
    'westeros'

    """
    return random.choice([
        "{country}",
        "{direction} {country}"
    ]).format(country=random.choice(countries),
              direction=direction(random=random))


@slugify_argument
@capitalize_argument
def city(random=random, *args, **kwargs):
    """
    Produce a city name

    >>> mock_random.seed(0)
    >>> city(random=mock_random)
    'east mysteryhall'
    >>> city(random=mock_random, capitalize=True)
    'Birmingchimp'
    >>> city(random=mock_random, slugify=True)
    'wonderfulsecretsound'

    """
    return random.choice([
        "{direction} {noun}{city_suffix}",
        "{noun}{city_suffix}",
        "{adjective}{noun}{city_suffix}",
        "{plural}{city_suffix}",
        "{adjective}{city_suffix}",
        "liver{noun}",
        "birming{noun}",
        "{noun}{city_suffix} {direction}"
    ]).format(direction=direction(random=random),
              adjective=adjective(random=random),
              plural=plural(random=random),
              city_suffix=city_suffix(random=random),
              noun=noun(random=random))


@slugify_argument
@capitalize_argument
def postal_code(random=random, *args, **kwargs):
    """
    Produce something that vaguely resembles a postal code

    >>> mock_random.seed(0)
    >>> postal_code(random=mock_random)
    'b0b 0c0'
    >>> postal_code(random=mock_random, capitalize=True)
    'E0E 0F0'
    >>> postal_code(random=mock_random, slugify=True)
    'h0h-0i0'

    """
    return random.choice([
        "{letter}{number}{letter} {other_number}{other_letter}{other_number}",
        "{number}{other_number}{number}{number}{other_number}",
        "{number}{letter}{number}{other_number}{other_letter}"
    ]).format(
        number=number(random=random),
        other_number=number(random=random),
        letter=letter(random=random),
        other_letter=letter(random=random)
    )



@slugify_argument
@capitalize_argument
def street(random=random, *args, **kwargs):
    """
    Produce something that sounds like a street name

    >>> mock_random.seed(0)
    >>> street(random=mock_random)
    'chimp place'
    >>> street(random=mock_random, capitalize=True)
    'Boatbench Block'
    >>> mock_random.seed(3)
    >>> street(random=mock_random, slugify=True)
    'central-britches-boulevard'

    """
    return random.choice([
        "{noun} {street_type}",
        "{adjective}{verb} {street_type}",
        "{direction} {adjective}{verb} {street_type}",
        "{direction} {noun} {street_type}",
        "{direction} {lastname} {street_type}",
    ]).format(noun=noun(random=random),
              lastname=lastname(random=random),
              direction=direction(random=random),
              adjective=adjective(random=random),
              verb=verb(random=random),
              street_type=random.choice(streets))


@slugify_argument
@capitalize_argument
def address(random=random, *args, **kwargs):
    """
    A street name plus a number!

    >>> mock_random.seed(0)
    >>> address(random=mock_random)
    '0000 amazingslap boardwalk'
    >>> address(random=mock_random, capitalize=True)
    '0000 South Throbbingjump Boulevard'
    >>> address(random=mock_random, slugify=True)
    'two-central-britches-boulevard'

    """
    return random.choice([
        "{number}{other_number}{number}{other_number} {street}",
        "{number}{other_number} {street}",
        "{numberwang} {street}",
        "apt {numberwang}, {number}{other_number}{other_number} {street}",
        "apt {number}{other_number}{number}, {numberwang} {street}",
        "po box {number}{other_number}{number}{other_number}",
    ]).format(number=number(random=random),
              other_number=number(random=random),
              numberwang=numberwang(random=random),
              street=street(random=random))


