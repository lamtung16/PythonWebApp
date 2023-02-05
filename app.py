from flask import Flask
from flask import Blueprint, render_template, request
import numpy as np
import matplotlib.pyplot as plt


app = Flask(__name__)

@app.route("/", methods=['GET', 'POST'])
def home():
    return render_template("index.html")

@app.route("/result", methods = ["POST", "GET"])
def result():
    output = request.form.to_dict()
    t = output["t"]
    if(t.lstrip('-+').isnumeric()):
        t = float(t)*1.0
    else:
        t = 1.0
    x = np.arange(-10, 10, 0.011)

    # export image
    plt.plot(x, np.power(x, t), 'k')
    plt.xlabel('x')
    plt.ylabel('f(x)')
    plt.savefig("static/image.pdf")
    plt.savefig("static/image.png")
    plt.close()

    return render_template("index.html", t=t)

if __name__ == '__main__':
    app.run(debug=True, port=8000)