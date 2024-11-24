# Simple Python Application to demonstrate Ingress in Kubernetes

from flask import Flask
app = Flask(__name__)

@app.route('/')
def get_value():
    return 'host sample-1'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)
