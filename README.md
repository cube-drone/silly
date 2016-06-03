# silly
A python library for producing fanciful test data.

## hat for?

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


### tell me about capitalization & slugification

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

### i want to generate numbers

    number = silly.number()
    print(number)
    # 7
    number_in_words = silly.numberwang()
    print(number_in_words)
    # Eighty Eight

### i want to generate words

    silly.noun()
    # arm
    silly.verb()
    # jump
    silly.adjective()
    # hide
    silly.plural()
    # kittens

### i want to generate a past participle

    silly.past_participle()
    # Traceback (most recent call last):
    # File "<stdin>", line 1, in <module>
    # AttributeError: module 'main' has no attribute 'past_participle'

Damn.

### how about i just generate a thing

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

### i need a web domain

    silly.domain()
    # pants.xyz

### i need a phone number for some reason

    silly.phone_number()
    # 555-6868

### how about an image?

    silly.image()
    # http://dummyimage.com/800x600/292929/e3e3e3&text=mighty poop

    silly.image(width=1000, height=60)
    # http://placekitten.com/1000/60

    silly.image(https=True, width=40, height=50)
    # https://dummyimage.com/40x50/292929/e3e3e3&text=house

### i want a whole sentence!

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

### sometimes I need some markdown!

    silly.markdown()
    # ## The World Needs A Wad Of Pencils, Badly.
    # God himself will head to The Law Offices Of Dancereverend, Sweater, And Footsir to buy a group of beech hearts.
    #
    # ## Birmingfisher Is In Mordor.
    # The United Nations needs one hundred and sixteen asses, badly.
    # Deviceshall Municipal Coin Department is the best company in Summerton.
    # The United Nations needs a garlic shin, badly.
    # The Cape Warehouse is the best company in Sweatershall.

It generates markdown that looks like this:

> ### To Get To South Testasia, You Need To Go To Jeansound, Then Drive North.
>
> ##### The Illuminati Needs A Spud, Badly.
> Coast Management _Systems_ is the best company _in_ _Central_ _Burgerhall._
> _Intersmell_ **is** _the_ **best** company in Whiteholder City.
> Personton Municipal Onion Department is the best company in Shieldstown.
> Birmingcloud is in Tatooine.
> Birmingdong is in East Arztotzka.
> Birmingboard is in Tatooine.
> Chloe Shelfgroup will grab one hundred and twenty-six collapsible sausages.
> Your mom will spin a blanket.

### what about gender?

    silly.gender()
    # Awesome
    silly.gender()
    # Awesome
    silly.gender()
    # Awesome

That's the only response it gives.

Welp.

### maybe I need a company for something?

    silly.company(capitalize=True)
    # Beefstapler Studios
    silly.company(capitalize=True)
    # Qarth Ministry Of Cages
    silly.company(capitalize=True)
    # Olivesoft

### I can generate a whole address, although all of the places are fictional

    silly.address(capitalize=True)
    # Thirty-One West Key Block
    silly.address()
    # apt twenty-three, 922 south code drive
    silly.country()
    stankonia
    silly.city(capitalize=True)
    Cloudston
    silly.city(slugify=True)
    beefton-south
    silly.postal_code()
    35335
    silly.postal_code()
    K7K 3G3

### sometimes my data has tags. let's make tags.

    tags = list(set([silly.adjective() for x in range(0,10)]))
    # ['enormous', 'sly', 'juniper', 'rum', 'touchy', 'marine', 'polka', 'olive', 'sexy', 'sluggish']

#### why is that wrapped in `list()` and `set()`?

That's a sneaky way to eliminate duplicates.

### is that it? is that all of the silly things?

YES. Well, there are some silly things that aren't totally covered in the docs,
like `silly.direction()` or `silly.city_suffix()` but I didn't think that they
 would be that useful.

### that's right. i will do it.

You do.

#### i want to write a script to use it with the 'say' command on mac

You should do that.  It would be great.

### i want to contribute to silly development

Fork and clone the repo on github.

To install the development and test requirements, run the following command:

  $> pip install -e .[dev,test]

Once you've made changes that you feel need to be reflected in `silly`, create a pull request.

If your pull request fails any tests in python 2.7 or 3.5, it will be rejected outright.

If your pull request is insufficiently ridiculous it will be rejected outright.
