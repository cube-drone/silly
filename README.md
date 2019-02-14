# Silly
A python library for producing fanciful test data.

## Why silly?

Sometimes I need more test data than just "Testy Testerson" at "123 Fake St."

`silly` can be used to generate data for things, names, dates, addresses, text...

## I want advanced features OR this data is not very professional looking!

Silly is designed to be quick, funny, and dumb.

If you want localization, customization, and data that doesn't contain the word "poopbutt",
you're probably going to want to look at [faker](https://github.com/joke2k/faker) instead.

## Installation

    pip install silly


## How to use

    import silly

### Generating Contact Information

    name = silly.name()
    print("my name is {}".format(name))
    # my name is colonel beefheart

    print("you should not contact me at {}".format(silly.email()))
    # you should not contact me at buttpike@chump-lol.xyz


### Capitalization and Slugification

    # this works on everything that it would make sense for it to work on
    #   for everything else it should fail silently
    #       like me

    silly.name(capitalize=True)
    # Colonel Travis Coffeesecrets
    silly.name(slugify=True)
    # carol-kittenmatt


### Generating Dates and Times

    year, month, day = silly.datetime().year, silly.datetime().month, silly.datetime().day
    # 1983, 12, 28

### Generating Numbers

    number = silly.number()
    print(number)
    # 7
    number_in_words = silly.numberwang()
    print(number_in_words)
    # Eighty Eight

### Generating Words

    silly.noun()
    # arm
    silly.verb()
    # jump
    silly.adjective()
    # musky
    silly.plural()
    # kittens

### Generating a Past Participle

    silly.past_participle()
    # Traceback (most recent call last):
    # File "<stdin>", line 1, in <module>
    # AttributeError: module 'main' has no attribute 'past_participle'

Damn.

### Generating... Things

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

### ...or Lots of Things

    silly.things()
    # a bunch of hats, a tub of hams, and ninety jeans

### Generating Domains

    silly.domain()
    # pants.xyz

### Generating Phone Numbers

    silly.phone_number()
    # 555-6868

### Generate an Image

    silly.image()
    # http://dummyimage.com/800x600/292929/e3e3e3&text=mighty poop

    silly.image(width=1000, height=60)
    # http://placekitten.com/1000/60

    silly.image(https=True, width=40, height=50)
    # https://dummyimage.com/40x50/292929/e3e3e3&text=house

### Generate a Whole Sentence...

    silly.sentence()
    # Your dad will head to Integrated Harvest And Secret to buy a shell boat.

### ...Or Even a Paragraph!

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

### Generate Some Markdown

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

### Generate a Gender

    silly.gender()
    # Awesome
    silly.gender()
    # Multitudes
    silly.gender()
    # Nil

### Generate a Company

    silly.company(capitalize=True)
    # Beefstapler Studios
    silly.company(capitalize=True)
    # Qarth Ministry Of Cages
    silly.company(capitalize=True)
    # Olivesoft

### Generate Whole Addresses (all fictional, of course)

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

### Generate some tags

    tags = list(set([silly.adjective() for x in range(0,10)]))
    # ['enormous', 'sly', 'juniper', 'rum', 'touchy', 'marine', 'polka', 'olive', 'sexy', 'sluggish']

#### why is that wrapped in `list()` and `set()`?

That's a sneaky way to eliminate duplicates.

### Is there more!?

YES. Well, there are some silly things that aren't totally covered in the docs,
like `silly.direction()` or `silly.city_suffix()` but I didn't think that they
 would be that useful.

### That's Right. I will do it.

You do.

#### I Want to Write a Script to Use `silly` With the 'say' Command on Mac

You should do that.  It would be great.

### I Want to Contribute to Silly Development

Fork and clone the repo on github.

To install the development and test requirements, run the following command:

    $> pip install -e .[dev,test]

Once you've made changes that you feel need to be reflected in `silly`, create a pull request.

If your pull request fails any tests in python 2.7 or 3.5, it will be rejected outright.

If your pull request is insufficiently ridiculous it will be rejected outright.
