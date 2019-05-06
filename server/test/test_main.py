import unittest
from mock import patch

from server import main
from server.util import clock


class ClockTestCase(unittest.TestCase):
    def setUp(self):
        self.addCleanup(patch.stopall)
        self.mock_clock = patch.object(
            clock, 'current_time'
        ).start()

    def test_clock(self):
        # Arrange
        self.mock_clock.return_value = 'time'
        # Act
        result = main.main()
        # Assert
        self.assertEqual(result, 'time')
