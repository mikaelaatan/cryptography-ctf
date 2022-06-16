#!/usr/bin/env python3

from flask import Flask, request, jsonify, render_template
from binascii import hexlify, unhexlify
from base64 import b64decode
from hashlib import sha1

app = Flask(__name__)
app.config['DEBUG'] = False

FLAG = # redacted
MAX_LEN = 100000

@app.route('/', methods=['GET'])
def home():
    return render_template('index.html')

@app.route('/login', methods=['POST'])
def login():
    if 'user' in request.form and 'pass' in request.form:
        try:
            username = b64decode(request.form['user'])
            password = b64decode(request.form['pass'])

            if len(username) > MAX_LEN or len(password) > MAX_LEN:
                return jsonify({'error': 'Request is too large.'})
            elif username == password:
                return jsonify({'error': 'Your password cannot be the same as your username.'})
            elif sha1(username).digest() == sha1(password).digest():
                return FLAG
            else:
                return jsonify({'error': 'Incorrect password.'})
        except:
            return jsonify({'error': 'Invalid request.'})
    else:
        return jsonify({'error': 'Invalid request.'})

if __name__ == '__main__':
    app.run(port=18401)

