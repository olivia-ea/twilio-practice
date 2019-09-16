from flask import Flask, request
from twilio.rest import Client

# TODO make credentials environment vars
twilio_phone_number = '+15106171282'
personal_phone_number = '+15106487309'
twilio_account_sid = 'AC3050c3bf79b5dd9f74ea488e99f06297'
twilio_auth_token = '994dbb8e2b8e10188a7fdf1228d57926'

app = Flask(__name__)

# @app.route is a route decorator that tells Flask that the URL should trigger a specific function
# also route decorator binds function to URL
@app.route('/messages', methods=['POST']) # /messages/ needs to be POST not get (to use headers and format message)
def send_message():
    client = Client(twilio_account_sid, twilio_auth_token)
    request_body = request.get_json()   # test using postman => run server, post request 'http://localhost:5000/messages', headers => key = Content-Type, value = application/json, body => select raw and put in json and select json as format type
    message = client.messages.create(
                              body=request_body['message_body'],
                              from_=twilio_phone_number,
                              to=request_body['phone_number']
                              )
    message_dict = {}
    message_dict['message_sid'] = message.sid
    message_dict['message_to'] = message.to
    message_dict['message_from'] = message.from_
    message_dict['message_body'] = message.body
    return message_dict

@app.route('/messages/<message_id>', methods=['GET']) # /message/<message_id>
def read_message(message_id):
    client = Client(twilio_account_sid, twilio_auth_token)
    message = client.messages(message_id).fetch()
    message_dict = {}
    message_dict['account_sid'] = message.account_sid
    message_dict['api_version'] = message.api_version
    message_dict['message_body'] = message.body
    message_dict['date_created'] = message.date_created
    return message_dict

@app.route('/filter_by', methods=['GET'])
def filter_all():
    client = Client(twilio_account_sid, twilio_auth_token)
    messages = client.messages.list(limit=100)
    filtered_dict = {}
    for message in messages:
        filtered_dict[message.sid] = message.body
    return filtered_dict

@app.route('/filter_by/sent/<phone_number>', methods=['GET'])
def filter_sent_to(phone_number):
    client = Client(twilio_account_sid, twilio_auth_token)
    messages = client.messages.list(limit=100)
    phone_number = '+1' + str(phone_number)
    filtered_dict = {}
    for message in messages:
        if message.to == phone_number:
            filtered_dict['message_sid'] = message.sid
            filtered_dict['message_sent_to'] = message.to
            filtered_dict['message_body'] = message.body
    return filtered_dict

@app.route('/filter_by/from/<phone_number>', methods=['GET'])
def filter_from(phone_number):
    client = Client(twilio_account_sid, twilio_auth_token)
    messages = client.messages.list(limit=20)
    phone_number = '+1' + str(phone_number)
    filtered_dict = {}
    for message in messages:
        if message.from_ == phone_number:
            filtered_dict['message_sid'] = message.sid
            filtered_dict['message_sent_from'] = message.from_
            filtered_dict['message_body'] = message.body
    return filtered_dict

if __name__ == '__main__':
    app.run(host="0.0.0.0")


# TODO: create twilio app microservice to create message, read message, filter message (from and to phone numbers)
# if no filter specified, show all by account_sid
# filter by
# url/send_message
# return data for a message for a given message sid

# follow CRUD format with endpoints
# know when to use get vs post

# have high level plan and communicate that in the beginning
# have endpoints, expected input and output (any contracts for the inputs/outputs?)
#
