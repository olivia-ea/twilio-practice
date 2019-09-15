from flask import Flask
import requests
from twilio.rest import Client

twilio_phone_number = '+15106171282'
twilio_account_sid = 'AC3050c3bf79b5dd9f74ea488e99f06297'
twilio_auth_token = '994dbb8e2b8e10188a7fdf1228d57926'

app = Flask(__name__)

@app.route('/send_sms') # /messages/ needs to be POST not get (to use headers and format message)
def send_message():
    client = Client(twilio_account_sid, twilio_auth_token)
    mock = Mock(client)
    message = client.messages.create(
                              body='Hi there!',
                              from_=twilio_phone_number,
                              to='+15106487309'
                            )
    sid_dict = {}
    sid_dict['sid'] = message.sid
    print(sid_dict)
    return sid_dict

@app.route('/read_sms/<id>') # /message/<message_id>
def read_message(id):
    # json to include account sid, api verson, body, date created

    client = Client(twilio_account_sid, twilio_auth_token)

    message = client.messages(id).fetch()

    message_dict = {}
    message_dict['account_sid'] = message.account_sid
    message_dict['api_version'] = message.api_version
    message_dict['body'] = message.body
    message_dict['date_created'] = message.date_created
    return message_dict

@app.route('/filter_sent_to/<phone_number>')
def filter_sent_to(phone_number):
    client = Client(twilio_account_sid, twilio_auth_token)

    messages = client.messages.list(
        from_=twilio_phone_number,
        to=phone_number,
        limit=20
    )

    filtered_dict = {}

    for message in messages:
        filtered_dict[message.sid] = message.body

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
