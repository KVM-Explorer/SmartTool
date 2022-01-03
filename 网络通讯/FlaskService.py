from flask import Flask
import json
app = Flask(__name__)
 
@app.route('/')
def hello_world():
	return 'hello world'
 
@app.route('/DeviceInfo')
def DevideInfo():
    text={"Version":2,"Data":3}
    json.dumps(text)
    return text

@app.route('/SystemInfo')
def SystemInfo():
    text = {"CPU":10}
    return text

@app.route('/StateInfo')
def StateInfo():
    text = {"Speed":10}
    return text


if __name__ == '__main__':
    app.run(port=8000,debug= True,host='0.0.0.0')
