"""Discussion Questions

1. What are the three main design advantages that object orientation
   can provide? Explain each concept.

ENCAPSULATION. The term and its data live close to each other
in the code.

ABSTRACTION. You don't need to know all the information 
listed inside a class to use it;
you can call the object without needing to know
what is "encapsulated" in the object.

INHERITANCE. You can pass attributes to objects via classes.

POLYMORPHISM. You can make different types of the same thing; 
more than one kind of class, for instance, – 
as in a Superclass and subclasses. 



2. What is a class?

A Class is a grouping that has attributes;
it can also specify that you do things with methods;
each instance of the Class has the attributes of that Class.
You name Classes with Capitals.
They are defined with the parameter 'self', which instantiates them.
'Self' beings a Class instance into being. 



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

class Road():
    num_lanes=2
    speed_limit=25
    
#instantiate road_1 and road_2
road_1 = Road()
road_2 = Road()

road_1.num_lanes = 4
road_1.speed_limit = 60

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
        return f'"{self.title}" – {self.author}'

# -- test --
book1 = Book("Experience", "Eliasson")
# print(book1)
# -- end of test --

#
# ##
# INSTRUCTIONS:
# We have given you a class, Book. 
# You’ll use it build a new Library class. 
# Your Library class needs to meet these specifications:
#   Each Library object needs an instance attribute called books 
#   which starts off as an empty list.
# We also need two methods:
#     create_and_add_book, 
#     which takes in the title and author of a book (as strings). 
#     It should instantiate a Book object 
#     and add it to the Library’s books list

#     find_books_by_author, 
#     which takes in an author’s name (as a string) 
#     and returns a list of all books by that author
###

class Library():
# class Library:    
    """A collection of books."""

    # make a booklist for the Library
    # instantiate a collection
    def __init__(self):     
        self.books = {}

    def create_and_add_book(self, title, author):
        # instantiate a Book Class object
        # a_book = Book(title, author)
        # use the author to create a list and add the title to the list
        self.books.setdefault(author, []) # setdefault makes a key and value
        self.books[author].append(title)
 
        print(f'The new book is {title} by {author}. The library currently contains: {self.books}')

    def find_books_by_author(self, author): 
        # check if author is in the keys
        if author in self.books:
            return self.books[author]
        print(f"We don't have anything by {author}!")  
        
        # this is one way to alphabetize the dict:
        # sorted_books = sorted(self.books.items())
        # return sorted_books
        # lambda function is easier


### test ###
# my_library = Library()
# my_library.create_and_add_book("Expo", "Larson")
# print(my_library)
# my_library.__dict__ - this is dunder dict, to see the object in a dict
# my_library.create_and_add_book("Expo", "Larson")
# my_library.create_and_add_book("Gene", "Mukherjee")
# my_library.create_and_add_book("Experience", "Eliasson")
# print(my_library)
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

    def __init__(self, length, width):
        """Inherit the definition from Rectangle."""
        # call the Superclass; super is a method and needs ()
        super().__init__(length, width)

    def calculate_sq_area(self):
        print("self.length", self.length)
        print("self.width", self.width)
        if self.length == self.width:
            return super().calculate_area() # this needs to returned EXPLICITLY
        
        else:
            print('Invalid Square')  
            None  

### TESTS ###
rect_1 = Rectangle(3,4)
print('**obj', rect_1)
print('len', rect_1.length)
print('w', rect_1.width)
print('area', rect_1.calculate_area())

square1 = Square(4, 4)
print('sq_area', square1.calculate_sq_area())

# - end of test -   