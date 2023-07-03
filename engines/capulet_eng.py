from engine import Engine
# from car import Car

class CapuletEngine(Engine):
    # def __init__(self, last_service_milelage, current_mileage):
    #     self.last_service_milelage = last_service_milelage
    #     self.current_milelage = current_mileage

    def needs_service(self):
        if self.current_mileage - self.last_service_milelage >= 30000:
            return True
        else:
            return False