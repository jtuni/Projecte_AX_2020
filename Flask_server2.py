from flask import Flask, request, render_template
import os

#todo:
#acabat !

app = Flask(__name__)

@app.route("/")
def hello():
    return render_template('Server2.html')

if __name__ == '__main__':
    app.run(debug=False, host="10.0.10.2", port=80)
