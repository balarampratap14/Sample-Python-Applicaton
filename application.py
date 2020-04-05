#!/usr/bin/env python
from flask import Flask
app = Flask(__name__)

@app.route('/')
    def hello_world():
        return 'Hello World!'

#@app.route('/hello/<username>') # dynamic route
#def hello_user(username):
   # return 'HEY! Hello %s!\n. Welcome to my UserPage.!!!!!' % username

if __name__ == '__main__':
    app.run(host='0.0.0.0')     # open for everyone
#   This Is Where Developers Should Start and Must be only file to be edited by any Developer #
