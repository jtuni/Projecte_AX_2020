from flask import Flask, request, render_template
import os
import random
import time

#todo:
#que el port canvii cada 10-15 segons pero que el server no deixi de puto funcionar

app = Flask(__name__)

@app.route("/")
def hello():
    return render_template('Server1.html')

if __name__ == '__main__':
	#for i in range(1,2000):
		#port_gen=random.randint(1024,49151)
    		app.run(debug=False, host="0.0.0.0", port=2000) #aquest es el rang de ports que podem fer servir
	#	time.sleep(15)
		#print(port_gen)
