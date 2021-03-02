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

    melon_prices = {'Honeydew': 2.50,
                    'Cantaloupe': 2.50,
                    'Watermelon': 2.95,
                    'Musk': 3.25,
                    'Crenshaw': 3.25,
                    'Christmas': 14.25}

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
print_melon_at_price(3.25)