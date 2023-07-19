from flask import Flask, render_template, request, json, jsonify
import re
import requests
import subprocess
import json
#from chatterbot import ChatBot
#from chatterbot.trainers import ChatterBotCorpusTrainer
 
app = Flask(__name__)
 
#english_bot = ChatBot("Chatterbot", storage_adapter="chatterbot.storage.SQLStorageAdapter")
#trainer = ChatterBotCorpusTrainer(english_bot)
#trainer.train("chatterbot.corpus.english")


def create_jira_issue(issue_data, jira_base_url, username, password):
    api_url = f"{jira_base_url}/rest/api/2/issue"

    headers = {
        "Content-Type": "application/json"
    }

    auth = (username, password)

    response = requests.post(api_url, headers=headers, auth=auth, json=issue_data)
    #print(response)
    if response.status_code == 201:
        print("Issue created successfully.")
        issue_key = response.json().get("key")
        return(f"Issue Key: {issue_key}")
    else:
        print("Failed to create issue.")
        return(f"Response: {response.text}")



@app.route("/")
def home():
    return render_template("index.html")
 
@app.route("/get")
def get_bot_response():
    userText = request.args.get('msg')
    ansibleOutput = ""
    if ("execute ansible-playbook" in userText):
        cmdexcute = str(userText).split("execute ")[1]
        #cmdexcuteabsoutepath = "cd /home/azureuser/genpactaiservice/ && " + cmdexcute + " && cd /home/azureuser/chatbot/genpactknowledgebase/"
        cmdexcuteabsoutepath = cmdexcute
        print (cmdexcuteabsoutepath)
        ansibleOut = subprocess.Popen(cmdexcuteabsoutepath, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
        ansibleOutput = ansibleOut.stdout.read().strip().decode('utf-8').replace('\\n', '\n')
        #.replace('\n', '<br/>')
        print (ansibleOutput)
        ansibleOutputForView = ansibleOutput.replace('\n', '<br/>')
        #return (ansibleOutput)
        #ansibleOutputInJSON = json.dumps(ansibleOutput)
        return (ansibleOutputForView)

    if ("jira" in userText):
        issue_type = ""
        summary = ""
        description = ""
        list_params = userText.split(",")
        for eachitem in list_params :
            if ("=" in eachitem): 
                if ("issue_type" in eachitem.strip().split("=")[0]):
                    issue_type = eachitem.split("=")[1]
                if ("summary" in eachitem.strip().split("=")[0]):
                    summary = eachitem.split("=")[1]
                if ("description" in eachitem.strip().split("=")[0]):
                    description = eachitem.split("=")[1]
                

        api_url = "https://api.openai.com/v1/completions"
        headers = {
                    "Authorization": "Bearer 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",
                    "Content-Type": "application/json"
                  }

        # Define the prompt template
        prompt = """
        Create Jira issue:
        - Project: {project}
        - Issue type: {issue_type}
        - Summary: {summary}
        - Description: {description}

        ---
        User: Create Jira issue
        Jira project: {project}
        Issue type: {issue_type}
        Summary: {summary}
        Description: {description}

        Jira: {{jira.issue.create, instance='https://aravintha1.atlassian.net', apiKey='ATCTT3xFfGN0NuXAD04C3XZfbvSzTwE88lQpFHV5nNfBapRDXwQQ_XMSdCG8GT1XLbKg-vpyHvdcjtmdgyQ-5PVWze7YvMb7rN1R7wVAp_uXk7ho4xM01nEmT9MrTDCvWCKJec4Iq2iowz9mkh-5BKHA_HVfct3kWRCG7g8zQCHLhA6xCxDfI2Q=4A8EBC00'}}
        """

        formatted_prompt = prompt.format(
        project="FP",
        issue_type=issue_type,
        summary=summary,
        description=description
        )
        print("formatted_prompt -> "+str(formatted_prompt))
        messages = [
                      {"role": "system", "content": "You are a Jira bot."},
                      {"role": "user", "content": formatted_prompt}
                   ]

        data = {
                "model": "text-davinci-003",
                #"messages": messages,
                "prompt": formatted_prompt,
                "max_tokens": 100,
                "temperature": 0.7
               }

        response = requests.post(api_url, headers=headers, json=data)
        issue = response.json()["choices"][0]["text"].strip().replace('\n', '<br/>')
        print("Generated Jira issue:")
        print(issue)
        issue_data = {
                     "fields": {
                            "project": {
                             "key": "FP"
                                    },
        "summary": summary,
        "description": description,
        "issuetype": {
            "name": issue_type
                            } 
                          }
                            }
        #issue_data_json = json.dumps(issue_data)

        responsejirafunction = create_jira_issue(issue_data, 'https://aravintha1.atlassian.net', 'vibhorsaxena2@gmail.com' , 'ATCTT3xFfGN0NuXAD04C3XZfbvSzTwE88lQpFHV5nNfBapRDXwQQ_XMSdCG8GT1XLbKg-vpyHvdcjtmdgyQ-5PVWze7YvMb7rN1R7wVAp_uXk7ho4xM01nEmT9MrTDCvWCKJec4Iq2iowz9mkh-5BKHA_HVfct3kWRCG7g8zQCHLhA6xCxDfI2Q=4A8EBC00')
        return ("Generated Jira issue: "+ issue)



    json_data = {"prompt": userText}
    print("json_data------------------------> "+str(json_data))
    headers = {'Accept' : 'application/json', 'Content-Type' : 'application/json'}
    resp = requests.post(url="https://genpactaiservice.azurewebsites.net/invokeopenapi", json=json_data, headers=headers, verify=False)
    #resp = []
    #resp = requests.post(url="https://localhost:5000/invokeopenapi", json=json_data, headers=headers, verify=False)
    response_dict = json.loads(resp.text)
    response_list = response_dict['output']
    orig_response_list = response_list
    for eachitem in response_list:
        print(eachitem)
        print()
        print()
    #respOut = str(resp.text).replace("}", "").replace("{output:", "").replace("{\"output\":\"", "").replace("\"", "")
    #return "<b>-</b> " + "\n\n<b>-</b> ".join(response_list)
    playbook_filename = ""
    if ("ansible-playbook" in str(response_list)):
         playbook_filename = str(response_list).split("ansible-playbook ")[1].split()[0]
         print("playbook_filename-->")
         print(playbook_filename)
    #orig_response_list_dispatch = orig_response_list.replace('\n', '<br/>') 
    orig_response_list_dispatch = [
    item.replace('\n', '<br/>')
    for item in orig_response_list
    ]    
    return "".join(orig_response_list_dispatch)
    #return jsonify({orig_response_list})

#if __name__ == "__main__":
#    app.run(host='0.0.0.0', ssl_context='adhoc')


if __name__ == "__main__":
    app.run(host='0.0.0.0', port='5050', ssl_context='adhoc')
