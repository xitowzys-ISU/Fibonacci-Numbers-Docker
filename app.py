from flask import Flask, redirect, url_for, request, render_template
import random
from math import sqrt

app = Flask(__name__)

def fib_2(N):
      
    a = 0
    b = 1

    if N < 2:
        return 1
     
    for i in range(1, N):
        c = a + b
        a = b
        b = c
    return b

@app.route('/', methods=["POST", "GET"])
def index():
    if request.method == "POST":
        N = int(request.form["fib_num"])
        return redirect(url_for("fib_result", usr=str(fib_2(N))))

    return render_template('index.html')

@app.route('/<usr>')
def fib_result(usr):
    return f"<h1>{usr}</h1>"

if __name__ == "__main__":
    app.run(host="0.0.0.0")
