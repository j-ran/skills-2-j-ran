"""This was unfinished when graded previously; 
now it is complete and returns correctly."""

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
            first_letters_dict[name[0]].append(name)
        # so long as there is name in names
        while first_letters_dict[name[0]]: 
            # use the last letter of the last answer
            # to get the value of the next answer
            start_letter = game_answers[-1][-1]
            # if nothing is there, the function will break
            if not first_letters_dict.get(start_letter):
                break
            # take the first value of the dictionary as an answer
            answer = first_letters_dict[start_letter].pop(0)
            game_answers.append(answer)
    
    return game_answers        


##### TESTING THE FUNCTION #####
names = ["bagon", "baltoy", "yamask", "starly", "nosepass", "kalob", "nicky", "booger"]
names1 = ["apple", "berry", "cherry"]
names2 = ["noon", "naan", "nun"]

print("For list 'names'", kids_game(names))
print("For list 'names2'", kids_game(names1))
print("For list 'names1'", kids_game(names2))