"""Discussion Questions

1. What are the three main design advantages that object orientation
   can provide? Explain each concept.

ENCAPSULATION. The term and its data live close to each other
in the code.

ABSTRACTION. You don't need to know all the information 
listed inside a class to use it;
you can call the object without needing to know
what is "encapsulated" in the object.

POLYMORPHISM. You can make different types of the same thing; 
more than one kind of class, for instance, – 
as in a Superclass and subclasses. 



2. What is a class?

A Class is a grouping that has attributes;
it can also specify that you do things with methods;
each instance of the Class has the attributes of that Class.
You name Classes with Capitals.



3. What is a method?

A method is like a function, but it is called on a Class.
Its first argument is "self," which Python passes automatically.



4. What is an instance in object orientation?

An instance is when you instantiate a Class;
it's a specific use-case of the Class. 
An instance can also be referred to as an object.



5. How is a class attribute different than an instance attribute?
   Give an example of when you might use each.

Class attributes are shred by all the instances of that class.
Instance attributes belong only to that instance. 

If we want to create a dog named Fido, 
it would be an object whose Class is Animal with the attribute dog,
and the instance attribute would be the name "Fido."

A second dog named Pierre
would be an object whose Class is Animal with the attribute dog,
and Pierre would have the instance attribute of a name, "Pierre."

class Animal:
    species = 'dog'

>>> fido = Animal()
>>> fido.species
dog
>>> fido.name = 'Fido'

"""


"""2. Road Class"""

class Road:
    def __init__(self, num_lanes = 2, speed_limit = 25):
        """Create a road with defined attributes."""
        self.num_lanes = num_lanes
        self.speed_limit = speed_limit

#instantiate road_1 and road_2
road_1 = Road()
road_2 = Road()

#update road_1
road_1 = Road(4, 60)

# - test -
# print(road_1.num_lanes)
# print(road_1.speed_limit)



"""3. Update Password"""


class User:
    """A user object."""

    def __init__(self, username, password):
        """Create a user with the given username and password."""

        self.username = username 
        self.password = password   

    def update_password(self, current_password, new_password): 
        """Create a new password after entering current password."""

        if current_password == self.password: 
            self.password = new_password    
        else:
            print('Invalid password')

# # - test -
# # instantiate a User by passing in a username and password
# mimi = User("mimi", "my_password")
# print(mimi.password)
# # run the method to update the user's password
# mimi.update_password("my_password", "new")
# print(mimi.password)
# #- end of test -



"""4. Build a Library"""


class Book:
    """Create a Book object."""

    def __init__(self, title, author):
        """Instantiate a book with the given title and author."""

        self.title = title
        self.author = author

    # see what we've got
    def __repr__(self):
        return f'"{self.title}" by {self.author}'

# -- test --
# book1 = Book("Experience", "Eliasson")
# print(book1)
# -- end of test --


class Library:
# class Library:    
    """A collection of books."""

    # no attributes passed in; instantiate an empty list
    def __init__(self): 
        """Create a book with the given title and author."""

        self.books = {}
#### shoot, I got stuck here again!!!!
    def create_and_add_book(self, title, author):
        """Make a Book object and append it to books list,
            i.e. add to Library."""
        
        self.books[author] = title
        # self.books.append(Book(title, author))
        # bookshelf = {books}
        print(self.books[author])
        # bookshelf[author] = title
        # sorted_bookshelf = sorted(bookshelf)
        # print(sorted_bookshelf)
    # list the books in this instance of the library
    def __repr__(self):    
        return f"My library is organized by author: {self.books}"

# note :: did not alphabetize by author
# -- test --
my_library = Library()
my_library.create_and_add_book("Expo", "Larson")
my_library.create_and_add_book("Gene", "Mukherjee")
my_library.create_and_add_book("Experience", "Eliasson")
print(my_library)
# -- end of test --



"""5. Rectangle"""


class Rectangle:
    """A rectangle."""

    def __init__(self, length, width):
        """Create a rectangle with the given length and width."""

        self.length = float(length)
        self.width = float(width)

    def calculate_area(self):
        """Return the area of the rectangle."""

        return self.length * self.width


class Square(Rectangle):
    """A particular kind of rectangle."""

    def __init__(self, length):
        """Create a rectangle with the same length and width."""
        # call the Superclass and make both dimensions equal to length 
        super().__init__(length, length)


# - test -
# instantiate a Square
a_square = Square(4)
# check that it has a width, inherited from Rectangle
print(a_square.width)
# calculate area of Square, a method inherited from Rectangle
print(a_square.calculate_area())
# - end of test -   