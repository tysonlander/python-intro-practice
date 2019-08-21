# A class is like a blueprint for creating objects. An object has properties and methods(functions) associated with it. Almost everything in Python is an object


class User:
    # Constructor
    def __init__(self, name, email, age):
        self.name = name
        self.email = email
        self.age = age

    def has_birthday(self):
        self.age += 1

    def greeting(self):
        return f"My name is {self.name} and I am {self.age}"


class Customer(User):
    # Constructor
    def __init__(self, name, email, age):
        self.name = name
        self.email = email
        self.age = age
        self.balance = 0

    def set_balance(self, balance):
        self.balance = balance

    def greeting(self):
        return f"My name is {self.name} and I am {self.age} and I owe a balance of {self.balance}"


# Init user object
tyson = User("Tyson Lander", "myemail@gmail.com", 30)
john = User("John doe", "john@gmail.com", 25)

# Edit property
tyson.age = 29

john.has_birthday()

# Call method
# print(john.greeting())


# Init customer
jane = Customer("Jane Doe", "jane@gmail.com", 40)

jane.set_balance(500)

print(john.greeting())

