class Person:

    instances = []

    def __init__(self, first_name, last_name):
        
        self.first_name = first_name
        self.last_name = last_name
        Person.instances.append(self)
    
    @classmethod
    def count_instances(cls):
        return len(Person.instances)

p1 = Person('John', 'Smith')
p2 = Person('Kate', 'Moss')

print(p1.count_instances())