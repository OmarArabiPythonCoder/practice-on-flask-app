from flask import Flask # this Flask is defferent because it is a class not a module

app = Flask(__name__) # name is always set to __main__ in your python file

@app.route("/")
def hello_world():
    return "Hello, World!"

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)