class Car:

    def __init__(self, model, brand, colour, doors):
        self._model = model
        self._brand = brand
        self._colour = colour
        self._doors = 5
        self._status = 'repose'
        self._engine = Engine(4)

    @property
    def model(self, model):
        return self._model
    
    @model.setter
    def model(self, model):
        self._model = model
    
    @property
    def brand(self, brand):
        return self._brand
    
    @brand.setter
    def brand(self, brand):
        self._brand = brand

    @property
    def colour(self, colour):
        return self._colour

    @colour.setter
    def colour(self, colour):
        self._colour = colour
    
    @property
    def doors(self, doors):
        return self._doors

    @doors.setter
    def doors(self, doors):
        self._doors = doors
    
    @property
    def status(self, status):
        return self._status
    
    @status.setter
    def status(self, status):
        self._status = status
    
    @property
    def engine(self, engine):
        return self._engine
    
    @engine.setter
    def engine(self, engine):
        self._engine = engine

    # Method to convert instance to string
    def __str__(self):
        return f'Model: {self._model} Brand: {self._brand} Colour: {self._colour} Engine: {self._engine}'

class Engine:
    
    def __init__(self, cylinders_number, engine_type = 'gasoline'):
        self._cylinders_number = cylinders_number
        self._engine_type = engine_type

    @property
    def cylinders_number(self, cylinders_number):
        return self._cylinders_number
    
    @cylinders_number.setter
    def cylinders_number(self, cylinders_number):
        self._cylinders_number = cylinders_number
    
    @property
    def engine_type(self, engine_type):
        return self._engine_type
    
    @engine_type.setter
    def engine_type(self, engine_type):
        self._engine_type = engine_type
    
    # Method to convert instance to string
    def __str__(self):
        return f'{self._cylinders_number} - {self._engine_type}'


def run():
    nissan_march = Car('March', 'Nissan', 'White', 5)
    nissan_march.model = "March Active 2020"

    print(nissan_march)

if __name__ == '__main__':
    run()