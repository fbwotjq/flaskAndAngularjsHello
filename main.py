from flask import Flask, json

app = Flask(__name__)
#app.config['STATIC_FOLDER'] = 'static'

@app.route("/")
def root():
    return "This is root page"

@app.route("/justGet", methods=['GET'])
def justGet():
    returnData = json.dumps({'name':'fbwotjq', 'id': 'jaco.ryu', 'type':'GET'})
    return returnData

@app.route("/justPost", methods=['Post'])
def justPost():
    returnData = json.dumps({'name':'fbwotjq', 'id': 'jaco.ryu', 'type':'POST'})
    return returnData

@app.route("/someUrl", methods=['GET'])
def someUrl():
    returnData = json.dumps({'user':{'name': 'fbwotjq', 'id': 'jaco.ryu', 'type': 'POST'}})
    return returnData

if __name__ == "__main__":
    app.run()