'''from flask import Flask, request

app = Flask(__name__)

@app.route('/', methods=['POST'])
def home():
    return request.data
    return "<h1>High Priority</h1>"

if __name__ == '__main__':
    app.run()




from flask import Flask, request
import requests

app = Flask(__name__)

@app.route('/', methods=['POST'])
def home():
    return "<h1>TESTING</h1>"


bugData={
    "Priority":"High","Bug ID":"11xh374","Build Number":"3.3.4","Reported on":"23/04/2022","Reason":"Defect","Environment":"macOS Sierra 10.12.6"
}
r = requests.post('https://prod-17.uksouth.logic.azure.com:443/workflows/232e0cfdb4f04a02be8b0ca021abe229/triggers/manual/paths/invoke?api-version=2016-10-01&sp=%2Ftriggers%2Fmanual%2Frun&sv=1.0&sig=d15OaKaplzQQgvAtA3thcBSzDxq92eM_7OeiVTiVonU',data=bugData)
print(r.text)'''

'''
highurl = "https://prod-17.uksouth.logic.azure.com:443/workflows/232e0cfdb4f04a02be8b0ca021abe229/triggers/manual/paths/invoke?api-version=2016-10-01&sp=%2Ftriggers%2Fmanual%2Frun&sv=1.0&sig=d15OaKaplzQQgvAtA3thcBSzDxq92eM_7OeiVTiVonU"
apikey = 

@app.route('/', methods=['POST'])
def home():
    
    data = requests.data
    r = requests.post(highurl, data=data)
    requests.post(url = highurl, data = "Test from API")
    print(r.text)

    for i in data:
        if i['Priority'] == 'High':
            request.post(url = highurl, data = data)

if __name__ == '__main__':
    app.run()'''