"""Dictionaries Assessment

**IMPORTANT:** These problems are meant to be solved using
dictionaries and sets.
"""

def count_words(phrase):
    """Count unique words in a string.

    This function should take a single string and return a dictionary
    that has all of the distinct words as keys and the number of
    times that word appears in the string as values.

    For example::

        >>> print_dict(count_words("each word appears once"))
        {'appears': 1, 'each': 1, 'once': 1, 'word': 1}

    Words that appear more than once should be counted each time::

        >>> print_dict(count_words("rose is a rose is a rose"))
        {'a': 2, 'is': 2, 'rose': 3}

    It's fine to consider punctuation part of a word (e.g., a comma
    at the end of a word can be counted as part of that word) and
    to consider differently-capitalized words as different::

        >>> print_dict(count_words("Porcupine see, porcupine do."))
        {'Porcupine': 1, 'do.': 1, 'porcupine': 1, 'see,': 1}
    """

# create an empty list for the words in the phrase
    all_words = []
# create an empty dictionary to take the word:word-count pairs     
    word_counts = {}
# split the phrase on spaces so that there are words (rather than ind. letters)
# sort the result so the words enter the dictionary in alpha-order
    phrase = sorted(phrase.split())

# go word by word and add to list 'all_words' 
# then get the count of each of the unique words in the list
# by using dictionary syntax (which creates unique keys from the 'all_words' list)
    for word in phrase:
        all_words.append(word)
        word_counts[word] = word_counts.get(word, 0) + 1
    return word_counts

# - test the function -
# phrase = "Porcupine see, porcupine do."
# phrase = "rose is a rose is a rose"
# phrase = "each word appears once or each word appears twice"
# print(count_words(phrase))



def print_melon_at_price(price):
    """Given a price, print all melons available at that price, in alphabetical order.

    Here are a list of melon names and prices:

    Honeydew 2.50
    Cantaloupe 2.50
    Watermelon 2.95
    Musk 3.25
    Crenshaw 3.25
    Christmas 14.25
    (it was a bad year for Christmas melons -- supply is low!)

    If there are no melons at that price print "None found"

        >>> print_melon_at_price(2.50)
        Cantaloupe
        Honeydew

        >>> print_melon_at_price(2.95)
        Watermelon

        >>> print_melon_at_price(5.50)
        None found
    """

# PLEASE NOTE: 
# I started this by making a separate file to hold the text. 
# This is in lines 85-100.

# # create text for the function from the given text 
#     price_list = open('melon_prices.txt')
# # format the text so that melon name and price are paired in a dictionary
#     # distinguish each line
#     # make key:value pairs from each line
#     # add the new key:value into the dict 'melon_prices'

#     melon_prices = {}

#     for line in price_list:
#         split_line = line.lstrip().rstrip().split()
#     # define the keys and values
#         melon = split_line[0]
#         melon_price = split_line[-1]
#     # add a new entry to the dictionary
#         melon_prices[melon] = melon_price

# Here, I write the dictionary into the function:

    melon_prices = {'Honeydew': '2.50',
                    'Cantaloupe': '2.50',
                    'Watermelon': '2.95',
                    'Musk': '3.25',
                    'Crenshaw': '3.25',
                    'Christmas': '14.25'}

    # make a list to hold the names of melons which cost the requested price
    melons_to_print = []

    # use '.items' to run through the dictionary
    for melon, melon_price in melon_prices.items():
        if price == melon_price:
            melons_to_print.append(melon)
            melons_to_print = sorted(melons_to_print)  
    
    if bool(melons_to_print) == False:
        print("None found")
    else:    
        for i in melons_to_print:
            print(i)

# - test -
# print_melon_at_price('3.25')


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

# attempt_01
# This doesn't work because a small word like "is" could get
# incorrectly replaced
# name the parts of the dictionary with '.items()'
    # for english_word, pirate_word in pirate_dict.items():
    #     # look for dict keys
    #     if english_word in phrase:
    #         # replace the word and keep the structure of the phrase
    #         phrase = phrase.replace(english_word, pirate_word)
    # return phrase

# attempt_02
# everything works; trying to deal with punctuation

    words = phrase.rstrip().split()
    puncs = ["!", "?"]

#make an empty list
    clean_list = []
    for word in words:
        clean_list.append(word)
        # if char in words has punc - THIS IS NOT IDEAL, THE CODE IS WET ...
        for punc in puncs:
            if punc in word:
            # the following is to create two list items,
            # an item of the word and an item of its punctuation, 
            # to replace the single item of "word+punctuation"  
                word_clean = word.replace("!", " ").replace('?',' ').split()
                word_plus = word_clean[0]
                clean_list.pop()
                clean_list.append(word_plus)
                clean_list.append(punc)  
    #print(clean_list)
    
    #now we are ready to translate! 
    #make empty list
    translation = []
    for word in clean_list:
        if word not in pirate_dict.keys():
            translation.append(word)
        else:
            translation.append(pirate_dict.get(word))  
    
    #print(translation)

    complete_trans = " ".join(translation)
    return complete_trans   


# - test -
# print(translate_to_pirate_talk("What is this hotel room, man? The restroom resembles a student restaurant! What is your excuse?"))
# result of print statement is: "What be this fleabag inn room, matey ? The head resembles a swabbie galley ! What be yer arr ?"
# note: ALMOST there. The punctuation has spaces around it. I am stopping here, though, as that is not a dicitonary problem.


def kids_game(names):
    """Play a kids' word chain game.

    Given a list of names, like::

      bagon baltoy yamask starly nosepass kalob nicky

    Do the following:

    1. Always start with the first word ("bagon", in this example).

    2. Add it to the results.

    3. Use the last letter of that word to look for the next word.
       Since "bagon" ends with n, find the *first* word starting
       with "n" in our list --- in this case, "nosepass".

    4. Add "nosepass" to the results, and continue. Once a word has
       been used, it can't be used again --- so we'll never get to
       use "bagon" or "nosepass" a second time.

    5. When you can't find an unused word to use, you're done!
       Return the list of output words.

    For example::

        >>> kids_game(["bagon", "baltoy", "yamask", "starly",
        ...            "nosepass", "kalob", "nicky", "booger"])
        ['bagon', 'nosepass', 'starly', 'yamask', 'kalob', 'baltoy']

    (After "baltoy", there are no more y-words, so we end, even
    though "nicky" and "booger" weren't used.)

    Two more examples:

        >>> kids_game(["apple", "berry", "cherry"])
        ['apple']

        >>> kids_game(["noon", "naan", "nun"])
        ['noon', 'naan', 'nun']

    This is a tricky problem. In particular, think about how using
    a dictionary (with the super-fast lookup they provide) can help;
    good solutions here will definitely require a dictionary.
    """

    first_letters_dict = {}
    game_answers = [names.pop(0)]
        
    for name in names:
        # create keys from the unique first letters of the names list
        if name[0] not in first_letters_dict:
            first_letters_dict[name[0]] = [name]

        else:
            # add the name to the dictionary 
            # as an additional value of its initial letter
            first_letters_dict[name[0]].append(name)
        

        # the following statement could also be 'while True:'
        # it means "while the key returns a value other than None"
        # in other words, so long as the key exists, or, in this case, 
        # so long as there is name in names so that there is a name[0]
        while first_letters_dict[name[0]]: 
            # use the last letter of the last answer
            # to get the value of the next answer
            start_letter = game_answers[-1][-1]
            # this checks that there are values 
            # other than None at start-letter key
            # if nothing is there, the function will break
            if not first_letters_dict.get(start_letter):
                print(f'Checking eligible values ...')
                break
            print(f"Then start w/ '{start_letter}' ...")
            # take the first value at the key out of the dictionary
            answer = first_letters_dict[start_letter].pop(0)
            print(f"Add {answer}.")
            game_answers.append(answer)
    print(f'Game answers are: {game_answers}.') 

names1 = ["apple", "berry", "cherry"]
names2 = ["noon", "naan", "nun"]
names = ["bagon", "baltoy", "yamask", "starly", "nosepass", "kalob", "nicky", "booger"]
kids_game(names)
