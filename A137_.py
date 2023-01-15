class Car:
    def __init__(self, name):
        self.name = name
        self.engine = None
        self.manufacturer = None

    def show(self):
        print(self.name, self.engine)

ferrari = Car('Ferrari')
porsche = Car('Porsche')
mercedes = Car('Mercedes')

class Engine:
    def __init__(self, name):
        self.name = name
        self.car = None

    def show(self):
        print(self.name, self.car)

ferrari_engine = Engine('Ferrari engine')
porsche_engine = Engine('Porsche engine')
mercedes_engine = Engine('Mercedes engine')

class Manufacturer:
    def __init__(self, name):
        self.name = name
        self.car = None

ferrari_manufacturer = Manufacturer('Ferrari manufacturer')
porsche_manufacturer = Manufacturer('Porsche manufacturer')
mercedes_manufacturer = Manufacturer('Mercedes manufacturer')

ferrari.engine = ferrari_engine

print(ferrari.engine)
ferrari_engine.show()
ferrari.show()
