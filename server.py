from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

i = 0

@app.route("/increment")
def increment():
    global i 
    i += 1
    return f"<p>{i}</p>"


app.run()

