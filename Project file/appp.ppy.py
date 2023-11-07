from flask import Flask, render_template, request


travel = Flask(__name__) # initializng the flask app


@travel.route('/')
def helloworld():
    return render_template("index.html")
if __name__ == '__main__':
    travel.run(debug = False, port = 5000)