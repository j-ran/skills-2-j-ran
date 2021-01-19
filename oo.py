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

        if self.password == current_password:
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


### from here on is not complete yet!