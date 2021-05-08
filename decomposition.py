class Car:

    def __init__(self, model, brand, colour, doors):
        self.model = model
        self.brand = brand
        self.colour = colour
        self.doors = 5
        self._status = 'repose'
        self._engine = Engine(4)

    def acelerate(self, aceleration_type = 'slow'):
        if aceleration_type == 'slow':
            self._engine.inject_gasoline(3)
        elif aceleration_type == 'fast':
            self._engine.inject_gasoline(10)

        self._status = 'movement'
    
    # Method to convert instance to string
    def __str__(self):
        return f'Model: {self.model} Brand: {self.brand} Colour: {self.colour} Engine: {self._engine}'

class Engine:
    
    def __init__(self, cylinders_number, engine_type = 'gasoline'):
        self.cylinders_number = cylinders_number
        self.engine_type = engine_type

    def inject_gasoline(self, amount):
        pass
    
    # Method to convert instance to string
    def __str__(self):
        return f'{self.cylinders_number} - {self.engine_type}'


def run():
    nissan_march = Car('March', 'Nissan', 'White', 5)

    print(nissan_march)

if __name__ == '__main__':
    run()