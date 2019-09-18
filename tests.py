import unittest
from nose.tools import assert_is_not_none
from unittest.mock import Mock, patch
from views import *
from constants import *
import requests
import json
from twilio.base.exceptions import TwilioRestException



# nosetests --verbosity=2 tests.py

class TestTwilioMicroservice(unittest.TestCase):
    # @classmethod
    # def setup_class(cls):
    #     # cls.mock_get_patcher = patch('views.requests.get')
    #     # cls.mock_get = cls.mock_get_patcher.start()
    #     self.app = app.test_client()
    #     self.app.testing = True
    #
    # @classmethod
    # def teardown_class(cls):
    #     cls.mock_get_patcher.stop()
    def setUp(self):
        self.app = app.test_client()

    def tearDown(self):
        pass

    # def test_valid_send_message_action(self):
    #     info = {'message_body': 'Testing Twilio post request', 'phone_number': '+15107897844'}
    #     response = self.app.post('/messages',
    #                              headers={'Content-Type': 'application/json'},
    #                              data=json.dumps(info))
    #     encoded_data = response.data.decode("utf-8")
    #     data = json.loads(encoded_data)
    #     self.assertIn('Testing Twilio post request', data['message_body'])
    #     self.assertIn('15106171282', data['message_from'])
    #     self.assertEqual(response.status_code, 200)

    def test_invalid_send_message_action(self):
        info = {'message_body': 'Testing Twilio post request', 'phone_number': '+99999999999999999'}
        response = self.app.post('/messages',
                                 headers={'Content-Type': 'application/json'},
                                 data=json.dumps(info))
        self.assertEqual(response.status_code, 500)
        self.assertFalse(is_valid_phone_number(info['phone_number']))

    def test_valid_view_message_by_id(self):
        pass

    def test_invalid_view_message_by_id(self):
        pass

    def test_valid_view_all_messages(self):
        result = self.app.get('/filter_by')
        encoded_data = result.data.decode("utf-8")
        data = json.loads(encoded_data)
        self.assertEqual(result.status_code, 200)
        self.assertIn('Sent from your Twilio trial account', data['message_body'])
        self.assertIn('15106171282', data['message_sent_from'])

    def test_invalid_view_all_messages(self):
        pass

    def test_valid_filter_messages_by_sent_to(self):
        pass

    def test_invalid_filter_messages_by_sent_to(self):
        pass

    def test_valid_phone_number(self):
        pass

    def test_invalid_phone_number(self):
        pass

    def test_valid_filter_messages_by_from(self):
        pass

    def test_invalid_filter_messages_by_from(self):
        pass


# TODO write test to make sure user is putting in correct input for phone number
# Error: test_client not working as expected; post request for testing still sending to phone number.
# Error:
if __name__ == '__main__':
    unittest.main()