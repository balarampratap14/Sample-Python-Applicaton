#!/usr/bin/env python
from flask import Flask
app = Flask(__name__)

@app.route('/')
@app.route('/hello/')
def hello_world():
    return 'Hello World! Your Python Application Is succesfully Up and Running.\n Created and Written By Balaram Pratap'
