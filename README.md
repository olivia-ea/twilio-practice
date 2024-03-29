# Twilio Microservice Challenge

## Table of Contents
* [Tasks](#tasks)
* [Tech Stack](#tech-stack)
* [Setting Up/Installation](#installation)
* [Files Explained](#files-explained)
* [How Handle the Post Request](#post-request)
* [Testing](#testing)
* [Personal](#personal)

## Tasks
Create a microservice that uses the Twilio API to do the following things:
* Create an SMS message
* Fetch individual message
* Read multiple messages with from and to filters

## Tech Stack
* Backend: Python, Flask
* APIs: Twilio API

## Installation

To run the Twilio microservice on your local computer, follow these steps:

Clone repository:
```
$ git clone https://github.com/olivia-ea/twilio-practice.git
```

Set up virtual environment:

```
$ virtualenv venv
```

Activate virtual envirnoment:
```
$ source venv/bin/activate
```

Install dependencies:
```
$ pip3 install -r requirements.txt
```

Get Client account SID, authorization token and phone number from Twilio and save them to a file secrets.sh:
```
export TWILIO_ACCOUNT_SID=YOUR_SID
export TWILIO_AUTH_TOKEN=YOUR_TOKEN
export TWILIO_PHONE_NUMBER=YOUR_PHONE_NUMBER
```

Run from the command line:
```
$ python3 server.py
```

Open localhost:5000 on browser.


## Files Explained
### server.py
* This file contains code only relating to the server.

### views.py
* This file contains the all the endpoints for the Twilio microservice.
* The functions hit the following endpoints:
    * /messages
    * /messages/<message_id>
    * /filter_by/
    * /filter_by/sent/<phone_number>
    * /filter_by/from/<phone_number>
* When each endpoint is hit, the request runs the respective get/post request by first making an API call to the Twilio API then casting the response into json. The return statement then parses through the json to give the desired format.

| URL      | HTTP Request Type     | Action     | Output     |
| :------------- | :---------- | :---------- | :----------- |
|  /messages | POST   | Creates a new custom message to a custom phone number from a Twilio phone number.    | Returns the message SID, the phone number of the received message, the phone number of the sender and the message body.   |
|  /messages/<message_id> | GET   | Given a specific message SID, displays the message content.    | Returns the message SID, API version, message contents, and date created.    |
|  /filter_by/ | GET   | Displays all the messages from the registered Twilio account.    | Returns the all the registered user's message SIDs, phone number of messages sent and received and message contents.    |
|  /filter_by/sent/<phone_number> | GET   | Given a phone number, displays all the messages that were sent to the specified phone numnber.    | Returns the filtered messages' SID, phone number sent to and message contents.    |
| /filter_by/from/<phone_number>   | GET | Given a phone number, displays all the messages that were sent from the specified phone numnber.    | Returns the filtered messages' SID, phone number sent from and message contents. \|

### testing.py
* Contains unit testing for above files. There is an individual function to test each endpoint using assert statements. The valid id tests are checking for a 200 status code and if a response is present whereas the invalid id tests are checking for a 404 status code.

## Post Request

Use Postman to access the post request for the /messages endpoint.

1. Run the server:

```
$ python3 server.py
```

2. Select "Post" request and enter 'http://localhost:5000/messages'
3. Select the headers tab and for key put 'Content-Type' and for value put 'application/json'
4. Switch to the body tab and select raw with JSON(application/json) format
5. Input custom data in form like so: {'message_body': <custom_message>, 'phone_number': <custom_phone_number>}
6. Press send

## Testing

In order to run the unit tests in the testing.py file, first run server.py and then the nosetest.

```
$ python3 server.py
```

```
$ nosetests --verbosity=2 testing.py
```

## Personal

### Major challenges
IN PROGRESS

### New things I learned:
IN PROGRESS

### Future enhancements:
IN PROGRESS


### Feedback
* Rename the endpoints to be more organized and CRUD compliant.
    * Simplified the endpoints to make routing more organized and RESTful.

* Optional vs required params
    * Created more endpoints with optional params

* Store app credentials securely
    * Stored credentials as environment variables

* More error handling