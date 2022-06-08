from flask import Flask

app = flask.Flask(__name__)
'''
@app.route("/")
def hello():
    return "High Priority"
'''

@app.route('/')
def home():
    return "<h1>High Priority</h1>"

if __name__ == '__main__':
    app.run(port=9090)

