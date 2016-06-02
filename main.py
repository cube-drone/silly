import datetime as _datetime
import random

import inflect
import six

inflectify = inflect.engine()

def slugify(string):
    """
    This is not as good as a proper slugification function, but the input space is limited
    """
    return string.replace(" ", "-").replace("\n", "-").replace(".", "").replace(",", "").lower()

letters = [
    'a',
    'b',
    'c',
    'd',
    'e',
    'f',
    'g',
    'h',
    'i',
    'j',
    'k',
    'l',
    'm',
    'n',
    'o',
    'p',
    'q',
    'r',
    's',
    't',
    'u',
    'v',
    'w',
    'x',
    'y',
    'z'
]


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
    '.xyz',
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
    def wrapped(*args, **kwargs):
        if "slugify" in kwargs and kwargs['slugify']:
            return slugify(func(*args, **kwargs))
        else:
            return func(*args, **kwargs)
    return wrapped


def capitalize_argument(func):
    def wrapped(*args, **kwargs):
        if "capitalize" in kwargs and kwargs['capitalize']:
            return func(*args, **kwargs).title()
        else:
            return func(*args, **kwargs)
    return wrapped


def datetime(past=True):
    """
    Returns a random datetime from the past
    """

    def year():
        if past:
            return random.choice(range(1950,2005))
        else:
            return _datetime.datetime.now().year + random.choice(range[1, 50])

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


def letter():
    return random.choice(letters)


def number():
    return random.randint(0,9)


@slugify_argument
@capitalize_argument
def title(*args, **kwargs):
    return random.choice(titles)


@slugify_argument
@capitalize_argument
def adjective(*args, **kwargs):
    return random.choice(adjectives)


@slugify_argument
@capitalize_argument
def noun(*args, **kwargs):
    return random.choice(nouns)


@slugify_argument
@capitalize_argument
def a_noun(*args, **kwargs):
    return inflectify.a(noun)


@slugify_argument
@capitalize_argument
def plural(*args, **kwargs):
    return inflectify.plural(random.choice(nouns))


@slugify_argument
@capitalize_argument
def verb(*args, **kwargs):
    return random.choice(verbs)


@slugify_argument
@capitalize_argument
def firstname(*args, **kwargs):
    return random.choice(firstnames)


@slugify_argument
@capitalize_argument
def lastname(*args, **kwargs):
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

    return random.choice(types).format(noun=noun(),
                                       second_noun=noun(),
                                       adjective=adjective(),
                                       plural=plural(),
                                       container=container(),
                                       verb=verb(),
                                       firstname=firstname(),
                                       title=title())


@slugify_argument
@capitalize_argument
def container(*args, **kwargs):
    return random.choice(containers)


@slugify_argument
@capitalize_argument
def numberwang(*args, **kwargs):
    n = random.randint(2, 150)
    return inflectify.number_to_words(n)


@slugify_argument
@capitalize_argument
def direction(*args, **kwargs):
    return random.choice(directions)


@slugify_argument
@capitalize_argument
def city_suffix(*args, **kwargs):
    return random.choice(city_suffixes)


@slugify_argument
@capitalize_argument
def tld(*args, **kwargs):
    return random.choice(tlds)



@slugify_argument
@capitalize_argument
def thing(*args, **kwargs):

    def noun_or_adjective_noun():
        if random.choice([True, False]):
            return noun()
        else:
            return adjective() + " " + noun()

    def plural_or_adjective_plural():
        if random.choice([True, False]):
            return plural()
        else:
            return adjective() + " " + plural()

    def container_of_nouns():
        return container() + " of " + plural_or_adjective_plural()

    def number_of_plurals():
        return numberwang() + " " + plural_or_adjective_plural()

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
def a_thing(*args, **kwargs):
    return thing(an=True, *args, **kwargs)


@slugify_argument
@capitalize_argument
def things(*args, **kwargs):
    return inflectify.join([a_thing(), a_thing(), a_thing()])


@slugify_argument
@capitalize_argument
def name(*args, **kwargs):
    if random.choice([True, True, True, False]):
        return firstname() + " " + lastname()
    elif random.choice([True, False]):
        return title() + " " + firstname() + " " + lastname()
    else:
        return title() + " " + lastname()


@slugify_argument
@capitalize_argument
def domain(*args, **kwargs):
    words = random.choice([
        noun(),
        thing(),
        adjective()+noun(),
    ])
    return slugify(words)+tld()


def email(*args, **kwargs):
    if 'name' in kwargs and kwargs['name']:
        words = kwargs['name']
    else:
        words = random.choice([
            noun(),
            name(),
            name()+"+spam",
        ])
    return slugify(words)+"@"+domain()


def phone_number(*args, **kwargs):
    return random.choice([
        '555-{number}{other_number}{number}{other_number}',
        '1-604-555-{number}{other_number}{number}{other_number}',
        '864-70-555-{number}{other_number}{number}{other_number}',
        '867-5309'
    ]).format(number=number(),
              other_number=number())


@slugify_argument
@capitalize_argument
def sentence(*args, **kwargs):
    if 'name' in kwargs and kwargs['name']:
        nm = kwargs(name)
    elif random.choice([True, False, False]):
        nm = name(capitalize=True)
    else:
        nm = random.choice(people)

    def type_one():
        return "{name} will {verb} {thing}.".format(name=nm,
                                                    verb=verb(),
                                                    thing=random.choice([a_thing(), things()]))

    def type_two():
        return "{city} is in {country}.".format(city=city(capitalize=True),
                                                country=country(capitalize=True))

    def type_three():
        return "{name} can't wait to {verb} {thing} in {city}.".format(name=nm,
                                                                      verb=verb(),
                                                                      thing=a_thing(),
                                                                      city=city(capitalize=True))

    def type_four():
        return "{name} will head to {company} to buy {thing}.".format(name=nm,
                                                                     company=company(capitalize=True),
                                                                     thing=a_thing())


    def type_five():
        return "{company} is the best company in {city}.".format(city=city(capitalize=True),
                                                                 company=company(capitalize=True))

    def type_six():
        return "To get to {country}, you need to go to {city}, then drive {direction}.".format(
            country=country(capitalize=True),
            city=city(capitalize=True),
            direction=direction())

    def type_seven():
        return "{name} needs {thing}, badly.".format(name=nm, thing=a_thing())

    def type_eight():
        return "{verb} {noun}!".format(verb=verb(capitalize=True), noun=noun())

    return random.choice([type_one(),
                          type_two(),
                          type_three(),
                          type_four(),
                          type_five(),
                          type_six(),
                          type_seven(),
                          type_eight()])


@slugify_argument
@capitalize_argument
def paragraph(length=10):
    """
    Produces a paragraph of text.
    """
    return " ".join([sentence() for x in range(0, length)])


def markdown(length=10):
    """
    Produces a bunch of markdown text.
    """

    def title_sentence():
        return "\n" + "#"*random.randint(1,5) + " " + sentence(capitalize=True)

    def embellish(word):
        return random.choice([word, word, word, "**"+word+"**", "_"+word+"_"])

    def randomly_markdownify(string):
        return " ".join([embellish(word) for word in string.split(" ")])

    sentences = []
    for i in range(0, length):
        sentences.append(random.choice([
            title_sentence(),
            sentence(),
            sentence(),
            randomly_markdownify(sentence())
        ]))
    return "\n".join(sentences)


@slugify_argument
@capitalize_argument
def gender(*args, **kwargs):
    return "Awesome"


@slugify_argument
@capitalize_argument
def company(*args, **kwargs):
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
    ]).format(noun=noun(),
              plural=plural(),
              country=country(),
              city=city(),
              adjective=adjective(),
              lastname=lastname(),
              other_lastname=lastname(),
              domain=domain(),
              second_noun=noun(),
              verb=verb(),
              thing=thing())


@slugify_argument
@capitalize_argument
def country(*args, **kwargs):
    return random.choice([
        "{country}",
        "{direction} {country}"
    ]).format(country=random.choice(countries),
              direction=direction())


@slugify_argument
@capitalize_argument
def city(*args, **kwargs):
    return random.choice([
        "{direction} {noun}{city_suffix}",
        "{noun}{city_suffix}",
        "{adjective}{noun}{city_suffix}",
        "{plural}{city_suffix}",
        "{adjective}{city_suffix}",
        "liver{noun}",
        "birming{noun}",
        "{noun}{city_suffix} {direction}"
    ]).format(direction=direction(),
              adjective=adjective(),
              plural=plural(),
              city_suffix=city_suffix(),
              noun=noun())


@slugify_argument
@capitalize_argument
def postal_code(*args, **kwargs):
    return random.choice([
        "{letter}{number}{letter} {other_number}{other_letter}{other_number}",
        "{number}{other_number}{number}{number}{other_number}",
        "{number}{letter}{number}{other_number}{other_letter}"
    ]).format(
        number=number(),
        other_number=number(),
        letter=letter(),
        other_letter=letter()
    )



@slugify_argument
@capitalize_argument
def street(*args, **kwargs):
    return random.choice([
        "{noun} {street_type}",
        "{adjective}{verb} {street_type}",
        "{direction} {adjective}{verb} {street_type}",
        "{direction} {noun} {street_type}",
        "{direction} {lastname} {street_type}",
    ]).format(noun=noun(),
              lastname=lastname(),
              direction=direction(),
              adjective=adjective(),
              verb=verb(),
              street_type=random.choice(streets))


@slugify_argument
@capitalize_argument
def address(*args, **kwargs):
    return random.choice([
        "{number}{other_number}{number}{other_number} {street}",
        "{number}{other_number} {street}",
        "{numberwang} {street}",
        "Apt {numberwang}, {number}{other_number}{other_number} {street}",
        "Apt {number}{other_number}{number}, {numberwang} {street}",
        "PO Box {number}{other_number}{number}{other_number}",
    ]).format(number=number(),
              other_number=number(),
              numberwang=numberwang(),
              street=street())


if __name__ == '__main__':
    nm = name(capitalize=True)
    six.print_(nm)
    six.print_(email(name=nm))
    six.print_(phone_number())
    six.print_("")
    six.print_(company(capitalize=True))
    six.print_(address(capitalize=True))
    six.print_(city(capitalize=True) + " " + postal_code(capitalize=True))
    six.print_(country(capitalize=True))
    six.print_("")
    six.print_(datetime().isoformat())
    six.print_(paragraph(length=4))
    six.print_("")
    six.print_(markdown(length=10))
