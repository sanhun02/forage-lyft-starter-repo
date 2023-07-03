from engine import Engine
from battery import Battery
from serviceable import Serviceable
from carfactory import CarFactory

class Car(Serviceable, CarFactory):
    def __init__(self, engine, battery):
        engine = Engine
        self.engine = engine
        battery = Battery
        self.battery = battery

    def needs_service(self):
        return self.engine.needs_service() and self.battery.needs_service()
