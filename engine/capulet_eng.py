from engine.engine import Engine

class CapuletEngine(Engine):
    def __init__(self, last_service_milelage, current_milelage):
        self.last_service_milelage = last_service_milelage
        self.current_milelage = current_milelage

    def needs_service(self):
        return self.current_milelage - self.last_service_milelage > 30000
        