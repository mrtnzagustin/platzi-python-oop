class Coor2D:

    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def distance(self, other_coor):
        x_diff = (self.x - other_coor.x)**2
        y_diff = (self.y - other_coor.y)**2

        return (x_diff + y_diff)**0.5

def run():
    coor1 = Coor2D(3, 30)
    coor2 = Coor2D(4, 8)

    print(f'Distance between coords {coor1.distance(coor2)}')

    # Check if object is instance of a specific class
    print(f'Is instance: {isinstance(coor1, Coor2D)}')

if __name__ == '__main__':
    run()
