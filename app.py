from flask import Flask, request, requests
app = Flask(__name__)

highurl = "https://prod-17.uksouth.logic.azure.com:443/workflows/232e0cfdb4f04a02be8b0ca021abe229/triggers/manual/paths/invoke?api-version=2016-10-01&sp=%2Ftriggers%2Fmanual%2Frun&sv=1.0&sig=d15OaKaplzQQgvAtA3thcBSzDxq92eM_7OeiVTiVonU"
apikey = "T6pFf9c3AHQKzMcnuHyeQqQE23AI578W01V94uw0mj965nAvBYklRYvu2l6frY3jm6IEHnQSbs7V+AStJWuQIQ=="

@app.route('/', methods=['POST'])
def home():
    data = request.data
    for i in data:
        if i['Priority'] == 'High':
            requests.post(url = highurl, data = data)

if __name__ == '__main__':
    app.run(host='0.0.0.0',port=9090)