from flask import Flask, request
from constants import *
from twilio.base.exceptions import TwilioRestException

app = Flask(__name__)

def is_valid_phone_number(phone_number):
    response = CLIENT.lookups.phone_numbers(phone_number).fetch()
    if response.status_code == 200:
        return True
    else:
        return False

@app.route('/messages', methods=['POST'])
def send_message_action():
    request_body = request.get_json()
    phone_number = request_body['phone_number']
    if is_valid_phone_number(phone_number):
        message = CLIENT.messages.create(
                                         body=request_body['message_body'],
                                         from_=TWILIO_PHONE_NUMBER,
                                         to=request_body['phone_number']
                                         )
        message_dict = {}
        message_dict['message_sid'] = message.sid
        message_dict['message_to'] = message.to
        message_dict['message_from'] = message.from_
        message_dict['message_body'] = message.body
        return message_dict
    else:
        # raise ValueError('Not a valid phone number!')
        return 404

@app.route('/messages/<message_id>', methods=['GET'])
def view_message_by_id(message_id):
    message = CLIENT.messages(message_id).fetch()
    message_dict = {}
    message_dict['account_sid'] = message.account_sid
    message_dict['api_version'] = message.api_version
    message_dict['message_body'] = message.body
    message_dict['date_created'] = message.date_created
    return message_dict

@app.route('/filter_by', methods=['GET'])
def view_all_messages():
    messages = CLIENT.messages.list(limit=100)
    filtered_dict = {}
    for message in messages:
        filtered_dict['message_sid'] = message.sid
        filtered_dict['message_sent_to'] = message.to
        filtered_dict['message_sent_from'] = message.from_
        filtered_dict['message_body'] = message.body
    return filtered_dict

@app.route('/filter_by/sent/<phone_number>', methods=['GET'])
def filter_messages_by_sent_to(phone_number):
    messages = CLIENT.messages.list(limit=100)
    phone_number = '+1' + str(phone_number)
    filtered_dict = {}
    for message in messages:
        if message.to == phone_number:
            filtered_dict['message_sid'] = message.sid
            filtered_dict['message_sent_to'] = message.to
            filtered_dict['message_body'] = message.body
    return filtered_dict

@app.route('/filter_by/from/<phone_number>', methods=['GET'])
def filter_messages_by_from(phone_number):
    messages = CLIENT.messages.list(limit=100)
    phone_number = '+1' + str(phone_number)
    filtered_dict = {}
    for message in messages:
        if message.from_ == phone_number:
            filtered_dict['message_sid'] = message.sid
            filtered_dict['message_sent_from'] = message.from_
            filtered_dict['message_body'] = message.body
    return filtered_dict

# TODO add error handling to check if vaild phone number for /messages and /filter_by urls