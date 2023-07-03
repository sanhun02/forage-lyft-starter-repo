from abc import ABC
from car import Car
from datetime import datetime

class CarFactory(ABC):
    def create_calliope(self, current_date, last_service_date, current_mileage, last_service_milelage) -> Car:
        last_service_date = datetime
        self.last_service_date = last_service_date
        current_date = datetime.today().date()
        self.current_date = current_date
        self.current_mileage = current_mileage
        self.last_service_milelage = last_service_milelage

    def create_glissade(self, current_date, last_service_date, current_mileage, last_service_milelage) -> Car:
        last_service_date = datetime
        self.last_service_date = last_service_date
        current_date = datetime.today().date()
        self.current_date = current_date
        self.current_mileage = current_mileage
        self.last_service_milelage = last_service_milelage

    def create_palindrome(self, current_date, last_service_date, warning_light_on) -> Car:
        last_service_date = datetime
        self.last_service_date = last_service_date
        current_date = datetime.today().date()
        self.current_date = current_date
        self.warning_light_on = warning_light_on

    def create_rorschach(self, current_date, last_service_date, current_mileage, last_service_milelage) -> Car:
        last_service_date = datetime
        self.last_service_date = last_service_date
        current_date = datetime.today().date()
        self.current_date = current_date
        self.current_mileage = current_mileage
        self.last_service_milelage = last_service_milelage

    def create_thovex(self, current_date, last_service_date, current_mileage, last_service_milelage) -> Car:
        last_service_date = datetime
        self.last_service_date = last_service_date
        current_date = datetime.today().date()
        self.current_date = current_date
        self.current_mileage = current_mileage
        self.last_service_milelage = last_service_milelage

