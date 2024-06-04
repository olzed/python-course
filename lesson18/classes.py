class Vehicle:
    def __init__(self, make, model):
        self.make = make
        self.model = model
    def moves(self):
        print('Moves along...')
        
    def get_make_model(self):
        print(f"I'm a {self.make} {self.model}.")
        
my_car = Vehicle('Tesla', 'Model 3')

# print(my_car.make)
# print(my_car.model)

my_car.get_make_model()
my_car.moves()

your_car = Vehicle('Cadillac', 'Escalade')
your_car.get_make_model()
your_car.moves()

class Airplane(Vehicle):
    def __init__(self, make, model, faa_id):
        super().__init__(make, model) # inherits from parent class
        self.faa_id = faa_id
    
    def moves(self):
        print('Flies along...')
        
class Truck(Vehicle):
    def moves(self):
        print('Rumbles along...')
        
class GolfCart(Vehicle):
    pass # inherits everything as is

airplane = Airplane('Cessna', 'Skyhawk', 'N-12345')
truck = Truck('Mack', 'Pinnacle')
golfwagon = GolfCart('Yamaha', 'GC100')

airplane.get_make_model()
airplane.moves()
truck.get_make_model()
truck.moves()
golfwagon.get_make_model()
golfwagon.moves()

print('\n\n')

# polymorphism
# gets everything and prints it
for v in (my_car, your_car, airplane, truck, golfwagon):
    v.get_make_model()
    v.moves()