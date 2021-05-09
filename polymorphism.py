class Person:

    def __init__(self, firstname, lastname):
        self._firstname = firstname
        self._lastname = lastname
    
    @property
    def firstname(self):
        return self._firstname
    
    @firstname.setter
    def firstname(self, firstname):
        self._firstname = firstname
    
    @property
    def lastname(self):
        return self._lastname
    
    @lastname.setter
    def lastname(self, lastname):
        self._lastname = lastname

    def move(self):
        print('I am walking')
    
class Cyclist(Person):
    
    def __init__(self, firstname, lastname):
        super().__init__(firstname, lastname)
    
    def move(self):
        print('I am riding my bicycle')

def run():
    person_a = Person('Juan', 'Martinez')
    person_a.move()
    cyclist_a = Cyclist('Lio', 'Messi')
    cyclist_a.move()


if __name__ == '__main__':
    run()