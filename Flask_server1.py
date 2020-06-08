from flask import Flask, request, render_template
import os
import random
import time

app = Flask(__name__)

@app.route("/")
def hello():
    return "199.209.11.3"

if __name__ == '__main__':
    port_gen=random.randint(10024,11024)
    app.run(host='10.0.0.1', port=port_gen)
