#  Creating an instance of the flask app
from flask import Flask

app = Flask(__name__)

# Routing and dynamic routing

@app.route('/')
def welcome():
    return 'Welcome to Phase Four'

@app.route('/<string:username>')
def user(username):
    return f'This is the profile of Student {username}'

# Create a development server

if __name__ == '__main__':
    app.run(port=5554)