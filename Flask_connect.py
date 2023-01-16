from flask import Flask, request, jsonify
import requests
import json

app = Flask(__name__)

# Dialogflow API endpoint
DF_ENDPOINT = "https://dialogflow.googleapis.com/v2/projects/<project_id>/agent/sessions/<session_id>:detectIntent"

@app.route("/webhook", methods=["POST"])
def webhook():
    # Get the request data from LINE
    req = request.get_json(silent=True, force=True)
    # Extract the text from the request
    text = req["events"][0]["message"]["text"]
    # Create the data to send to Dialogflow
    data = {
        "queryInput": {
            "text": {
                "text": text,
                "languageCode": "en"
            }
        }
    }
    # Send the data to Dialogflow
    headers = {
        "Authorization": "Bearer <dialogflow_access_token>",
        "Content-Type": "application/json"
    }
    res = requests.post(DF_ENDPOINT, json=data, headers=headers)
    # Extract the response from Dialogflow
    df_res = res.json()
    # Get the response text
    response_text = df_res["queryResult"]["fulfillmentText"]
    # Send the response text back to LINE
    line_res = {
        "to": req["events"][0]["source"]["userId"],
        "messages": [
            {
                "type": "text",
                "text": response_text
            }
        ]
    }
    line_endpoint = "https://api.line.me/v2/bot/message/reply"
    line_headers = {
        "Content-Type": "application/json",
        "Authorization": "Bearer <line_access_token>"
    }
    requests.post(line_endpoint, json=line_res, headers=line_headers)
    return jsonify(req)

if __name__ == "__main__":
    app.run(debug=True)