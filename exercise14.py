class Pet:
    def __init__(self, name, age) -> None:
        self._name = name
        self._age = age

    @property
    def name(self):
        return self._name

    @name.setter
    def name_set(self, value):
        self._name = value

    @property
    def age(self):
        return self._age

    @age.setter
    def age_set(self, value):
        self._age = value

pet = Pet('Max', 5)

print(pet.__dict__)

pet.name_set = 'Tom'
pet.age_set = 8

print(pet.__dict__)