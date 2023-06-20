from flask import Flask, render_template, request, json

import requests
import json
#from chatterbot import ChatBot
#from chatterbot.trainers import ChatterBotCorpusTrainer
 
app = Flask(__name__)
 
#english_bot = ChatBot("Chatterbot", storage_adapter="chatterbot.storage.SQLStorageAdapter")
#trainer = ChatterBotCorpusTrainer(english_bot)
#trainer.train("chatterbot.corpus.english")
 
@app.route("/")
def home():
    return render_template("index.html")
 
@app.route("/get")
def get_bot_response():
    userText = request.args.get('msg')
    json_data = {"prompt": userText}
    print("json_data------------------------> "+str(json_data))
    headers = {'Accept' : 'application/json', 'Content-Type' : 'application/json'}
    resp = requests.post(url="https://genpactaiservice.azurewebsites.net/invokeopenapi", json=json_data, headers=headers, verify=False)
    #resp = []
    #resp = requests.post(url="https://localhost:5000/invokeopenapi", json=json_data, headers=headers, verify=False)
    response_dict = json.loads(resp.text)
    response_list = response_dict['output']
    for eachitem in response_list:
        print(eachitem)
        print()
        print()
    #respOut = str(resp.text).replace("}", "").replace("{output:", "").replace("{\"output\":\"", "").replace("\"", "")
    return "<b>-</b> " + "\n\n<b>-</b> ".join(response_list)

if __name__ == "__main__":
    app.run(host='0.0.0.0', ssl_context='adhoc')
