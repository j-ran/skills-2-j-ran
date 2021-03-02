"""In response to comment:
 'You should treat words with punctuation as if they were different words: 
> translate_to_pirate_talk("my student is not a man!")
> 'me swabbie be not a man!'

This function now treats 'man' and 'man!' as different entities."""

def translate_to_pirate_talk(phrase):
    """Translate phrase to pirate talk.

    Given a phrase, translate each word to the Pirate-speak
    equivalent. Words that cannot be translated into Pirate-speak
    should pass through unchanged. Return the resulting sentence.

    Here's a table of English to Pirate translations:

    ----------  ----------------
    English     Pirate
    ----------  ----------------
    sir         matey
    hotel       fleabag inn
    student     swabbie
    man         matey
    professor   foul blaggart
    restaurant  galley
    your        yer
    excuse      arr
    students    swabbies
    are         be
    restroom    head
    my          me
    is          be
    ----------  ----------------



    For example::

        >>> translate_to_pirate_talk("my student is not a man")
        'me swabbie be not a matey'

    You should treat words with punctuation as if they were different
    words::

        >>> translate_to_pirate_talk("my student is not a man!")
        'me swabbie be not a man!'
    """

# create the dictionary
    pirate_dict = {"sir": "matey",
                    "hotel": "fleabag inn",
                    "student": "swabbie",
                    "man": "matey",
                    "professor": "foul blaggart",
                    "restaurant": "galley",
                    "your": "yer",
                    "excuse": "arr",
                    "students": "swabbies",
                    "are": "be",
                    "restroom": "head",
                    "my": "me",
                    "is": "be"}


    words = phrase.rstrip().split()

    translation = []
    for word in words:
        if word not in pirate_dict.keys():
            translation.append(word)
        else:
            translation.append(pirate_dict.get(word))  

    complete_trans = " ".join(translation)
    return complete_trans   

print(translate_to_pirate_talk("my student is not a man"))
print(translate_to_pirate_talk("my student is not a man!"))