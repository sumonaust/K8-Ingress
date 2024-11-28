# Simple Python Application

from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'hostbase ingress controller'

if __name__ == '__main__':
    app.run(host='0.0.0.0')
