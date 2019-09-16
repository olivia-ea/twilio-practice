import unittest
import unittest.mock

class TestTwilioMicroservice(unittest.TestCase):
    def test_valid_response_for_create_sms_function(self):
        # check if phone number is valid
        # check if message body is not empty
        # check status code is not 200 => response will be none
        # if status code is 200 => check if it's in dict format


# TODO look up mocking and stubbing

if __name__ == '__main__':
    unittest.main()