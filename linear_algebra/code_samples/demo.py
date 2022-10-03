

# create a person class
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"{self.name} is {self.age} years old."

    def __repr__(self):
        return f"Person({self.name}, {self.age})"

    def __add__(self, other):
        return f"{self.name} is {self.age + other.age} years old."

    def __sub__(self, other):
        return f"{self.name} is {self.age - other.age} years old."

    def __mul__(self, other):
        return f"{self.name} is {self.age * other.age} years old."

    def __truediv__(self, other):
        return f"{self.name} is {self.age / other.age} years old."

    def __floordiv__(self, other):
        return f"{self.name} is {self.age // other.age} years old."

    def __mod__(self, other):
        return f"{self.name} is {self.age % other.age} years old."

    def __pow__(self, other):
        return f"{self.name} is {self.age ** other.age} years old."

    def __lt__(self, other):
        return self.age < other.age

    def __le__(self, other):
        return self.age <= other.age

    def __eq__(self, other):
        return self.age == other.age

    def __ne__(self, other):
        return self.age != other.age

    def __gt__(self, other):
        return self.age > other.age

    def __ge__(self, other):
        return self.age >= other.age

    def __len__(self):
        return self.age

    def __getitem__(self, index):
        return f"{self.name} is {self.age} years old."

    def __setitem__(self, index, value):
        self.age = value

    def __delitem__(self, index):
        del self.age

    def __call__(self):
        return f"{self.name} is {self.age} years old."

    def __contains__(self, item):
        return item in self.name

    def __iter__(self):
        return iter(self.name)

    def __next__(self):
        return next(self.name)


# create a person object
person = Person("John", 30)

# print the person object
print(person)

# create another person object
person2 = Person("Jane", 25)

# add the two persons
print(person + person2)



