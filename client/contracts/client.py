import atexit
import unittest

from pact import Consumer, Provider, Term

from ..main import get_time


pact = Consumer('Consumer').has_pact_with(
    Provider('Provider'), port=5001)
pact.start_service()
atexit.register(pact.stop_service)


class GetUserInfoContract(unittest.TestCase):
    def test_get_time(self):
        expected = {
          'currentTime': Term(
              '\d+-\d+-\d \d+:\d+:\d+',  # noqa W605
              '2016-12-15 20:16:01')
        }

        (pact
         .given('A request is made for the current time')
         .upon_receiving('a request for current time')
         .with_request('get', '/')
         .will_respond_with(200, body=expected))

        with pact:
            result = get_time()

        self.assertEqual(result, expected)
