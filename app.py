from flask import Flask, request

app = Flask(__name__)
'''
@app.route("/")
def hello():
    return "High Priority"
'''

@app.route('/', methods=['POST'])
def home():
    return request.data
    return "<h1>High Priority</h1>"

if __name__ == '__main__':
    app.run(host='0.0.0.0',port=9090)

