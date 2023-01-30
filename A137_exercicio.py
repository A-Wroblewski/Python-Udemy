class Car:
    def __init__(self, name):
        self.name = name
        self._engine = None
        self._manufacturer = None

    @property
    def engine(self):
        return self._engine

    @engine.setter
    def engine(self, name):
        self._engine = name

    @property
    def manufacturer(self):
        return self._manufacturer

    @manufacturer.setter
    def manufacturer(self, name):
        self._manufacturer = name

class Engine:
    def __init__(self, name):
        self.name = name

class Manufacturer:
    def __init__(self, name):
        self.name = name

ferrari = Car('Ferrari')
porsche = Car('Porsche')
mercedes = Car('Mercedes')

ferrari_engine = Engine('Ferrari engine')
porsche_engine = Engine('Porsche engine')
mercedes_engine = Engine('Mercedes engine')

ferrari_manufacturer = Manufacturer('Ferrari manufacturer')
porsche_manufacturer = Manufacturer('Porsche manufacturer')
mercedes_manufacturer = Manufacturer('Mercedes manufacturer')

ferrari.engine = ferrari_engine
ferrari.manufacturer = ferrari_manufacturer

print(ferrari.name)
print(ferrari.engine.name)
print(ferrari.manufacturer.name, '\n')

porsche.engine = mercedes_engine
porsche.manufacturer = porsche_manufacturer

print(porsche.name)
print(porsche.engine.name)
print(porsche.manufacturer.name, '\n')

mercedes.engine = porsche_engine
mercedes.manufacturer = ferrari_manufacturer

print(mercedes.name)
print(mercedes.engine.name)
print(mercedes.manufacturer.name)
