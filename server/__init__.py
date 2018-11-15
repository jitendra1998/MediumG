from flask import Flask, request
app = Flask(__name__)
from server import flaskcode

if __name__ == '__main__':
    app.run(debug=True)