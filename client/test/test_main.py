"""Client unit tests."""
import unittest
from mock import MagicMock, Mock, patch
from click.testing import CliRunner

from .. import main


class ClientTestCase(unittest.TestCase):
    def setUp(self):
        self.addCleanup(patch.stopall)
        self.mock_request = patch.object(
            main.requests, 'get'
        ).start()
        self.mock_request.return_value = MagicMock(
            json=Mock(return_value='neat'))

        patch.object(main.time, 'sleep').start()

    def test_main(self):
        """Test main path with no additional args."""
        # Arrange

        # Act
        runner = CliRunner()
        response = runner.invoke(main.get_time)
        # Assert
        self.assertEqual(response.exit_code, 0)
        self.assertIn('neat', response.output)
        self.mock_request.assert_called_with(
            'http://localhost:5001')
        self.assertEqual(self.mock_request.call_count, 5)

    def test_main_three_tries(self):
        """Test only repeating three times."""
        # Arrange

        # Act
        runner = CliRunner()
        response = runner.invoke(
            main.get_time, ['--repeat', 3])
        # Assert
        self.assertEqual(response.exit_code, 0)
        self.assertIn('neat', response.output)
        self.mock_request.assert_called_with(
            'http://localhost:5001')
        self.assertEqual(self.mock_request.call_count, 3)

    def test_main_supplied_hostname(self):
        """Test supplying an alternate hostname."""
        # Arrange

        # Act
        runner = CliRunner()
        response = runner.invoke(
            main.get_time, ['--hostname', 'test'])
        # Assert
        self.assertEqual(response.exit_code, 0)
        self.mock_request.assert_called_with(
            'http://test:5001')
