import unittest
from unittest.mock import patch, PropertyMock

import mock.adafruit_dht as adafruit_dht
import mock.GPIO as GPIO
from SmartHome import SmartHome
from SmartHomeError import SmartHomeError


class SmartHomeTest(unittest.TestCase):
    """
    Your test cases go here
    """

    def test_room_occupancy(self):
        sh = SmartHome()
        res = sh.check_room_occupancy()
        self.assertTrue(res)