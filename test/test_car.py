import unittest
from datetime import datetime

from battery.nubbin_bat import NubbinBattery
from battery.spindler_bat import SpindlerBattery
from engine.capulet_eng import CapuletEngine
from engine.sternman_eng import SternmanEngine
from engine.willoughby_eng import WilloughbyEngine

class TestEngine(unittest.TestCase):
    def test_capulet_needs_service(self):
        last_service_milelage = 10000
        current_milelage = 50000
        capulet_eng = CapuletEngine(last_service_milelage, current_milelage)

        self.assertTrue(capulet_eng.needs_service())

    def test_capulet_no_service(self):
        last_service_milelage = 10000
        current_milelage = 20000
        capulet_eng = CapuletEngine(last_service_milelage, current_milelage)

        self.assertFalse(capulet_eng.needs_service())

    def test_sternman_needs_service(self):
        warning_light_on = True
        sternman_eng = SternmanEngine(warning_light_on)

        self.assertTrue(sternman_eng.needs_service())

    def test_sternman_needs_service(self):
        warning_light_on = False
        sternman_eng = SternmanEngine(warning_light_on)

        self.assertFalse(sternman_eng.needs_service())

    def test_willoughby_needs_service(self):
        last_service_milelage = 10000
        current_milelage = 80000
        capulet_eng = WilloughbyEngine(last_service_milelage, current_milelage)

        self.assertTrue(capulet_eng.needs_service())

    def test_capulet_no_service(self):
        last_service_milelage = 10000
        current_milelage = 20000
        capulet_eng = WilloughbyEngine(last_service_milelage, current_milelage)

        self.assertFalse(capulet_eng.needs_service())

class TestBattery(unittest.TestCase):
    def test_nubbin_needs_service(self):
        current_date = datetime.today().date()
        last_service_date = current_date.replace(year=current_date.year - 5) 
        nubbin_bat = NubbinBattery(current_date, last_service_date)

        self.assertTrue(nubbin_bat.needs_service())

    def test_nubbin_no_service(self):
        current_date = datetime.today().date()
        last_service_date = current_date.replace(year=current_date.year - 1) 
        nubbin_bat = NubbinBattery(current_date, last_service_date)

        self.assertFalse(nubbin_bat.needs_service())

    def test_spindler_needs_service(self):
        current_date = datetime.today().date()
        last_service_date = current_date.replace(year=current_date.year - 3) 
        spindler_bat = SpindlerBattery(current_date, last_service_date)

        self.assertTrue(spindler_bat.needs_service())

    def test_spindler_no_service(self):
        current_date = datetime.today().date()
        last_service_date = current_date.replace(year=current_date.year - 1) 
        spindler_bat = SpindlerBattery(current_date, last_service_date)

        self.assertFalse(spindler_bat.needs_service())

if __name__ == '__main__':
    unittest.main()
