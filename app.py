import os
from flask import Flask, jsonify, request
from math import sqrt

app = Flask(__name__)

@app.route('/')
def fibo():
    prx = 1
    ant = 0
    lim = 49
    found = 0
    resp = "0, "
    while(found < lim):
        tmp = prx
        prx += ant
        ant = tmp
        found += 1
        resp += str(prx) + ","
        if(found % 10 == 0):
        	resp+= "<br>"
    return resp

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
