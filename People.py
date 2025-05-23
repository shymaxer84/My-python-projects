class Person:
    number_of_people = 0
    GRAVITY = -9.8

    def __init__(self, name: str):
        self.name = name
        Person.add_person()

    @classmethod
    def number_of_people_(cls):
        return cls.number_of_people

    @classmethod
    def add_person(cls):
        cls.number_of_people += 1


p1 = Person("tim")
print(p1.__dict__)
p2 = Person("lilll")
print(Person.number_of_people_())
