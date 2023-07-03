from engine import Engine

class Willoughby(Engine):
    # def __init__(self, last_service_milelage, current_mileage):
    #     self.last_service_milelage = last_service_milelage
    #     self.current_milelage = current_mileage

    def needs_service(self):
        if self.current_mileage - self.last_service_milelage >= 60000:
            return True
        else:
            return False