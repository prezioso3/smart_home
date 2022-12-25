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

    def setUp(self) -> None:
        self.sh = SmartHome()

    @patch.object(GPIO, "input")
    def test_room_occupancy(self, mock_sensor_value):
        mock_sensor_value.return_value = 0
        res = self.sh.check_room_occupancy()
        self.assertTrue(res)

    @patch.object(GPIO, "input")
    def test_room_empty(self, mock_sensor_value):
        mock_sensor_value.return_value = 10
        res = self.sh.check_room_occupancy()
        self.assertFalse(res)

    def test_turn_light_on(self):
        self.sh.manage_light_level()
        self.assertTrue(self.sh.light_on)