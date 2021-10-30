class Pet:
    def __init__(self, name) -> None:
        self._name = name

    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, value):
        self._name = value
        return self._name

pet = Pet('Max')
pet.name = 'Oscar'
print(pet.__dict__)