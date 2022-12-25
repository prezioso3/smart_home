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

    @patch.object(GPIO, "input")
    def test_room_occupancy(self, mock_sensor_value):
        mock_sensor_value.return_value = 0
        sh = SmartHome()
        res = sh.check_room_occupancy()
        self.assertTrue(res)

    def test_room_empty(self):
        sh = SmartHome()
        res = sh.check_room_occupancy()
        self.assertFalse(res)