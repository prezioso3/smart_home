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

    @patch.object(SmartHome, "measure_lux")
    @patch.object(GPIO, "input")
    def test_turn_light_on(self, mock_sensor_value, mock_light_level):
        mock_light_level.return_value = 490
        mock_sensor_value.return_value = 0
        self.sh.manage_light_level()
        self.assertTrue(self.sh.light_on)

    @patch.object(GPIO, "input")
    def test_turn_light_off(self, mock_sensor_value):
        mock_sensor_value.return_value = 32
        self.sh.manage_light_level()
        self.assertFalse(self.sh.light_on)

    @patch.object(GPIO, "input")
    def test_light_level_valid(self, mock_light_level):
        mock_light_level.return_value = 550
        value = self.sh.measure_lux()
        self.assertEqual(550, value)