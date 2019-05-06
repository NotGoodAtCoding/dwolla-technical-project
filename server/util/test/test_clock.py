"""Unit tests for the clock utility."""
import unittest

from freezegun import freeze_time
from server.util import clock


class ClockTestCase(unittest.TestCase):
    @freeze_time("2019-05-04")
    def test_clock(self):
        self.assertEqual(clock.current_time(),
                         '{"currentTime": "05/04/19 00:00:00"}')
