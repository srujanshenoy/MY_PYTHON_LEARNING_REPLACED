from unicodedata import name


class Person:
    def __init__(self, name, sirname):
        self.name = name
        self.sirname = sirname
        self.fullname = name + sirname

    def talk(self):
        print(
            f"Hello there! What is your name? my name is {self.name} and full name is {self.fullname}")


John = Person("John", "Smith")
John.talk()
