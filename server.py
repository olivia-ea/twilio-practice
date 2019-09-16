from views import app

if __name__ == '__main__':
    app.run(host="0.0.0.0")


# if no filter specified, show all by account_sid
# filter by
# url/send_message
# return data for a message for a given message sid

# follow CRUD format with endpoints
# know when to use get vs post

# have high level plan and communicate that in the beginning
# have endpoints, expected input and output (any contracts for the inputs/outputs?)
#
# @app.route is a route decorator that tells Flask that the URL should trigger a specific function
# also route decorator binds function to URL
