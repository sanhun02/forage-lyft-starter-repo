from battery import Battery
# from datetime import datetime

class NubbinBattery(Battery):
    # def __init__(self, last_service_date, current_date) -> None:
    #     last_service_date = datetime
    #     self.last_service_date = last_service_date
    #     current_date = datetime.today().date()
    #     self.current_date = current_date

    def needs_service(self):
        if self.last_service_date.replace(year=self.last_service_date.year + 4) < self.current_date:
            return True
        else:
            return False
        