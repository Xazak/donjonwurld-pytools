#import the needed randomness modules
from random import choice, random, randint

def genbook():
    return '%s by %s' % (booktitle(), humanname())

def booktitle():
    i = randint(0, 2)  # 0, 1, or 2
    if i == 0:
        # interpolation is a very powerful way to build strings
        return 'The %s %s' % (adjective().title(), noun().title())
    elif i == 1:
        # .title() is a method of string objects which returns the string title-cased
        return 'A History of %s in %s' % (noun().title(), placename())
    else:
        # if there's only one substitution, you don't need the parens
        return 'The Complete %s' % noun().title()

def humanname():
    # you can also build strings with +
    return choice(['John', 'Mark', 'Luke', 'Michael', 'Tony']) + ' ' + choice(['Johnson', 'Smith', 'Richards', 'Doom', 'Firebrand'])

def adjective():
    return choice(['hot', 'smart', 'super', 'oily', 'lost'])

def noun():
    # do basically the same thing as adjective(), a little more verbosely (and with a bit of extra chance)
    lst = ['duck', 'wood', 'forest', 'gunsmith']
    if random() < .5:  # random generates a float between 0 and 1
        lst.append('slope')  # add to the list
    return choice(lst)

def placename():
    return (adjective() + noun()).title()

# this only executes if this is the main script (not if it's imported by another script)
if __name__ == '__main__':
    for i in range(10):
        print genbook()

