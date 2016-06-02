# silly
A python library for producing fanciful test data. 

## what for?

Sometimes I need more test data than just "Testy Testerson" at "123 Fake St."

`silly` can be used to generate data for things. Names. Datetimes. Addresses. Text.

## i want advanced features or your data is not very professional looking

Silly is designed to be quick, funny, and dumb.

If you want localization, customization, and data that doesn't contain the word "poopbutt",
you're probably going to want to look at [faker](https://github.com/joke2k/faker) instead.

## how I install?

    pip install silly


## how I use?

### first bring it in

    import silly

### generate contact info

    name = silly.name()
    print("my name is {}".format(name))
    # my name is colonel beefheart

    print("you should not contact me at {}".format(silly.email()))
    # you should not contact me at buttpike@chump-lol.xyz


### capitalization & slugification

    # this works on everything that it would make sense for it to work on
    #   for everything else it should fail silently
    #       like me

    silly.name(capitalize=True)
    # Colonel Travis Coffeesecrets
    silly.name(slugify=True)
    # carol-kittenmatt


### i want to generate dates and times

    year, month, day = silly.datetime().year, silly.datetime().month, silly.datetime().day
    # 1983, 12, 28

### generate numbers

    number = silly.number()
    print(number)
    # 7
    number_in_words = silly.numberwang()
    print(number_in_words)
    # Eighty Eight

### generate nouns and verbs and adjectives and plurals

    silly.noun()
    # arm
    silly.verb()
    # jump
    silly.adjective()
    # hide
    silly.plural()
    # kittens

### generate past participle

    silly.past_participle()
    # Traceback (most recent call last):
    # File "<stdin>", line 1, in <module>
    # AttributeError: module 'main' has no attribute 'past_participle'

Damn.

### or just generate a thing

    silly.thing()
    # bunch of hats
    silly.thing()
    # eye
    silly.thing()
    # seventy five butts

    silly.a_thing()
    # a tub of hams
    silly.a_thing()
    # an arm
    #silly.a_thing()
    # ninety jeans

### or a whole bunch of things

    silly.things()
    # a bunch of hats, a tub of hams, and ninety jeans

### a web domain

    silly.domain()
    # pants.xyz

### a phone number for some reason

    silly.phone_number()
    # 555-6868

### a whole sentence!

    silly.sentence()
    # Your dad will head to Integrated Harvest And Secret to buy a shell boat.

### or a paragraph!

    silly.paragraph()
    # Youssef Chiffon needs a cluster of white dances, badly.
    # Cabinet Management Systems is the best company in Bagsberg.
    # Armourshire is in North Testonia. Fear space!

    silly.paragraph(length=1000)
    # oh no! that was the length in SENTENCES!
    # what have we done!
    # oh well
    # let's do this anyways:
    #
    # Cheekshop is the best company in Birmingplace.
    # Cornelius Slabmove will braise a heart, seventy-two rum staffs,
    # and one hundred and thirty-two plans. Mysteriousshire Plumbing
    # is the best company in Coasttown. Your mom can't wait to punch
    # one hundred and thirty-seven brown socks in Jerkhall....

### sometimes you need some markdown!

    silly.markdown()
    # ## The World Needs A Wad Of Pencils, Badly.
    # God himself will head to The Law Offices Of Dancereverend, Sweater, And Footsir to buy a group of beech hearts.
    #
    # ## Birmingfisher Is In Mordor.
    # The United Nations needs one hundred and sixteen asses, badly.
    # Deviceshall Municipal Coin Department is the best company in Summerton.
    # The United Nations needs a garlic shin, badly.
    # The Cape Warehouse is the best company in Sweatershall.

it generates markdown that looks like this:

### To Get To South Testasia, You Need To Go To Jeansound, Then Drive North.

##### The Illuminati Needs A Spud, Badly.
Coast Management _Systems_ is the best company _in_ _Central_ _Burgerhall._
_Intersmell_ **is** _the_ **best** company in Whiteholder City.
Personton Municipal Onion Department is the best company in Shieldstown.
Birmingcloud is in Tatooine.
Birmingdong is in East Arztotzka.
Birmingboard is in Tatooine.
Chloe Shelfgroup will grab one hundred and twenty-six collapsible sausages.
Your mom will spin a blanket.

### what about gender?

    silly.gender()
    # Awesome
    silly.gender()
    # Awesome
    silly.gender()
    # Awesome

that's the only response it gives

welp

### maybe you need a company for something?

    silly.company()
    # Beefstapler Studios
    silly.company()
    # Qarth Ministry Of Cages
    silly.company()
    # Olivesoft

### you can generate a whole address, although all of the places are fictional

    silly.address()
    # Thirty-One West Key Block
    silly.address()
    # Apt Twenty-Three, 922 South Code Drive
    silly.country()
    Stankonia
    silly.city()
    Cloudston
    silly.city()
    Beefton South
    silly.postal_code()
    35335
    silly.postal_code()
    K7K 3G3

### sometimes your data has tags. let's make tags.

    tags = list(set([silly.noun() for x in range(0,10)]))
    # ['enormous', 'sly', 'juniper', 'rum', 'touchy', 'marine', 'polka', 'olive', 'sexy', 'sluggish']

#### why is that wrapped in `list()` and `set()`

That's a sneaky way to eliminate duplicates.


### that's it. that's all the things.

YES. Now it is time for me to use your software.

### that's right. do it.

I will.

#### i want to write a script to use it with the 'say' command on mac

You should do that.  It would be great.

### i want to contribute to silly development

It needs tests, tox, and travis before I'll be able to accept pull requests. Coming soon.

Also if the pull request is insufficiently ridiculous it will be rejected outright.
