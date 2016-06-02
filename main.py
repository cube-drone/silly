import datetime as _datetime
import random

import slugify
import inflect
import six

inflectify = inflect.engine()

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
]

nouns = [
    'onion',
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
    'shin',
    'button',
    'byte',
    'cabinet',
    'vehicle',
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
        return datetime(past)

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
def container(*args, **kwargs):
    return random.choice(containers)


@slugify_argument
@capitalize_argument
def numberwang(*args, **kwargs):
    n = random.randint(2, 150)
    return inflectify.number_to_words(n)


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
        "{adjective}{title}"
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
    return thing(a=True, *args, **kwargs)



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


def sentence(*args, **kwargs):
    if 'name' in kwargs and kwargs['name']:
        nm = kwargs(name)
    elif random.choice([True, False, False]):
        nm = name(capitalize=True)
    else:
        nm = random.choice(["I",
                            "You",
                            "Nobody",
                            "The government",
                            "Everybody",
                            "The world",
                            "Your mom"])

    return "{name} will {verb} {thing}.".format(name=nm,
                                                   verb=verb(),
                                                   thing=random.choice([thing(a=True), things()]))


def markdown(length=10):

    def title_sentence():
        return "\n" + "#"*random.randint(1,5) + " " + sentence()

    def embellish(word):
        return random.choice([word, word, "**"+word+"**", "_"+word+"_"])

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
    return "Stop putting gender in your databases. You're just wasting everybody's time."


@slugify_argument
@capitalize_argument
def company_name(*args, **kwargs):
    return random.choice([
        "faculty of Applied {noun}",
       "{noun} studies",
        "{noun} studies department",
        "department of {noun} studies",
        "{noun} management systems",
        "inter{verb}",
        "{thing} incorporated",
        "{noun}co",
    ]).format(noun=noun(), verb=verb(), thing=thing())


@slugify_argument
@capitalize_argument
def address(*args, **kwargs):
    return ""


if __name__ == '__main__':
    print(company_name(capitalize=True))
